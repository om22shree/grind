from typing import List, Optional

from .traversal import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    height(root)
    return diameter


def is_balanced(root: Optional[TreeNode]) -> bool:
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1


def path_sum(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    paths = []

    def dfs(node: Optional[TreeNode], remaining: int, path: List[int]) -> None:
        if not node:
            return
        path.append(node.val)
        remaining -= node.val
        if not node.left and not node.right and remaining == 0:
            paths.append(path[:])
        dfs(node.left, remaining, path)
        dfs(node.right, remaining, path)
        path.pop()

    dfs(root, target_sum, [])
    return paths


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def gain(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)
        return node.val + max(left, right)

    gain(root)
    return int(best)
