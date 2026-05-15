from collections import Counter
import heapq
from typing import List


def kth_largest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    return [num for num, _ in Counter(nums).most_common(k)]


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    heap = []
    for num, count in Counter(nums).items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])
