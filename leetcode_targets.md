# LeetCode Targets

Use this as the concrete problem sheet. The markdown drills teach recall; these are the actual
LeetCode-style reps to grind until the pattern fires automatically.

Priority:
- `Core`: must become instant recall.
- `Reinforce`: same pattern, slightly different shape.
- `Stretch`: harder variant or interview-pressure variant.

## Arrays And Strings

### Sliding Window

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 643 | Maximum Average Subarray I | `dsa/sliding_window.py::max_average_subarray` |
| Core | 3 | Longest Substring Without Repeating Characters | `dsa/sliding_window.py::length_of_longest_substring` |
| Core | 76 | Minimum Window Substring | `dsa/sliding_window.py::min_window_substring` |
| Core | 239 | Sliding Window Maximum | `dsa/sliding_window.py::sliding_window_maximum` |
| Core | 438 | Find All Anagrams in a String | `dsa/sliding_window.py::find_anagrams` |
| Core | 424 | Longest Repeating Character Replacement | `dsa/sliding_window.py::longest_repeating_character_replacement` |
| Reinforce | 567 | Permutation in String | fixed window frequency match |
| Reinforce | 209 | Minimum Size Subarray Sum | variable window minimum |
| Reinforce | 1004 | Max Consecutive Ones III | variable window with at most `k` bad items |
| Stretch | 992 | Subarrays with K Different Integers | exactly-k via at-most-k |

### Two Pointers

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 167 | Two Sum II - Input Array Is Sorted | `dsa/two_pointers.py::two_sum_sorted` |
| Core | 15 | 3Sum | `dsa/two_pointers.py::three_sum` |
| Core | 11 | Container With Most Water | `dsa/two_pointers.py::max_area` |
| Core | 42 | Trapping Rain Water | `dsa/two_pointers.py::trap_rain_water` |
| Core | 26 | Remove Duplicates from Sorted Array | `dsa/two_pointers.py::remove_duplicates` |
| Core | 283 | Move Zeroes | `dsa/two_pointers.py::move_zeroes` |
| Core | 392 | Is Subsequence | `dsa/two_pointers.py::is_subsequence` |
| Core | 125 | Valid Palindrome | `dsa/two_pointers.py::valid_palindrome` |
| Core | 75 | Sort Colors | `dsa/two_pointers.py::sort_colors` |
| Reinforce | 977 | Squares of a Sorted Array | two ends, fill from back |
| Reinforce | 18 | 4Sum | sorted anchor plus two pointers |

### Binary Search

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 704 | Binary Search | `dsa/binary_search.py::binary_search` |
| Core | 35 | Search Insert Position | lower bound |
| Core | 34 | Find First and Last Position of Element in Sorted Array | lower/upper bound |
| Core | 33 | Search in Rotated Sorted Array | `dsa/binary_search.py::search_rotated` |
| Core | 875 | Koko Eating Bananas | `dsa/binary_search.py::min_eating_speed` |
| Core | 1011 | Capacity To Ship Packages Within D Days | `dsa/binary_search.py::ship_within_days` |
| Reinforce | 153 | Find Minimum in Rotated Sorted Array | rotated boundary |
| Reinforce | 162 | Find Peak Element | binary search on slope |
| Stretch | 410 | Split Array Largest Sum | search-on-answer |

### Intervals

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 56 | Merge Intervals | `dsa/intervals.py::merge_intervals` |
| Core | 57 | Insert Interval | `dsa/intervals.py::insert_interval` |
| Core | 435 | Non-overlapping Intervals | `dsa/intervals.py::erase_overlap_intervals` |
| Core | 252 | Meeting Rooms | `dsa/intervals.py::can_attend_meetings` |
| Core | 253 | Meeting Rooms II | `dsa/intervals.py::min_meeting_rooms` |
| Core | 986 | Interval List Intersections | `dsa/intervals.py::interval_intersection` |
| Reinforce | 452 | Minimum Number of Arrows to Burst Balloons | greedy by end |
| Stretch | 759 | Employee Free Time | merge schedules |

## Graphs

### Traversal And Grid BFS

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 200 | Number of Islands | `dsa/graphs/traversal.py::num_islands` |
| Core | 733 | Flood Fill | `dsa/graphs/traversal.py::flood_fill_dfs` |
| Core | 133 | Clone Graph | BFS/DFS with visited map |
| Core | 542 | 01 Matrix | `dsa/graphs/matrix_bfs.py::update_matrix` |
| Core | 994 | Rotting Oranges | `dsa/graphs/matrix_bfs.py::oranges_rotting` |
| Core | 127 | Word Ladder | `dsa/graphs/word_ladder.py::ladder_length` |
| Reinforce | 695 | Max Area of Island | grid DFS component size |
| Reinforce | 130 | Surrounded Regions | boundary flood fill |
| Stretch | 1091 | Shortest Path in Binary Matrix | BFS shortest path |

### Dependencies, Connectivity, Paths

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 207 | Course Schedule | `dsa/graphs/topo_sort.py::can_finish` |
| Core | 210 | Course Schedule II | `dsa/graphs/topo_sort.py::find_course_order` |
| Core | 684 | Redundant Connection | `dsa/graphs/union_find.py::redundant_connection` |
| Core | 323 | Number of Connected Components in an Undirected Graph | `dsa/graphs/union_find.py::count_components` |
| Core | 743 | Network Delay Time | `dsa/graphs/dijkstra.py::network_delay_time` |
| Core | 787 | Cheapest Flights Within K Stops | `dsa/graphs/bellman_ford.py::cheapest_flight_with_k_stops` |
| Reinforce | 261 | Graph Valid Tree | union-find or DFS |
| Reinforce | 785 | Is Graph Bipartite? | BFS coloring |
| Stretch | 778 | Swim in Rising Water | Dijkstra / binary search + BFS |

## Heaps

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 215 | Kth Largest Element in an Array | `dsa/heaps/top_k.py::kth_largest` |
| Core | 347 | Top K Frequent Elements | `dsa/heaps/top_k.py::top_k_frequent` |
| Core | 973 | K Closest Points to Origin | `dsa/heaps/top_k.py::k_closest_points` |
| Core | 23 | Merge k Sorted Lists | `dsa/heaps/merge_k.py::merge_k_lists` |
| Core | 621 | Task Scheduler | `dsa/heaps/scheduling.py::least_interval` |
| Core | 295 | Find Median from Data Stream | `dsa/heaps/scheduling.py::MedianFinder` |
| Reinforce | 703 | Kth Largest Element in a Stream | fixed-size min-heap |
| Reinforce | 1046 | Last Stone Weight | repeated max item |
| Stretch | 480 | Sliding Window Median | two heaps with lazy deletion |

## Linked Lists

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 206 | Reverse Linked List | `dsa/linkedlists/basics.py::reverse_list` |
| Core | 141 | Linked List Cycle | `dsa/linkedlists/basics.py::has_cycle` |
| Core | 142 | Linked List Cycle II | `dsa/linkedlists/basics.py::detect_cycle_start` |
| Core | 876 | Middle of the Linked List | `dsa/linkedlists/basics.py::middle_node` |
| Core | 234 | Palindrome Linked List | `dsa/linkedlists/basics.py::is_palindrome` |
| Core | 21 | Merge Two Sorted Lists | `dsa/linkedlists/merge.py::merge_two_lists` |
| Core | 23 | Merge k Sorted Lists | `dsa/linkedlists/merge.py::merge_k_lists` |
| Core | 19 | Remove Nth Node From End of List | `dsa/linkedlists/merge.py::remove_nth_from_end` |
| Core | 143 | Reorder List | `dsa/linkedlists/merge.py::reorder_list` |
| Core | 146 | LRU Cache | `dsa/linkedlists/cache.py::LRUCache` |
| Reinforce | 2 | Add Two Numbers | dummy head |
| Reinforce | 24 | Swap Nodes in Pairs | pointer rewiring |

## Trees

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 102 | Binary Tree Level Order Traversal | `dsa/trees/traversal.py::level_order` |
| Core | 94 | Binary Tree Inorder Traversal | `dsa/trees/traversal.py::inorder_iterative` |
| Core | 98 | Validate Binary Search Tree | `dsa/trees/bst.py::is_valid_bst` |
| Core | 230 | Kth Smallest Element in a BST | `dsa/trees/bst.py::kth_smallest` |
| Core | 235 | Lowest Common Ancestor of a BST | `dsa/trees/bst.py::lowest_common_ancestor_bst` |
| Core | 104 | Maximum Depth of Binary Tree | `dsa/trees/dfs_properties.py::max_depth` |
| Core | 543 | Diameter of Binary Tree | `dsa/trees/dfs_properties.py::diameter_of_binary_tree` |
| Core | 110 | Balanced Binary Tree | `dsa/trees/dfs_properties.py::is_balanced` |
| Core | 113 | Path Sum II | `dsa/trees/dfs_properties.py::path_sum` |
| Core | 124 | Binary Tree Maximum Path Sum | `dsa/trees/dfs_properties.py::max_path_sum` |
| Core | 297 | Serialize and Deserialize Binary Tree | `dsa/trees/serialization.py` |
| Core | 208 | Implement Trie | `dsa/trees/trie.py::Trie` |
| Core | 139 | Word Break | `dsa/trees/trie.py::word_break` |
| Reinforce | 236 | Lowest Common Ancestor of a Binary Tree | postorder recursion |
| Reinforce | 199 | Binary Tree Right Side View | BFS levels |
| Stretch | 212 | Word Search II | trie + backtracking |

## DP

| Priority | LeetCode | Title | Local Pattern |
|---|---:|---|---|
| Core | 70 | Climbing Stairs | `dsa/dp_lite.py::climb_stairs` |
| Core | 198 | House Robber | `dsa/dp_lite.py::house_robber` |
| Core | 322 | Coin Change | `dsa/dp_lite.py::coin_change` |
| Core | 139 | Word Break | `dsa/dp_lite.py::word_break` |
| Core | 300 | Longest Increasing Subsequence | `dsa/dp_lite.py::longest_increasing_subsequence` |
| Core | 62 | Unique Paths | `dsa/dp_lite.py::unique_paths` |
| Reinforce | 213 | House Robber II | circular choose/skip |
| Reinforce | 377 | Combination Sum IV | counting DP |
| Stretch | 1143 | Longest Common Subsequence | 2D DP |

## Infra-Flavored Local Builds

These are not always clean LeetCode fits. Build them locally from `dsa/rate_limiter.py` and
`lethal_recall/infra_design/rate_limiter_and_sre.md`.

| Priority | Problem | Local Pattern |
|---|---|---|
| Core | Sliding-window log limiter | `dsa/rate_limiter.py::SlidingWindowLogRateLimiter` |
| Core | Token bucket limiter | `dsa/rate_limiter.py::TokenBucketRateLimiter` |
| Core | Fixed-window limiter | `dsa/rate_limiter.py::FixedWindowRateLimiter` |
| Core | Health-check window | `dsa/rate_limiter.py::HealthCheckWindow` |
| Reinforce | Consistent hash ring | `infra_design/rate_limiter_and_sre.md::Q5` |
| Reinforce | Ring buffer | `infra_design/rate_limiter_and_sre.md::Q6` |

## First 30 Core Problems

Do these before spreading out:

1. 3 - Longest Substring Without Repeating Characters
2. 76 - Minimum Window Substring
3. 239 - Sliding Window Maximum
4. 15 - 3Sum
5. 42 - Trapping Rain Water
6. 33 - Search in Rotated Sorted Array
7. 875 - Koko Eating Bananas
8. 56 - Merge Intervals
9. 253 - Meeting Rooms II
10. 200 - Number of Islands
11. 207 - Course Schedule
12. 684 - Redundant Connection
13. 743 - Network Delay Time
14. 787 - Cheapest Flights Within K Stops
15. 215 - Kth Largest Element in an Array
16. 347 - Top K Frequent Elements
17. 23 - Merge k Sorted Lists
18. 295 - Find Median from Data Stream
19. 206 - Reverse Linked List
20. 141 - Linked List Cycle
21. 19 - Remove Nth Node From End of List
22. 146 - LRU Cache
23. 102 - Binary Tree Level Order Traversal
24. 98 - Validate Binary Search Tree
25. 543 - Diameter of Binary Tree
26. 124 - Binary Tree Maximum Path Sum
27. 208 - Implement Trie
28. 322 - Coin Change
29. 300 - Longest Increasing Subsequence
30. Token bucket limiter - local build

