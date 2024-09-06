from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PathSumIIISolution:
    def __init__(self, root: Optional[TreeNode], target_sum: int):

        self.root: Optional[TreeNode] = root
        self.target_sum: int = target_sum

    def solve(self) -> int:

        if not self.root:
            return 0
        num_path_sum = 0
        nodes: List[TreeNode] = []

        def dfs_traverse(cur_node: Optional[TreeNode]):
            if not cur_node:
                return
            nodes.append(cur_node)
            dfs_traverse(cur_node.left)
            dfs_traverse(cur_node.right)

        dfs_traverse(self.root)

        def path_sum(cur_node: Optional[TreeNode], cur_sum=0) -> int:
            if not cur_node:
                return 0
            num_path = 0
            if cur_sum + cur_node.val == self.target_sum:
                num_path += 1
            num_path += path_sum(cur_node.left, cur_sum + cur_node.val)
            num_path += path_sum(cur_node.right, cur_sum + cur_node.val)
            return num_path

        for cur_n in nodes:
            num_path_sum += path_sum(cur_n)

        return num_path_sum
