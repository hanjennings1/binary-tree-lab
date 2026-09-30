from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    # BASE CASE: an empty tree with no nodes has depth 0
    if root is None:
        return 0

    # RECURSIVE CASE: find the depth of each side
    left_depth = max_depth(root.left) 
    right_depth = max_depth(root.right) 

    # COMBINE: depth = deeper subtree (left/right) + 1
    return max(left_depth, right_depth) + 1


# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass
