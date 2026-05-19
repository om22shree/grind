# Linked List And Cache Drills

Sources:
- `dsa/linkedlists/basics.py`
- `dsa/linkedlists/merge.py`
- `dsa/linkedlists/cache.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Linked Lists.

## Recognition Prompts

1. Reverse a singly linked list.
2. Detect if a linked list has a cycle.
3. Find the cycle start.
4. Find middle node.
5. Check if a list is a palindrome.
6. Merge two sorted lists.
7. Merge k sorted lists.
8. Remove nth node from end.
9. Reorder list as `L0 -> Ln -> L1 -> Ln-1`.
10. Build an LRU cache.

## Coding Questions

### Q1. Reverse List

Before coding:

```text
Save next before rewiring current.next.
```

### Q2. Has Cycle

Use slow and fast pointers.

### Q3. Detect Cycle Start

After slow meets fast, reset one pointer to head and move both one step.

### Q4. Middle Node

Use fast/slow pointer movement.

### Q5. Palindrome Linked List

Use either:
- deque comparison
- reverse second half

### Q6. Merge Two Sorted Lists

Use dummy head and tail pointer.

### Q7. Merge K Sorted Lists

Use min-heap with tie-breaker.

### Q8. Remove Nth From End

Use dummy node and an `n`-node gap.

### Q9. Reorder List

Steps:
- find middle
- reverse second half
- weave two halves

### Q10. LRU Cache

Implement both versions:
- `OrderedDict`
- hashmap plus doubly linked list

Invariant:

```text
Hashmap gives O(1) access; order structure tracks recency.
```
