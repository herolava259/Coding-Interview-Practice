from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DiameterOfBinaryTreeSolution:
    def __init__(self, root: Optional[TreeNode]):
        self.root: Optional[TreeNode] = root

    def solve(self) -> int:
        def dfs_diameter(cur_node: Optional[TreeNode]) -> Tuple[int, int]:
            if not cur_node:
                return -1, 0
            max_d_left, max_p_left = dfs_diameter(cur_node.left)
            max_d_right, max_p_right = dfs_diameter(cur_node.right)

            return max(max_d_left, max_d_right, max_p_left + max_p_right + 2), max(max_p_left, max_p_right) + 1

        max_d, _ = dfs_diameter(self.root)

        return max_d
