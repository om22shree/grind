from collections import deque, defaultdict
import math
from typing import Dict


class SlidingWindowLogRateLimiter:
    def __init__(self, limit: int, window_seconds: float):
        self.limit = limit
        self.window_seconds = window_seconds
        self.requests: Dict[str, deque] = defaultdict(deque)

    def allow(self, key: str, now: float) -> bool:
        q = self.requests[key]
        cutoff = now - self.window_seconds

        while q and q[0] <= cutoff:
            q.popleft()

        if len(q) >= self.limit:
            return False

        q.append(now)
        return True


class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate_per_second: float):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_second
        self.tokens = defaultdict(lambda: float(capacity))
        self.last_seen = defaultdict(float)

    def allow(self, key: str, now: float, cost: float = 1.0) -> bool:
        elapsed = max(0.0, now - self.last_seen[key])
        self.tokens[key] = min(self.capacity, self.tokens[key] + elapsed * self.refill_rate)
        self.last_seen[key] = now

        if self.tokens[key] < cost:
            return False

        self.tokens[key] -= cost
        return True


class FixedWindowRateLimiter:
    def __init__(self, limit: int, window_seconds: int):
        self.limit = limit
        self.window_seconds = window_seconds
        self.counts = defaultdict(int)

    def allow(self, key: str, now: float) -> bool:
        window_id = math.floor(now / self.window_seconds)
        bucket = (key, window_id)
        self.counts[bucket] += 1
        return self.counts[bucket] <= self.limit


class HealthCheckWindow:
    def __init__(self, window_size: int, max_failures: int):
        self.window_size = window_size
        self.max_failures = max_failures
        self.events = defaultdict(deque)
        self.failures = defaultdict(int)

    def record(self, service: str, ok: bool) -> bool:
        q = self.events[service]
        q.append(ok)
        if not ok:
            self.failures[service] += 1

        if len(q) > self.window_size:
            old = q.popleft()
            if not old:
                self.failures[service] -= 1

        return self.failures[service] <= self.max_failures


if __name__ == "__main__":
    limiter = SlidingWindowLogRateLimiter(limit=2, window_seconds=10)
    assert limiter.allow("api", 0.0) is True
    assert limiter.allow("api", 1.0) is True
    assert limiter.allow("api", 2.0) is False
