from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DeleteBSTNodeSolution:
    def __init__(self, root: Optional[TreeNode], key: int):

        self.root: Optional[TreeNode] = root

        self.key: int = key

    def solve(self) -> Optional[TreeNode]:

        if not self.root:
            return None

        cur_n: Optional[TreeNode] = self.root
        par_n: Optional[TreeNode] = None
        is_left: bool = True
        while cur_n and cur_n.val != self.key:
            par_n = cur_n
            if cur_n.val < self.key:
                is_left = False
                cur_n = cur_n.right
            else:
                is_left = True
                cur_n = cur_n.left

        if not cur_n:
            return self.root

        selected_node: Optional[TreeNode] = cur_n
        left_n = selected_node.left
        if not left_n:
            if not par_n:
                self.root = selected_node.right
                del selected_node
                return self.root
            if is_left:
                par_n.left = selected_node.right
            else:
                par_n.right = selected_node.right
            del selected_node
            return self.root

        if not left_n.right:
            selected_node.val, left_n.val = left_n.val, selected_node.val
            selected_node.left = left_n.left
            del left_n
            return self.root

        # find successor of selected_node
        successor_n = left_n.right
        par_successor = left_n
        while successor_n.right:
            par_successor = successor_n
            successor_n = successor_n.right

        # swap values between selected node ( get value equal key) and successor node of the node
        selected_node.val, successor_n.val = successor_n.val, selected_node.val

        par_successor.right = successor_n.left
        del successor_n
        return self.root
