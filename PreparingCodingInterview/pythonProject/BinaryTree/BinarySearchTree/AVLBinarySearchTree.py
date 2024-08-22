from typing import Optional


class TreeNode:
    def __init__(self, key: int, h: int = 1, bal: int = 0, left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None, parent: Optional['TreeNode'] = None):
        self.key: int = key
        self.h: int = h
        self.bal: int = bal
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right
        self.parent: TreeNode | None = parent


class AVLBinarySearchTree:
    def __init__(self):
        self.root: TreeNode | None = None

    def is_balance(self, root: TreeNode | None):
        if root is None:
            return True

        if not self.is_balance(root.left):
            return False
        if not self.is_balance(root.right):
            return False

        left_h = root.left.h if root.left else 0
        right_h = root.right.h if root.right else 0

        return -1 <= left_h - right_h <= 1

    def height_of_node(self, root_node: TreeNode | None) -> int:
        if not root_node:
            return 0

        return 1 + max(self.height_of_node(root_node.left), self.height_of_node(root_node.right))

    def revise_balance(self, root: TreeNode | None):

        if root is None:
            return

        root.h = self.height_of_node(root)

        if root.h < 2:
            return

        def get_situation_non_balance():

            left_h = root.left.h if root.left else 0
            right_h = root.right.h if root.right else 0

            left_c, right_c = root.left, root.right
            if -1 <= left_h - right_h <= 1:
                return -1

            ll_h, lr_h, rl_h, rr_h = 0, 0, 0, 0

            if left_h > 0:
                ll_h = left_c.left.h if left_c.left else 0
                lr_h = left_c.right.h if left_c.right else 0

            if right_h > 0:
                rl_h = right_c.left.h if right_c.left else 0
                rr_h = right_c.h if right_c.right else 0

            if ll_h > right_h + 1:
                return 1
            elif rr_h > left_h + 1:
                return 2
            elif lr_h > right_h + 1:
                return 3
            elif rl_h > left_h + 1:
                return 4

            return -1

        def right_rotation(root_node) -> TreeNode:

            left_node, right_node = root_node.left, root_node.right
            ll_node, lr_node = left_node.left, left_node.right

            root_node.left = lr_node
            root_node.h -= 1

            left_node.left, left_node.right = ll_node, root_node

            return left_node

        def left_rotation(root_node: TreeNode) -> TreeNode:
            left_node, right_node = root_node.left, root_node.right
            rl_node, rr_node = right_node.left, right_node.right

            root_node.right = rl_node
            root_node.h -= 1

            right_node.left = root_node

            return right_node

        situation = get_situation_non_balance()
        new_root = root
        parent = root.parent
        if situation == -1:
            return
        elif situation == 1:
            new_root = right_rotation(root)
        elif situation == 2:
            new_root = left_rotation(root)
        elif situation == 3:
            root.left = left_rotation(root.left)
            new_root = right_rotation(root)
        elif situation == 4:
            root.right = right_rotation(root.right)
            new_root = left_rotation(root)
        if parent.left == root:
            parent.left = new_root
        elif parent.right == root:
            parent.right = new_root

        self.revise_balance(parent)
