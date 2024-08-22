from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val: int = val
        self.left: Optional['TreeNode'] = left
        self.right: Optional['TreeNode'] = right


class SumRootToLeafSolution:
    def __init__(self, root: Optional[TreeNode]):
        self.root: TreeNode | None = root
        self.sums = 0

    def solve(self) -> int:
        if not self.root:
            return 0

        self.dfs_count(0, self.root)

        return self.sums

    def dfs_count(self, num: int, cur_node: Optional[TreeNode]):

        num = num * 10 + cur_node.val
        if cur_node.left is None and cur_node.right is None:
            self.sums += num

        if cur_node.left:
            self.dfs_count(num, cur_node.left)
        if cur_node.right:
            self.dfs_count(num, cur_node.right)
