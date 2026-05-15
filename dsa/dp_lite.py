import bisect
from functools import lru_cache
from typing import List


def climb_stairs(n: int) -> int:
    prev, cur = 1, 1
    for _ in range(n):
        prev, cur = cur, prev + cur
    return prev


def house_robber(nums: List[int]) -> int:
    skip = take = 0
    for num in nums:
        skip, take = max(skip, take), skip + num
    return max(skip, take)


def coin_change(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if value >= coin:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return -1 if dp[amount] == float("inf") else int(dp[amount])


def word_break(s: str, word_dict: List[str]) -> bool:
    words = set(word_dict)
    max_len = max(map(len, words), default=0)

    @lru_cache(None)
    def dp(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, min(len(s), i + max_len) + 1):
            if s[i:j] in words and dp(j):
                return True
        return False

    return dp(0)


def longest_increasing_subsequence(nums: List[int]) -> int:
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)


def unique_paths(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(m - 1):
        for col in range(1, n):
            row[col] += row[col - 1]
    return row[-1]


if __name__ == "__main__":
    assert house_robber([2, 7, 9, 3, 1]) == 12
    assert coin_change([1, 2, 5], 11) == 3
    assert word_break("leetcode", ["leet", "code"]) is True
