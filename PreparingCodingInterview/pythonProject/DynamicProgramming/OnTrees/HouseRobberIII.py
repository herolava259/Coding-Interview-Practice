from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HouseRobberIIISolution:
    def __init__(self, root: Optional[TreeNode]):
        self.root: Optional[TreeNode] = root

    def solve(self) -> int:
        def find_total_max(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root:
                return 0, 0

            without_right, has_right = find_total_max(root.right)
            without_left, has_left = find_total_max(root.left)

            return max(has_right, without_right)+max(has_left, without_left), without_right + without_left + root.val

        return max(*find_total_max(self.root))


