# Sliding Window Drills

Source file: `dsa/sliding_window.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Arrays And Strings -> Sliding Window.

## Recognition Prompts

1. You need the best average over exactly `k` consecutive values.
2. You need the longest substring with no repeated character.
3. You need the shortest substring containing all characters of another string.
4. You need the max value in every window of size `k`.
5. You need every start index where a permutation of `p` appears in `s`.
6. You can replace at most `k` characters to make the longest repeated-character substring.

For each prompt, answer:

```text
Pattern:
Window type:
State stored:
Shrink condition:
```

## Coding Questions

### Q1. Max Average Subarray

Given `nums` and integer `k`, return the maximum average of any contiguous subarray of length `k`.

Force yourself to use:
- rolling sum
- no nested loops

### Q2. Longest Substring Without Repeating Characters

Return the length of the longest substring without duplicate characters.

Edge cases:
- empty string
- all same character
- duplicate appears before current window start

### Q3. Minimum Window Substring

Return the minimum substring of `s` containing all characters from `t`, including duplicates.

Before coding, say:

```text
I expand right to satisfy requirements, then shrink left while the window remains valid.
```

### Q4. Sliding Window Maximum

Return the maximum for every window of size `k`.

Required invariant:

```text
The deque stores candidate indices in decreasing value order, and expired indices leave from the front.
```

### Q5. Find All Anagrams

Return all start indices of anagrams of `p` in `s`.

Constraint:
- Keep the window size exactly `len(p)` after warm-up.

### Q6. Longest Repeating Character Replacement

Given uppercase string `s` and integer `k`, return the longest substring length after replacing at most `k` characters.

Core check:

```text
window_length - max_frequency <= k
```

## Speed Ladder

1. Code Q1 and Q2 in 12 minutes.
2. Code Q3 alone in 15 minutes.
3. Code Q4 alone in 12 minutes.
4. Code Q5 and Q6 in 20 minutes.
