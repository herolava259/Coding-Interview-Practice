from typing import List, Deque as Queue, Tuple
from collections import deque as queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_values_in_depth_k(root_node: TreeNode, exclusive_node: TreeNode | None, k: int) -> List[int]:
    if k == 0:
        return [root_node.val]
    q: Queue[Tuple[int, TreeNode]] = queue()
    if root_node.left and root_node.left != exclusive_node:
        q.append((1, root_node.left))
    if root_node.right and root_node.right != exclusive_node:
        q.append((1, root_node.right))

    while q and q[0][0] < k:
        depth, cur_node = q.popleft()

        if cur_node.left:
            q.append((depth + 1, cur_node.left))
        if cur_node.right:
            q.append((depth + 1, cur_node.right))

    return [item[1].val for item in q]


class DistanceKSolution:
    def __init__(self, root: TreeNode, target: TreeNode, k: int):

        self.root: TreeNode = root
        self.target: TreeNode = target
        self.k: int = k

    def find_ancestor_nodes_of_target(self) -> List[TreeNode]:
        def dfs_find(cur_n: TreeNode | None) -> List[TreeNode] | None:
            if not cur_n:
                return None

            if cur_n == self.target:
                return [self.target]

            left_lst = dfs_find(cur_n.left)

            if left_lst:
                left_lst.append(cur_n)
                return left_lst

            right_lst = dfs_find(cur_n.right)

            if right_lst:
                right_lst.append(cur_n)
                return right_lst
            return None

        return dfs_find(self.root)

    def solve(self) -> List[int]:

        ancestor = self.find_ancestor_nodes_of_target()

        cur_k = self.k
        n = len(ancestor)
        i = 0
        results: List[int] = []
        exclusive_node = None
        while i < n and cur_k >= 0:
            results.extend(find_values_in_depth_k(ancestor[i], exclusive_node, cur_k))
            exclusive_node = ancestor[i]
            cur_k -= 1
            i += 1

        return results


