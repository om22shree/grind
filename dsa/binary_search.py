import bisect
import math
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def lower_bound(nums: List[int], target: int) -> int:
    return bisect.bisect_left(nums, target)


def upper_bound(nums: List[int], target: int) -> int:
    return bisect.bisect_right(nums, target)


def count_occurrences(nums: List[int], target: int) -> int:
    return upper_bound(nums, target) - lower_bound(nums, target)


def search_rotated(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def min_eating_speed(piles: List[int], h: int) -> int:
    def feasible(speed: int) -> bool:
        return sum(math.ceil(pile / speed) for pile in piles) <= h

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left


def ship_within_days(weights: List[int], days: int) -> int:
    def feasible(capacity: int) -> bool:
        needed = 1
        load = 0
        for weight in weights:
            if load + weight > capacity:
                needed += 1
                load = 0
            load += weight
        return needed <= days

    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    assert binary_search([1, 3, 5], 3) == 1
    assert count_occurrences([1, 2, 2, 2, 3], 2) == 3
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
