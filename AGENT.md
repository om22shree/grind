# AGENT.md

This repository is an interview-prep pattern library for DevOps/SRE-flavored coding rounds. The goal is fast recall, not broad textbook coverage. Keep files small, executable, and easy to rehearse from memory.

Do not depend on the reference PDFs. They are optional manual additions under `revision_roadmaps/` and are not required to reproduce or work with this repo.

## Repo Purpose

Build a Python-first command center for common coding interview patterns:

- Graph traversal, dependencies, shortest paths, and connectivity.
- Heaps for top-k, k-way merge, scheduling, and streaming medians.
- Linked-list pointer patterns and LRU cache design.
- Tree traversal, BST constraints, tree DP, serialization, and trie/prefix lookup.
- Cross-cutting arrays/string patterns: sliding window, two pointers, binary search, intervals, light DP, and rate limiters.

Every implementation should help the user answer four interview prompts:

```python
# Pattern:
# Invariant:
# Complexity:
# Interview line:
```

## Required Structure

Recreate this source structure:

```text
.
├── AGENT.md
├── README.md
└── dsa/
    ├── README.md
    ├── common-imports.py
    ├── binary_search.py
    ├── dp_lite.py
    ├── heaps.py
    ├── intervals.py
    ├── rate_limiter.py
    ├── sliding_window.py
    ├── two_pointers.py
    ├── graphs/
    │   ├── __init__.py
    │   ├── bellman_ford.py
    │   ├── dijkstra.py
    │   ├── matrix_bfs.py
    │   ├── topo_sort.py
    │   ├── traversal.py
    │   ├── union_find.py
    │   └── word_ladder.py
    ├── heaps/
    │   ├── __init__.py
    │   ├── merge_k.py
    │   ├── scheduling.py
    │   └── top_k.py
    ├── linkedlists/
    │   ├── __init__.py
    │   ├── basics.py
    │   ├── cache.py
    │   └── merge.py
    └── trees/
        ├── __init__.py
        ├── bst.py
        ├── dfs_properties.py
        ├── serialization.py
        ├── traversal.py
        └── trie.py
```

Ignore and do not reproduce:

- `revision_roadmaps/*.pdf`
- `__pycache__/`
- `*.pyc`
- local editor state

## Root README

The root `README.md` should describe the repo as job-switch grind material and point to the DSA pattern layout. Include these ideas:

- Important Python3 imports.
- Standard algo implementations that can be modified on the fly.
- Recall-oriented pattern folders:
  - `dsa/graphs/`: traversal, topo sort, union-find, Dijkstra, matrix BFS, word ladder, bounded Bellman-Ford.
  - `dsa/heaps/`: top-k, merge-k, scheduling, running median.
  - `dsa/linkedlists/`: pointer basics, merge/reorder patterns, LRU cache.
  - `dsa/trees/`: traversals, BST, DFS properties, serialization, trie/prefix lookup.
- Cross-cutting pattern files:
  - `dsa/sliding_window.py`
  - `dsa/two_pointers.py`
  - `dsa/binary_search.py`
  - `dsa/intervals.py`
  - `dsa/heaps.py`
  - `dsa/dp_lite.py`
  - `dsa/rate_limiter.py`

Also keep the system-design reminders:

- Rate limiter: token bucket.
- Rate limiter: sliding window log.
- Consistent hashing.
- Ring buffer.
- Quick revision notes.

## DSA README

`dsa/README.md` is the practice command center. It must contain a table:

```text
File | Pattern | Must-solve problems | Recall line
```

Rows should cover:

- `common-imports.py`
- All top-level pattern files.
- Every implementation file under `graphs/`, `heaps/`, `linkedlists/`, and `trees/`.

End with this practice loop:

1. Pick one row.
2. Read the recall line.
3. Re-type the core function from memory.
4. Run a tiny test.
5. Say pattern, invariant, complexity, and interview line out loud.

## Common Imports

`dsa/common-imports.py` is the import drill sheet. Keep it short:

```python
from collections import deque, defaultdict, Counter, OrderedDict
import heapq
import bisect
import math
from functools import lru_cache
from typing import List, Dict, Set, Tuple, Optional
```

Maximize these imports throughout the repo where appropriate:

- `deque`: BFS, queues, sliding windows.
- `defaultdict`: adjacency lists, grouped state, counters with defaults.
- `Counter`: frequency problems.
- `OrderedDict`: concise LRU cache.
- `heapq`: priority queues, Dijkstra, top-k, k-way merge.
- `bisect`: binary-search boundaries and LIS tails.
- `math`: clean numeric helpers when useful.
- `lru_cache`: memoized recursion.
- typing imports: make templates easier to read.

## File Style

Use plain Python. No external dependencies.

Every practice function and important class method should have this comment block immediately above it:

```python
# Pattern: short name of the pattern.
# Invariant: what remains true while the algorithm runs.
# Complexity: O(...) time, O(...) space.
# Interview line: one sentence to say out loud before or after coding.
def function_name(...):
    ...
```

For class methods, indent the comment block inside the class:

```python
class MedianFinder:
    # Pattern: two heaps for streaming median.
    # Invariant: small has lower half, large has upper half.
    # Complexity: O(1) setup, O(n) space.
    # Interview line: two heaps keep the median at the heap tops.
    def __init__(self):
        ...
```

Nested helpers that encode the main trick should also get prompt comments, especially DFS helpers, tree DP helpers, trie suffix DP helpers, and cache linked-list helpers.

Keep comments compact and practical. These are recall prompts, not lecture notes.

## Top-Level Pattern Files

### `dsa/sliding_window.py`

Include:

- `max_average_subarray`
- `length_of_longest_substring`
- `min_window_substring`
- `sliding_window_maximum`
- `find_anagrams`
- `longest_repeating_character_replacement`

Use `deque`, `defaultdict`, and `Counter`.

### `dsa/two_pointers.py`

Include:

- `two_sum_sorted`
- `three_sum`
- `max_area`
- `trap_rain_water`
- `remove_duplicates`
- `move_zeroes`
- `is_subsequence`
- `valid_palindrome`
- `sort_colors`

Focus on pointer movement invariants.

### `dsa/binary_search.py`

Include:

- `binary_search`
- `lower_bound`
- `upper_bound`
- `count_occurrences`
- `search_rotated`
- `min_eating_speed`
- `ship_within_days`

Use `bisect` for boundary helpers and `math` where useful. Search-on-answer functions must clearly define `feasible(...)`.

### `dsa/intervals.py`

Include:

- `merge_intervals`
- `insert_interval`
- `erase_overlap_intervals`
- `can_attend_meetings`
- `min_meeting_rooms`
- `interval_intersection`

Use sorting and `heapq` for meeting rooms.

### `dsa/heaps.py`

This is a compact rehearsal sheet duplicating the most useful heap patterns from `dsa/heaps/`.

Include:

- `ListNode`
- `kth_largest`
- `top_k_frequent`
- `k_closest_points`
- `merge_k_sorted_arrays`
- `merge_k_lists`
- `merge_sorted_log_streams`
- `least_interval`
- `MedianFinder`

Use `Counter` and `heapq`.

### `dsa/dp_lite.py`

Include only light, high-yield DP:

- `climb_stairs`
- `house_robber`
- `coin_change`
- `word_break`
- `longest_increasing_subsequence`
- `unique_paths`

Use `lru_cache` for memoized DFS and `bisect` for LIS.

### `dsa/rate_limiter.py`

Include infra-flavored implementations:

- `SlidingWindowLogRateLimiter`
- `TokenBucketRateLimiter`
- `FixedWindowRateLimiter`
- `HealthCheckWindow`

Use `deque`, `defaultdict`, `math`, and typing. The goal is to bridge coding rounds to SRE/DevOps systems talk.

## Graph Modules

### `dsa/graphs/traversal.py`

Include:

- `Graph` type alias.
- `build_graph`
- `bfs_order`
- `dfs_order`
- `num_islands`
- `flood_fill_dfs`

Use `deque` for BFS and `defaultdict(list)` for graph construction.

### `dsa/graphs/topo_sort.py`

Include:

- `can_finish`
- `find_course_order`
- `has_cycle_dfs`

Use Kahn topo sort and DFS color marking.

### `dsa/graphs/union_find.py`

Include:

- `UnionFind`
- `redundant_connection`
- `count_components`

Use path compression and union by rank. `union` should return `False` when two nodes are already connected.

### `dsa/graphs/dijkstra.py`

Include:

- `network_delay_time`
- `shortest_path`

Use adjacency list plus `heapq`.

### `dsa/graphs/matrix_bfs.py`

Include:

- `Grid` type alias.
- `update_matrix`
- `oranges_rotting`

Use multi-source BFS.

### `dsa/graphs/word_ladder.py`

Include:

- `ladder_length`

Use wildcard buckets and BFS.

### `dsa/graphs/bellman_ford.py`

Include:

- `cheapest_flight_with_k_stops`

Use bounded Bellman-Ford with a copied price array each round.

### `dsa/graphs/__init__.py`

Re-export the public graph functions/classes via `__all__`. Keep it thin; no algorithm logic.

## Heap Modules

### `dsa/heaps/top_k.py`

Include:

- `kth_largest`
- `top_k_frequent`
- `top_k_frequent_heap`
- `k_closest_points`

### `dsa/heaps/merge_k.py`

Include:

- `ListNode`
- `merge_k_sorted_arrays`
- `merge_k_lists`
- `merge_sorted_log_streams`

### `dsa/heaps/scheduling.py`

Include:

- `least_interval`
- `MedianFinder`

### `dsa/heaps/__init__.py`

Re-export heap utilities via `__all__`.

## Linked List Modules

### `dsa/linkedlists/basics.py`

Include:

- `ListNode`
- `build_linked_list`
- `to_list`
- `reverse_list`
- `has_cycle`
- `detect_cycle_start`
- `middle_node`
- `is_palindrome`

### `dsa/linkedlists/merge.py`

Include:

- `merge_two_lists`
- `merge_k_lists`
- `remove_nth_from_end`
- `reorder_list`

Import `ListNode` and `reverse_list` from `.basics`.

### `dsa/linkedlists/cache.py`

Include:

- `LRUCache` using `OrderedDict`
- `ManualLRUCache` using hashmap plus doubly-linked list

### `dsa/linkedlists/__init__.py`

Re-export linked-list helpers via `__all__`.

## Tree Modules

### `dsa/trees/traversal.py`

Include:

- `TreeNode`
- `build_tree_level`
- `preorder_recursive`
- `inorder_recursive`
- `postorder_recursive`
- `inorder_iterative`
- `level_order`

### `dsa/trees/bst.py`

Include:

- `is_valid_bst`
- `kth_smallest`
- `lowest_common_ancestor_bst`

Import `TreeNode` from `.traversal`.

### `dsa/trees/dfs_properties.py`

Include:

- `max_depth`
- `diameter_of_binary_tree`
- `is_balanced`
- `path_sum`
- `max_path_sum`

### `dsa/trees/serialization.py`

Include:

- `serialize`
- `deserialize`

Use BFS with `deque` and `#` as null sentinel.

### `dsa/trees/trie.py`

Include:

- `TrieNode`
- `Trie`
- `word_break`

Use `defaultdict(TrieNode)` for lazy trie children and `lru_cache` for `word_break`.

### `dsa/trees/__init__.py`

Re-export tree and trie utilities via `__all__`.

## Smoke Tests

Some files should include a tiny `if __name__ == "__main__":` section with 2-3 assertions. Keep these short and deterministic. They are smoke checks, not a full test suite.

Good candidates:

- `sliding_window.py`
- `two_pointers.py`
- `binary_search.py`
- `intervals.py`
- `heaps.py`
- `dp_lite.py`
- `rate_limiter.py`

## Verification

After edits, run:

```bash
python3 -m py_compile dsa/*.py dsa/graphs/*.py dsa/heaps/*.py dsa/linkedlists/*.py dsa/trees/*.py
```

For quick import smoke testing:

```bash
python3 -c "from dsa.graphs.traversal import num_islands; from dsa.heaps.scheduling import MedianFinder; from dsa.linkedlists.basics import build_linked_list; from dsa.trees.trie import Trie; print(num_islands([['1','0'],['1','1']])); m=MedianFinder(); m.add_num(1); m.add_num(2); print(m.find_median(), build_linked_list([1]), Trie)"
```

Expected output includes:

```text
1
1.5 ListNode(1) <class 'dsa.trees.trie.Trie'>
```

## How To Extend

When adding a new pattern:

1. Prefer an existing pattern file or folder.
2. Add one small, memorable implementation.
3. Add the four-line mental model comment.
4. Add a row to `dsa/README.md`.
5. Use imports from `common-imports.py` where appropriate.
6. Add a tiny smoke assertion only if it improves confidence without clutter.
7. Run `py_compile`.

Do not add:

- Heavy frameworks.
- Long explanation blocks.
- Large test harnesses.
- Exotic algorithms unless they are common in the target interview patterns.
- PDF-dependent content.

## Working Principles

- Optimize for interview recall.
- Prefer simple, idiomatic Python over cleverness.
- Keep each file small enough to rehearse.
- Make invariants explicit.
- Use infra analogies where useful: dependency graphs, scheduler queues, merged log streams, service discovery prefixes, caches, health checks, and rate limits.
- Preserve the practice-command-center role of `dsa/README.md`.
