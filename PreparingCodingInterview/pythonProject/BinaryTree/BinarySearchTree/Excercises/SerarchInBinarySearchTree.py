from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search_tree(cur_node: Optional[TreeNode], val) -> Optional[TreeNode]:

            if not cur_node:
                return None

            if cur_node.val == val:
                return cur_node
            elif cur_node.val > val:
                return search_tree(cur_node.left, val)
            else:
                return search_tree(cur_node.right, val)

        return search_tree(root, val)
