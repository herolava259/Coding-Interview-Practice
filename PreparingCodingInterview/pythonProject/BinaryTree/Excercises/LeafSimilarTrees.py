from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LeafSimilarSolution:
    def __init__(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        self.root1: Optional[TreeNode] = root1
        self.root2: Optional[TreeNode] = root2

    def solve(self) -> bool:

        if (not self.root1 and self.root2) or (self.root1 and not self.root2):
            return False

        val_leaf_1: List[int] = []

        def retrieve_leaf_val1(cur_node: Optional[TreeNode]) -> None:
            if not cur_node:
                return
            if not cur_node.left and not cur_node.right:
                val_leaf_1.append(cur_node.val)
                return

            retrieve_leaf_val1(cur_node.left)
            retrieve_leaf_val1(cur_node.right)

        retrieve_leaf_val1(self.root1)

        def check_sequences_tree2(cur_node: Optional[TreeNode]) -> bool:

            if not cur_node:
                return True

            if not cur_node.left and not cur_node.right:

                if not val_leaf_1 or cur_node.val != val_leaf_1.pop(0):
                    return False
                return True

            if not check_sequences_tree2(cur_node.left):
                return False

            return check_sequences_tree2(cur_node.right)

        if not check_sequences_tree2(self.root2):
            return False

        return not val_leaf_1
