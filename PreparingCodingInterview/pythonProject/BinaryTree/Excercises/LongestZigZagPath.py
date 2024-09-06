from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LongestZigZagSolution:
    def __init__(self, root: Optional[TreeNode]):
        self.root: Optional[TreeNode] = root

    def solve(self) -> int:
        max_zigzag_length = 0

        def dfs_zigzag(cur_node: Optional[TreeNode], cur_len: int, type_left: bool):
            nonlocal max_zigzag_length
            if cur_len > max_zigzag_length:
                max_zigzag_length = cur_len
            if not cur_node:
                return

            if type_left:
                dfs_zigzag(cur_node.right, cur_len + 1, False)
                dfs_zigzag(cur_node.left, 0, True)
            else:
                dfs_zigzag(cur_node.right, 0, False)
                dfs_zigzag(cur_node.left, cur_len+1, True)

        dfs_zigzag(self.root.left, 1, True)
        dfs_zigzag(self.root.right, 1, False)
        
        return max_zigzag_length
