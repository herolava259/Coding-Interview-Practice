from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class UniqueTreesGenerator:
    def __init__(self, n: int):
        self.n: int = n

    def solve(self) -> List[Optional[TreeNode]]:

        def generate_tree(low: int, high: int) -> List[TreeNode]:

            if low == high:
                return [TreeNode(low)]
            roots: List[TreeNode] = []

            right_child_roots: List[TreeNode] = generate_tree(low + 1, high)
            for righ_child in right_child_roots:
                roots.append(TreeNode(low, None, righ_child))
            left_child_roots: List[TreeNode] = generate_tree(low, high - 1)

            for left_child in left_child_roots:
                roots.append(TreeNode(high, left_child, None))

            for root_val in range(low + 1, high):

                left_child_roots: List[TreeNode] = generate_tree(low, root_val - 1)

                right_child_roots: List[TreeNode] = generate_tree(root_val + 1, high)

                for left_child in left_child_roots:
                    for right_child in right_child_roots:
                        roots.append(TreeNode(root_val, left_child, right_child))

            return roots

        return generate_tree(1, self.n)


n1 = 5
sln = UniqueTreesGenerator(n1)

print(sln.solve())