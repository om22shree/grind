# Dependencies And Paths Drills

Sources:
- `dsa/graphs/topo_sort.py`
- `dsa/graphs/union_find.py`
- `dsa/graphs/dijkstra.py`
- `dsa/graphs/bellman_ford.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Graphs -> Dependencies, Connectivity, Paths.

## Recognition Prompts

1. Course prerequisites, can all courses be finished?
2. Need one valid ordering of dependent tasks.
3. Need to detect a directed cycle.
4. Need to detect redundant edge in an undirected graph.
5. Need number of connected components.
6. Need shortest signal time with non-negative weights.
7. Need shortest path from one source to all nodes.
8. Need cheapest flight with at most `k` stops.

## Coding Questions

### Q1. Course Schedule

Return whether all courses can be completed.

Invariant:

```text
Zero indegree nodes are ready to process.
```

### Q2. Course Schedule II

Return one valid course order, or empty list if impossible.

### Q3. Directed Cycle With DFS Colors

Return whether a directed graph has a cycle.

Color meaning:
- `0`: unvisited
- `1`: visiting
- `2`: done

### Q4. Union Find

Implement:
- `find` with path compression
- `union` with size/rank

### Q5. Redundant Connection

Return the edge that creates an undirected cycle.

Interview line:

```text
A failed union means both endpoints were already connected.
```

### Q6. Count Components

Return number of connected components in an undirected graph.

### Q7. Network Delay Time

Return time for signal to reach all nodes, or `-1`.

Invariant:

```text
With non-negative weights, the first heap pop finalizes the shortest distance.
```

### Q8. Cheapest Flights Within K Stops

Use bounded Bellman-Ford.

Required:
- copy previous distances each round
- each round adds at most one edge
