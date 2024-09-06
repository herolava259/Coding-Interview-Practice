from typing import List, Optional, Deque
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxLevelSumSolution:

    def __init__(self, root: Optional[TreeNode]):

        self.root: Optional[TreeNode] = root

    def solve(self):
        if not self.root:
            return 0

        q: Deque[tuple] = deque()

        cur_d, cur_node = 1, self.root
        cur_sum = self.root.val
        max_sum = cur_sum
        min_d = 1

        d = 1

        q.append((cur_d, cur_node))
        while q:

            cur_d, cur_node = q.popleft()

            if cur_d > d:
                if cur_sum > max_sum:
                    min_d = d
                    max_sum = cur_sum
                d = cur_d
                cur_sum = cur_node.val
            else:
                cur_sum += cur_node.val

            if not cur_node.left:
                q.append((cur_d + 1, cur_node.left))
            if not cur_node.right:
                q.append((cur_d + 1, cur_node.right))
        if cur_sum > max_sum:
            min_d = d
        return min_d
