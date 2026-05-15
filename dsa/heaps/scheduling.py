from collections import Counter
import heapq
from typing import List


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
