# Trees, BST, Serialization, Trie Drills

Sources:
- `dsa/trees/traversal.py`
- `dsa/trees/bst.py`
- `dsa/trees/dfs_properties.py`
- `dsa/trees/serialization.py`
- `dsa/trees/trie.py`

Actual problems: see `lethal_recall/leetcode_targets.md` -> Trees.

## Recognition Prompts

1. Build a tree from level-order values.
2. Return preorder, inorder, or postorder traversal.
3. Return level-order traversal.
4. Validate a BST.
5. Find kth smallest in BST.
6. Find LCA in BST.
7. Compute max depth.
8. Compute diameter.
9. Check if tree is height-balanced.
10. Return root-to-leaf paths matching a sum.
11. Compute max path sum.
12. Serialize and deserialize a binary tree.
13. Implement prefix search.
14. Solve word break with trie or memoized DFS.

## Coding Questions

### Q1. Traversal Pack

Implement:
- preorder recursive
- inorder recursive
- postorder recursive
- inorder iterative
- level order

### Q2. Validate BST

Use lower and upper bounds.

Invariant:

```text
Every node must be strictly between the bounds inherited from ancestors.
```

### Q3. Kth Smallest In BST

Use inorder traversal.

### Q4. LCA In BST

Walk down using BST ordering.

### Q5. Max Depth

Return `1 + max(left_depth, right_depth)`.

### Q6. Diameter Of Binary Tree

Return height upward, update diameter at each node.

### Q7. Balanced Binary Tree

Return `-1` early if any subtree is imbalanced.

### Q8. Path Sum II

Use DFS backtracking.

### Q9. Binary Tree Maximum Path Sum

Return one-sided gain upward, update global two-sided path at node.

### Q10. Serialize / Deserialize

Use null sentinels to preserve shape.

### Q11. Trie

Implement:
- `insert`
- `search`
- `starts_with`

### Q12. Word Break

Use memoized DFS over string index.
