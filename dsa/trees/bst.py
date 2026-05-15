from typing import Optional

from .traversal import TreeNode


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        if not low < node.val < high:
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, float("-inf"), float("inf"))


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right

    raise ValueError("k is larger than the number of nodes")


def lowest_common_ancestor_bst(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur
    return None
