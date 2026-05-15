from collections import deque, defaultdict
from functools import lru_cache
from typing import List, Dict, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    idx = 1

    while q and idx < len(values):
        node = q.popleft()
        if idx < len(values) and values[idx] is not None:
            node.left = TreeNode(values[idx])
            q.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            q.append(node.right)
        idx += 1

    return root


def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    stack = []
    order = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        order.append(cur.val)
        cur = cur.right

    return order


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    levels = []
    q = deque([root])

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        levels.append(level)

    return levels


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


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


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


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    return [level[-1] for level in level_order(root)]


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


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    """Prefix lookup template: DNS paths, config keys, service discovery names."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return bool(node and node.is_word)

    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


def word_break(s: str, word_dict: List[str]) -> bool:
    """Light DP template included because it often pairs with trie/prefix questions."""
    words = set(word_dict)
    max_len = max(map(len, words), default=0)

    @lru_cache(None)
    def can_break(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, min(len(s), i + max_len) + 1):
            if s[i:j] in words and can_break(j):
                return True
        return False

    return can_break(0)


if __name__ == "__main__":
    root = build_tree_level([3, 9, 20, None, None, 15, 7])
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    assert max_depth(root) == 3
    trie = Trie()
    trie.insert("consul")
    assert trie.starts_with("con") is True
