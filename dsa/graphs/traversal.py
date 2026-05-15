from collections import deque, defaultdict
from typing import Dict, List, Tuple


Graph = Dict[int, List[int]]


def build_graph(edges: List[Tuple[int, int]], directed: bool = False) -> Graph:
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        if not directed:
            graph[b].append(a)
    return graph


def bfs_order(graph: Graph, start: int) -> List[int]:
    seen = {start}
    q = deque([start])
    order = []

    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                q.append(nei)

    return order


def dfs_order(graph: Graph, start: int) -> List[int]:
    seen = set()
    order = []

    def dfs(node: int) -> None:
        seen.add(node)
        order.append(node)
        for nei in graph[node]:
            if nei not in seen:
                dfs(nei)

    dfs(start)
    return order


def num_islands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            islands += 1
            grid[r][c] = "0"
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))

    return islands


def flood_fill_dfs(grid: List[List[str]], r: int, c: int, target: str = "1") -> None:
    if not grid or not grid[0]:
        return
    rows, cols = len(grid), len(grid[0])
    if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != target:
        return

    grid[r][c] = "0"
    flood_fill_dfs(grid, r + 1, c, target)
    flood_fill_dfs(grid, r - 1, c, target)
    flood_fill_dfs(grid, r, c + 1, target)
    flood_fill_dfs(grid, r, c - 1, target)
