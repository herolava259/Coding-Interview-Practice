from typing import List, Optional


class TreeNode:
    def __init__(self, val: int, left_node: Optional['TreeNode'] = None, right_node: Optional['TreeNode'] = None):
        self.val: int = val
        self.left_node: Optional['TreeNode'] = left_node
        self.right_node: Optional['TreeNode'] = right_node



class BaseBinaryTree:
    def __init__(self, root: TreeNode | None = None):
        self.root: TreeNode = TreeNode(0) if root is None else root

    def make_tree_node(self, val: int = 0) -> TreeNode:

        return TreeNode(val)

    def count_node(self, cur_node: TreeNode | None) -> int:

        if cur_node is None:
            return 0

        return 1 + self.count_node(cur_node.left_node) + self.count_node(cur_node.right_node)

    def depth(self, cur_node: TreeNode | None) -> int:

        if not cur_node:
            return 0

        left_dept = self.depth(cur_node.left_node)
        right_dept = self.depth(cur_node.right_node)

        return max(left_dept, right_dept) + 1

    def preorder_traverse(self, cur_node: TreeNode):

        if cur_node is None:
            return

        print(cur_node.val)
        self.preorder_traverse(cur_node.left_node)
        self.preorder_traverse(cur_node.right_node)

    def inorder_traverse(self, cur_node: TreeNode):

        if cur_node is None:
            return

        self.inorder_traverse(cur_node.left_node)
        print(cur_node.val)
        self.inorder_traverse(cur_node.right_node)

    def postorder_traverse(self, cur_node: TreeNode):

        if cur_node is None:
            return

        self.postorder_traverse(cur_node.left_node)
        self.postorder_traverse(cur_node.right_node)
        print(cur_node.val)
