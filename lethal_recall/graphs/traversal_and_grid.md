# Graph Traversal And Grid BFS Drills

Sources:
- `dsa/graphs/traversal.py`
- `dsa/graphs/matrix_bfs.py`
- `dsa/graphs/word_ladder.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Graphs -> Traversal And Grid BFS.

## Recognition Prompts

1. Visit all reachable nodes from a starting node.
2. Count connected regions of `"1"` cells in a grid.
3. Recolor an entire connected component.
4. Compute distance from every cell to nearest zero.
5. Compute minutes until all oranges rot.
6. Transform one word into another by changing one letter at a time.

## Coding Questions

### Q1. Build Graph

Build an adjacency list from edge pairs.

Variants:
- undirected
- directed

### Q2. BFS Order

Return nodes in BFS order from `start`.

Invariant:

```text
Mark visited when enqueuing so a node enters the queue once.
```

### Q3. DFS Order

Return nodes in DFS preorder.

### Q4. Number Of Islands

Count islands in a grid of `"1"` and `"0"`.

Required:
- mutate visited land or keep a visited set
- avoid revisiting cells

### Q5. Flood Fill DFS

Rewrite all connected `target` cells from a starting point.

### Q6. 01 Matrix

Return distance from each cell to nearest zero.

Key idea:

```text
Start BFS from all zero cells at once.
```

### Q7. Rotting Oranges

Return minutes until all fresh oranges rot, or `-1`.

### Q8. Word Ladder

Return shortest transformation length.

Required:
- wildcard buckets like `h*t`
- BFS by levels
