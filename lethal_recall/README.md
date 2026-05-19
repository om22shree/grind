# Lethal Recall

This directory is for turning the `dsa/` pattern library into interview muscle memory.
Use it as a drill mat: read a prompt, identify the pattern, state the invariant, code from
memory, then compare against the source file only after you have a working attempt.

For concrete problems, use `leetcode_targets.md`. The topic files are the recall drills; the
LeetCode target sheet is the actual problem list.

## Rules

1. No passive reading first.
2. For every question, say these four lines before or after coding:
   - Pattern:
   - Invariant:
   - Complexity:
   - Interview line:
3. Re-type the core function from memory.
4. Run a tiny test.
5. If stuck, read only the matching function signature and comments from `dsa/`.
6. Repeat misses the next day.

## Directory Map

| Directory | Purpose |
|---|---|
| `arrays_and_strings/` | Sliding window, two pointers, binary search, intervals |
| `graphs/` | BFS/DFS, topo sort, union-find, shortest paths, grid BFS |
| `heaps/` | Top-k, k-way merge, scheduling, streaming median |
| `linkedlists/` | Pointer rewiring, dummy nodes, fast/slow, LRU cache |
| `trees/` | Traversal, BST, postorder properties, serialization, trie |
| `dp/` | Memoization, rolling DP, coin change, word break, LIS |
| `infra_design/` | Rate limiters, health windows, SRE-flavored adaptations |
| `mixed_rounds/` | Timed rounds that mix patterns the way interviews do |

Start with `drill_index.md` when you want to choose by problem smell instead of topic name.
Start with `leetcode_targets.md` when you want exact problems to solve.

## Daily Loop

### 30-Minute Recall Session

1. Pick one topic file.
2. Do 3 warm-up recognition prompts without coding.
3. Code 2 full questions from memory.
4. Explain one solution as if to an interviewer.
5. Mark misses in `miss_log.md`.

### 60-Minute Lethal Session

1. Pick one weak area.
2. Code 4 questions from that area.
3. Do 1 mixed-round question cold.
4. Re-code the hardest one without looking.
5. Write the invariant from memory.

## Scoring

| Score | Meaning |
|---|---|
| 0 | Could not identify pattern |
| 1 | Identified pattern but needed source |
| 2 | Solved with hints or major pauses |
| 3 | Solved cleanly from memory |
| 4 | Solved cleanly and explained invariant/complexity |
| 5 | Solved fast, tested edge cases, and gave a crisp interview explanation |

## Promotion Rule

A pattern is not "known" until you score 4 or 5 on three separate days.
