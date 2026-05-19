# Heaps Drills

Sources:
- `dsa/heaps.py`
- `dsa/heaps/top_k.py`
- `dsa/heaps/merge_k.py`
- `dsa/heaps/scheduling.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Heaps.

## Recognition Prompts

1. Need kth largest element.
2. Need top k frequent values.
3. Need k closest points to origin.
4. Need merge k sorted arrays.
5. Need merge k sorted linked lists.
6. Need merge sorted timestamped logs.
7. Need schedule tasks with cooldown.
8. Need median from a stream.

## Coding Questions

### Q1. Kth Largest

Return kth largest using heap selection.

Two approaches:
- `heapq.nlargest`
- fixed-size min-heap

### Q2. Top K Frequent

Return k most frequent numbers.

Do it twice:
- `Counter.most_common`
- heap-based fixed-size selection

### Q3. K Closest Points

Return k closest points to origin.

Do not compute square roots.

### Q4. Merge K Sorted Arrays

Emit the smallest current head, then advance that source.

Heap item:

```text
(value, array_index, element_index)
```

### Q5. Merge K Sorted Lists

Use heap with a tie-breaker index.

### Q6. Merge Sorted Log Streams

Merge lists of `(timestamp, message)` pairs.

SRE analogy:

```text
This is reconstructing one ordered event stream from multiple sorted service logs.
```

### Q7. Task Scheduler

Return least intervals to execute tasks with cooldown `n`.

### Q8. Median Finder

Implement:
- `add_num`
- `find_median`

Invariant:

```text
Max-heap has lower half, min-heap has upper half, sizes differ by at most one.
```
