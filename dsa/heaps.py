from collections import Counter
import heapq
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def kth_largest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    return [num for num, _ in Counter(nums).most_common(k)]


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])


def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    heap = []
    for array_id, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], array_id, 0))

    merged = []
    while heap:
        value, array_id, idx = heapq.heappop(heap)
        merged.append(value)
        next_idx = idx + 1
        if next_idx < len(arrays[array_id]):
            heapq.heappush(heap, (arrays[array_id][next_idx], array_id, next_idx))

    return merged


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for idx, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, idx, node))

    dummy = ListNode()
    tail = dummy
    while heap:
        _, idx, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next


def merge_sorted_log_streams(streams: List[List[Tuple[int, str]]]) -> List[Tuple[int, str]]:
    heap = []
    for stream_id, stream in enumerate(streams):
        if stream:
            ts, msg = stream[0]
            heapq.heappush(heap, (ts, stream_id, 0, msg))

    merged = []
    while heap:
        ts, stream_id, idx, msg = heapq.heappop(heap)
        merged.append((ts, msg))
        next_idx = idx + 1
        if next_idx < len(streams[stream_id]):
            next_ts, next_msg = streams[stream_id][next_idx]
            heapq.heappush(heap, (next_ts, stream_id, next_idx, next_msg))

    return merged


def least_interval(tasks: List[str], n: int) -> int:
    counts = [-count for count in Counter(tasks).values()]
    heapq.heapify(counts)
    time = 0

    while counts:
        cooldown = []
        slots = n + 1

        while slots and counts:
            count = heapq.heappop(counts) + 1
            if count:
                cooldown.append(count)
            time += 1
            slots -= 1

        for count in cooldown:
            heapq.heappush(counts, count)

        if counts:
            time += slots

    return time


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2


if __name__ == "__main__":
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert merge_k_sorted_arrays([[1, 4], [1, 3], [2]]) == [1, 1, 2, 3, 4]
