from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InorderTraversalSolution:

    def __init__(self, root: Optional[TreeNode]):
        self.root: Optional[TreeNode] = root

    def solve(self) -> List[int]:
        result: List[int] = []

        def dfs_search(cur_node: Optional[TreeNode]):
            if not cur_node:
                return

            dfs_search(cur_node.left)
            result.append(cur_node.val)
            dfs_search(cur_node.right)

        dfs_search(self.root)

        return result

