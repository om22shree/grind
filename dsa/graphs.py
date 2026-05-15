from collections import deque, defaultdict, Counter
import heapq
from typing import List, Dict, Set, Tuple, Optional


Grid = List[List[int]]
Graph = Dict[int, List[int]]
WeightedGraph = Dict[int, List[Tuple[int, int]]]


class UnionFind:
    """Disjoint-set template for cycle/connectivity questions."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        self.count -= 1
        return True


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
    """LeetCode 200. BFS template for grid reachability."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            islands += 1
            grid[r][c] = "0"
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
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


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """LeetCode 207. Kahn topo sort: cycle exists if not all nodes are consumed."""
    graph = defaultdict(list)
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    q = deque(i for i, degree in enumerate(indegree) if degree == 0)
    taken = 0

    while q:
        node = q.popleft()
        taken += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return taken == num_courses


def find_course_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    q = deque(i for i, degree in enumerate(indegree) if degree == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return order if len(order) == num_courses else []


def has_cycle_dfs(num_nodes: int, edges: List[Tuple[int, int]]) -> bool:
    """Directed graph cycle detection with 0/1/2 color marking."""
    graph = build_graph(edges, directed=True)
    color = [0] * num_nodes

    def dfs(node: int) -> bool:
        color[node] = 1
        for nei in graph[node]:
            if color[nei] == 1:
                return True
            if color[nei] == 0 and dfs(nei):
                return True
        color[node] = 2
        return False

    return any(color[node] == 0 and dfs(node) for node in range(num_nodes))


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """LeetCode 743. Dijkstra with adjacency list + min-heap."""
    graph = defaultdict(list)
    for src, dst, weight in times:
        graph[src].append((dst, weight))

    dist = {}
    heap = [(0, k)]

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = cost
        for nei, weight in graph[node]:
            if nei not in dist:
                heapq.heappush(heap, (cost + weight, nei))

    return max(dist.values()) if len(dist) == n else -1


def shortest_path(n: int, edges: List[Tuple[int, int, int]], start: int) -> List[float]:
    graph = defaultdict(list)
    for a, b, weight in edges:
        graph[a].append((b, weight))

    dist = [float("inf")] * n
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for nei, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                heapq.heappush(heap, (new_cost, nei))
    return dist


def redundant_connection(edges: List[List[int]]) -> Optional[List[int]]:
    uf = UnionFind(len(edges) + 1)
    for a, b in edges:
        if not uf.union(a, b):
            return [a, b]
    return None


def count_components(n: int, edges: List[List[int]]) -> int:
    uf = UnionFind(n)
    for a, b in edges:
        uf.union(a, b)
    return uf.count


def update_matrix(mat: Grid) -> Grid:
    """LeetCode 542. Multi-source BFS from every zero."""
    rows, cols = len(mat), len(mat[0])
    q = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                q.append((r, c))
            else:
                mat[r][c] = -1

    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))

    return mat


def oranges_rotting(grid: Grid) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while q:
        r, c, minutes = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, minutes + 1))

    return minutes if fresh == 0 else -1


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    words = set(word_list)
    if end_word not in words:
        return 0

    patterns = defaultdict(list)
    for word in words | {begin_word}:
        for i in range(len(word)):
            patterns[word[:i] + "*" + word[i + 1:]].append(word)

    q = deque([(begin_word, 1)])
    seen = {begin_word}

    while q:
        word, distance = q.popleft()
        if word == end_word:
            return distance
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            for nxt in patterns[pattern]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, distance + 1))
            patterns[pattern].clear()
    return 0


def cheapest_flight_with_k_stops(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    """LeetCode 787. Bellman-Ford bounded to k + 1 edges."""
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        next_prices = prices[:]
        for a, b, price in flights:
            if prices[a] != float("inf"):
                next_prices[b] = min(next_prices[b], prices[a] + price)
        prices = next_prices

    return -1 if prices[dst] == float("inf") else int(prices[dst])


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    return [num for num, _ in Counter(nums).most_common(k)]


def kth_largest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def merge_sorted_log_streams(streams: List[List[Tuple[int, str]]]) -> List[Tuple[int, str]]:
    """Infra-flavored merge-k-sorted-lists: (timestamp, message)."""
    heap = []
    for stream_id, stream in enumerate(streams):
        if stream:
            ts, msg = stream[0]
            heapq.heappush(heap, (ts, stream_id, 0, msg))

    merged = []
    while heap:
        ts, stream_id, idx, msg = heapq.heappop(heap)
        merged.append((ts, msg))
        next_idx = idx + 1
        if next_idx < len(streams[stream_id]):
            next_ts, next_msg = streams[stream_id][next_idx]
            heapq.heappush(heap, (next_ts, stream_id, next_idx, next_msg))

    return merged


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
