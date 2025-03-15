from typing import List, Deque as Stack, Optional
from collections import deque as stack

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ConstructMaximumBinaryTreeSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> Optional[TreeNode]:

        if not self.nums:
            return None
        st: Stack[TreeNode] = stack()

        st.append(TreeNode(self.nums[0]))


        for i in range(1, len(self.nums)):

            new_node = TreeNode(self.nums[i])
            left_node: TreeNode | None = None
            while st and st[-1].val < new_node.val:
                left_node = st.pop()

            if st:
                st[-1].right = new_node
            new_node.left = left_node
            st.append(new_node)

        return st[0]
