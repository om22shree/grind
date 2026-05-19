# DP Lite Drills

Source file: `dsa/dp_lite.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> DP.

## Recognition Prompts

1. Number of ways to climb stairs with 1 or 2 steps.
2. Max money from houses without robbing adjacent houses.
3. Minimum coins to make an amount.
4. Can a string be segmented into dictionary words?
5. Length of longest increasing subsequence.
6. Number of unique paths in an `m x n` grid.

## Coding Questions

### Q1. Climbing Stairs

Use rolling Fibonacci-style DP.

### Q2. House Robber

Use choose/skip state.

Invariant:

```text
At each house, best is either previous best or current value plus best before previous.
```

### Q3. Coin Change

Use bottom-up unbounded coin DP.

### Q4. Word Break

Use memoized DFS by start index.

Before coding, state:

```text
The state is whether suffix s[i:] can be segmented.
```

### Q5. Longest Increasing Subsequence

Use patience sorting tails plus binary search.

### Q6. Unique Paths

Use one-row grid DP.

## DP Smell Checklist

- What is the state?
- What choices transition from that state?
- What is the base case?
- Can I compress memory?
- Am I minimizing, maximizing, counting, or deciding feasibility?
