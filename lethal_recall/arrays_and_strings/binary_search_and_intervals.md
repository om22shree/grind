# Binary Search And Intervals Drills

Sources:
- `dsa/binary_search.py`
- `dsa/intervals.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Arrays And Strings -> Binary Search / Intervals.

## Binary Search Recognition

1. Find exact target in sorted array.
2. Find first insertion position for target.
3. Count target occurrences.
4. Search a rotated sorted array.
5. Minimize eating speed so all piles finish by `h`.
6. Minimize ship capacity so all packages ship within `days`.

## Binary Search Coding Questions

### Q1. Classic Binary Search

Return index or `-1`.

State the loop invariant before coding.

### Q2. Lower Bound / Upper Bound

Implement using `bisect`, then implement manually.

### Q3. Rotated Array Search

Return target index in rotated sorted array with distinct values.

Interview line:

```text
At every step, one half is sorted; use that half to decide whether target can live there.
```

### Q4. Koko Eating Bananas

Return minimum integer speed.

Required:
- define `feasible(speed)`
- binary search the first feasible speed

### Q5. Ship Packages Within D Days

Return minimum capacity.

Bounds:
- low is max weight
- high is sum of weights

## Interval Recognition

1. Merge all overlapping intervals.
2. Insert one interval into sorted non-overlapping intervals.
3. Remove minimum intervals to eliminate overlap.
4. Decide if one person can attend all meetings.
5. Find minimum meeting rooms.
6. Intersect two sorted interval lists.

## Interval Coding Questions

### Q6. Merge Intervals

Sort by start, then merge into an output list.

### Q7. Insert Interval

Use three phases:
- add intervals before new interval
- merge overlaps
- add intervals after new interval

### Q8. Meeting Rooms II

Return minimum rooms needed.

Invariant:

```text
The min-heap stores end times of meetings currently occupying rooms.
```

### Q9. Interval List Intersections

Use two pointers over two sorted interval lists.
