# Lab: Binary Trees – Depth and Ancestors

**Completed Sept 30, 2026**


A Python implementation of two classic binary tree problems:

1. **Maximum Depth**: finds the number of nodes on the longest path from the root to a leaf.
2. **Lowest Common Ancestor (BST)**: finds the deepest node that has two given nodes as descendants in a Binary Search Tree.

## Files

- `binary_tree_lab.py`: the `TreeNode` class and both function implementations
- `binary_tree_tests.py`: unit tests for both functions

## Requirements

- Python 3.x (no external packages needed)

## How to Run

1. Clone the repository:
```
   git clone https://github.com/hanjennings1/binary-tree-lab.git
   cd binary-tree-lab
```
2. Run the test suite:
```
   python binary_tree_tests.py
```
   If `python` isn't recognized, use `python3` instead.

## Approach

**`max_depth`**: Uses recursion. An empty tree has depth 0. Otherwise, a node's depth is the deeper of its left and right subtrees, plus 1 for the node itself.

**`lowest_common_ancestor`**: Uses the BST property (left < node < right). If both values are smaller than the current node, search left. If both are larger, search right. Otherwise the values split at this node (or one of them is this node), so it is the LCA.