# Infra Design And SRE-Flavored Drills

Source file: `dsa/rate_limiter.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Infra-Flavored Local Builds.

Root README concepts:
- token bucket
- sliding-window log
- fixed window
- health-check window
- consistent hashing
- ring buffer

## Recognition Prompts

1. Allow at most `N` requests per user in the last `W` seconds.
2. Allow bursts up to capacity, but refill steadily over time.
3. Count requests per fixed time bucket.
4. Mark a service unhealthy if too many recent checks failed.
5. Map keys to servers so adding/removing servers moves limited keys.
6. Store the last `N` events with constant-time overwrite.

## Coding Questions

### Q1. Sliding Window Log Rate Limiter

Implement `allow(key, now)`.

State:
- map key to deque of timestamps
- expire timestamps outside the window

### Q2. Token Bucket Rate Limiter

Implement `allow(key, now, cost=1.0)`.

State:
- tokens available
- last refill time

Interview line:

```text
Token bucket allows bursts up to capacity while enforcing average refill rate.
```

### Q3. Fixed Window Rate Limiter

Implement `allow(key, now)`.

State:
- current window id
- count in that window

### Q4. Health Check Window

Implement `record(service, ok)`.

Return whether the service is healthy after recording the check.

### Q5. Consistent Hashing Sketch

Design a minimal consistent hash ring.

Implement:
- `add_server(server)`
- `remove_server(server)`
- `get_server(key)`

Focus on:
- sorted ring positions
- `bisect` for lookup
- wraparound at end of ring

### Q6. Ring Buffer Sketch

Implement fixed-capacity event buffer.

Methods:
- `append(value)`
- `to_list()` in oldest-to-newest order

## SRE Adaptation Prompts

1. How would you rate limit per API key and per IP at the same time?
2. How would you merge logs from 20 services by timestamp?
3. How would you model service dependencies as a graph?
4. How would you detect a deployment cycle in dependency metadata?
5. How would you route customer IDs across cache nodes?
