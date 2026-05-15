import heapq
from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    removed = 0
    prev_end = float("-inf")

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            removed += 1

    return removed


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    intervals.sort()
    return all(intervals[i][0] >= intervals[i - 1][1] for i in range(1, len(intervals)))


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    intervals.sort()
    rooms = []

    for start, end in intervals:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)


def interval_intersection(first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
    i = j = 0
    result = []

    while i < len(first) and j < len(second):
        start = max(first[i][0], second[j][0])
        end = min(first[i][1], second[j][1])
        if start <= end:
            result.append([start, end])

        if first[i][1] < second[j][1]:
            i += 1
        else:
            j += 1

    return result


if __name__ == "__main__":
    assert merge_intervals([[1, 3], [2, 6], [8, 10]]) == [[1, 6], [8, 10]]
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
