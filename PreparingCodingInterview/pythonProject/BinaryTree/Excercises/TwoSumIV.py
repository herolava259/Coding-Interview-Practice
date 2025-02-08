from typing import List, Optional, DefaultDict, Set
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class UpClimbNode:
    def __init__(self, val: int=0, left: Optional['UpClimbNode'] = None, right: Optional['UpClimbNode'] = None
                 , par: Optional['UpClimbNode'] = None):

        self.val = val
        self.left = left
        self.right = right
        self.par = par

def flatten(r: Optional[TreeNode])-> List[int]:
    if not r:
        return []

    left_partition: List[int] = flatten(r.left)
    right_partition: List[int] = flatten(r.right)

    return left_partition + [r.val] + right_partition

class TwoSumIVSolution:
    def __init__(self, root: Optional[TreeNode], k: int):
        self.root: Optional[TreeNode] = root
        self.k: int = k

    def hash_map_solve(self) -> bool:

        mark_tb: DefaultDict[int, bool] = defaultdict(bool)
        val_set: Set[int] = set()
        def dfs_mark(r: Optional[TreeNode]) -> bool:
            if not r:
                return False
            mark_tb[r.val] = True
            val_set.add(r.val)
            dfs_mark(r.left)
            dfs_mark(r.right)
            return True

        dfs_mark(self.root)

        for n_val in val_set:
            if mark_tb[self.k-n_val]:
                return True

        return False


    def flatten_tree_solve(self) -> bool:

        def bs_exist(arr: List[int], beg: int, search_val: int) -> bool:

            low, high = beg, len(arr) - 1

            while low < high:
                mid = (low + high) >> 1

                if arr[mid] == search_val:
                    return True
                elif arr[mid] < search_val:
                    low = mid+1
                else:
                    high = mid - 1

            return False

        sorted_arr: List[int] = flatten(self.root)

        for i in range(len(sorted_arr)-1):

            val_less = sorted_arr[i]
            if bs_exist(sorted_arr, i+1, self.k - val_less):
                return True

        return False
    def simple_two_pointer_solve(self):

        arr = flatten(self.root)

        left, right = 0, len(arr) -1

        while left < right:

            obs_v = arr[left] + arr[right]

            if obs_v == self.k:
                return True
            elif obs_v < self.k:
                left += 1
            else:
                right -= 1
        return False

    def complex_two_pointer_solve(self) -> bool:

        def convert(u: Optional[TreeNode], par: Optional[UpClimbNode] = None) -> Optional[UpClimbNode]:

            if not u:
                return None

            climb_u = UpClimbNode(u.val, None, None, par)

            climb_u.left = convert(u.left, climb_u)
            climb_u.right = convert(u.right, climb_u)

            return climb_u

        up_r: Optional[UpClimbNode] = convert(self.root)
        if not up_r:
            return False

        left_n = up_r

        while left_n.left:
            left_n = left_n.left

        right_n = up_r

        while right_n.right:
            right_n = right_n.right

        def step_forward(r: UpClimbNode) -> Optional[UpClimbNode]:

            if r.right:
                right_most = r.right
                while right_most.left:
                    right_most = right_most.left
                return right_most

            more_n = r

            while more_n.par and more_n.par.val < r.val:
                more_n = more_n.par

            return more_n

        def step_backward(r: UpClimbNode) -> Optional[UpClimbNode]:

            if r.left:
                left_most = r.left

                while left_most.right:
                    left_most = left_most.right

                return left_most
            less_n = r

            while less_n.par and less_n.par.val > r.val:
                less_n = less_n.par

            return less_n


        while left_n and right_n and left_n != right_n:

            obs_val = left_n.val + right_n.val

            if obs_val == self.k:
                return True
            elif obs_val < self.k:
                left_n = step_forward(left_n)
            else:
                right_n = step_backward(right_n)

        return False




