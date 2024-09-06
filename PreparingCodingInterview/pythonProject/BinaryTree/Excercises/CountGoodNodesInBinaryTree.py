from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CountGoodNodesSolution:
    def __init__(self, root: TreeNode):

        self.root: Optional[TreeNode] = root

    def solve(self) -> int:
        if not self.root:
            return 0

        def count_good_node(cur_node: Optional[TreeNode], max_path_val=-(10 ** 4) - 1):
            if not cur_node:
                return 0
            if cur_node.val < max_path_val:
                return count_good_node(cur_node.left, max_path_val) + count_good_node(cur_node.right, max_path_val)

            return 1 + count_good_node(cur_node.left, cur_node.val) + count_good_node(cur_node.right, cur_node.val)

        return count_good_node(self.root)
