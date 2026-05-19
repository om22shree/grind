# Two Pointers Drills

Source file: `dsa/two_pointers.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Arrays And Strings -> Two Pointers.

## Recognition Prompts

1. Sorted array, find two values summing to target.
2. Need triplets summing to zero without duplicates.
3. Max water between vertical lines.
4. Rainwater trapped between bars.
5. Remove duplicates in-place from sorted array.
6. Move zeroes to the end while preserving non-zero order.
7. Check if one string is a subsequence of another.
8. Check palindrome while ignoring punctuation and case.
9. Sort an array containing only `0`, `1`, and `2`.

## Coding Questions

### Q1. Two Sum II

Return 1-indexed positions for two numbers in a sorted array that add to target.

Interview line:

```text
If the sum is too small, only moving left rightward can increase it.
```

### Q2. 3Sum

Return unique triplets that sum to zero.

Must handle:
- duplicate anchors
- duplicate left/right values after finding a triplet

### Q3. Container With Most Water

Return the maximum container area.

Required reasoning:

```text
Move the shorter wall because the taller wall cannot help while width only shrinks.
```

### Q4. Trapping Rain Water

Return total trapped water.

Invariant:

```text
The side with the lower max boundary determines trapped water at that pointer.
```

### Q5. In-Place Cleanup Pack

Implement from memory:
- `remove_duplicates`
- `move_zeroes`
- `sort_colors`

### Q6. String Pointer Pack

Implement from memory:
- `is_subsequence`
- `valid_palindrome`
