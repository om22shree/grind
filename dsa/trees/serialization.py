from collections import deque
from typing import Optional

from .traversal import TreeNode


def serialize(root: Optional[TreeNode]) -> str:
    if not root:
        return ""

    values = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node:
            values.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            values.append("#")

    while values and values[-1] == "#":
        values.pop()
    return ",".join(values)


def deserialize(data: str) -> Optional[TreeNode]:
    if not data:
        return None

    values = data.split(",")
    root = TreeNode(int(values[0]))
    q = deque([root])
    idx = 1

    while q and idx < len(values):
        node = q.popleft()
        if idx < len(values) and values[idx] != "#":
            node.left = TreeNode(int(values[idx]))
            q.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] != "#":
            node.right = TreeNode(int(values[idx]))
            q.append(node.right)
        idx += 1

    return root
