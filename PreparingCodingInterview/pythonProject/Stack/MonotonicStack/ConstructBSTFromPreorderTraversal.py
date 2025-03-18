from typing import List, Optional,  Deque as Stack
from collections import deque as stack


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTFromPreorderSolution:
    def __init__(self, preorder: List[int]):

        self.preorder: List[int] = preorder

    def solve(self) -> Optional[TreeNode]:

        if not self.preorder:
            return None

        st: Stack[TreeNode] = stack()
        root_node = TreeNode(self.preorder[0])
        st.append(root_node)
        for num in self.preorder[1:]:
            new_node = TreeNode(num)
            if not st:
                st.append(new_node)
                continue

            if st and st[-1].val > num:
                st[-1].left = new_node
                st.append(new_node)
                continue
            par_node = st[-1]
            while st and st[-1].val < num:
                par_node = st.pop()
            par_node.right = new_node
            st.append(new_node)

        return root_node
