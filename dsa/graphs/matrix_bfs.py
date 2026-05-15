from collections import deque
from typing import List


Grid = List[List[int]]


def update_matrix(mat: Grid) -> Grid:
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
