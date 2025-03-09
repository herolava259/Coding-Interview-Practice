from typing import List, Deque, Tuple
from collections import deque


error_result = [9,9,9,9,9,9,9,2,7,5,4,3,0,0,1,7,1,8,1,5,2,5,7,0,4,3,8,7,3,8,5,3,8,3,4,0,2,3,8,2,7,1,2,3,8,7,6,7,1,1,3,9,0,5,2,8,2,8,7,5,0,8,0,7,2,8,5,6,5,9,5,1,5,2,6,2,4,9,9,7,6,5,7,9,2,8,8,3,5,9,5,1,8,8,4,6,6,3,8,4,6,6,1,3,4,1,6,7,0,8,0,3,3,1,8,2,2,4,5,7,3,7,7,4,3,7,3,0,7,3,0,9,7,6,0,3,0,3,1,5,1,4,5,2,7,6,2,4,2,9,5,5,9,8,4,2,3,6,1,9]
def arg_max(arr: List[int], idx1: int, idx2: int) -> int:

    if idx1 == -1 and idx2 == -1:
        return -1

    if idx1 == -1:
        return idx2
    if idx2 == -1:
        return idx1
    return idx1 if arr[idx1] >= arr[idx2] else idx2

class SegmentTree:
    def __init__(self):
        self.nums: List[int] = []
        self.arr: List[int] = []
        self.size: int = 0

        self.arg_max = lambda idx1,idx2: arg_max(self.nums, idx1, idx2)

    def initialize(self, nums: List[int]):
        self.size = len(nums)
        self.arr = [0] * (4 * self.size + 1)
        self.nums = nums


        def build(idx: int, l: int, r: int):

            if l >= r:
                self.arr[idx] = l
                return

            mid = (l+r) >> 1

            left_idx = idx << 1
            right_idx = left_idx + 1

            build(left_idx, l, mid)
            build(right_idx, mid+1, r)

            self.arr[idx] = self.arg_max(self.arr[left_idx], self.arr[right_idx])

        build(1, 0, self.size-1)

    def get(self,u: int, v: int,idx: int = 1, l: int = 0, r: int=0)-> int:

        if v < l or u > r:
            return -1

        if u <= l <= r <= v:
            return self.arr[idx]

        left_idx = idx << 1
        right_idx = left_idx + 1

        mid = (l+r) >> 1

        return self.arg_max(self.get(u, v, left_idx, l, mid), self.get(u, v, right_idx, mid+1, r))

    def easy_get(self, u: int, v: int) -> int:
        return self.get(u, v, 1, 0, self.size-1)


class CreateMaximumNumberSolution:
    def __init__(self, nums1: List[int], nums2: List[int], k: int):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        self.nums1: List[int] = nums1
        self.nums2: List[int] = nums2
        self.k: int = k

    def naive_solve(self) -> List[int]:

        def find_k_len_arr(arr: List[int], k: int) -> List[int]:

            low, high = 0, len(arr)-k
            results: List[int] = [0] * k

            st: SegmentTree = SegmentTree()
            st.initialize(arr)

            for idx in range(k):
                found_idx = st.easy_get(low, high)

                results[idx] = arr[found_idx]
                low = found_idx + 1
                high += 1
            return results

        def schrodinger_merge(arr1: List[int], arr2: List[int]) -> List[int]:

            if not arr1:
                return arr2
            if not arr2:
                return arr1

            results: List[int] = []
            uncertainty_q: Deque[Tuple[int, int, int]] = deque()
            arr: Tuple[List[int], List[int]] = (arr1, arr2)
            p: List[int] = [0, 0]

            while p[0] < len(arr[0]) and p[1] < len(arr[1]):
                val: List[int] = [arr[0][p[0]], arr[1][p[1]]]
                idx0, idx1 = 0, 1
                if val[1] > val[0]:
                    idx0, idx1 = 1, 0

                if val[1] == val[0]:
                    # while uncertainty_q and uncertainty_q[0][-1] >= val[0]:
                    #     results.append(uncertainty_q.popleft()[-1])

                    uncertainty_q.append((p[0], p[1],val[0]))
                    results.append(val[1])
                    p[0] += 1
                    p[1] += 1
                    continue

                while uncertainty_q and uncertainty_q[0][-1] > val[idx0]:
                    results.append(uncertainty_q.popleft()[-1])

                if uncertainty_q:
                    p[idx1] = uncertainty_q[0][idx1]
                uncertainty_q.clear()

                if arr[0][p[0]] == arr[1][p[1]]:
                    uncertainty_q.append((p[0], p[1], arr[0][p[0]]))
                    p[idx1] += 1
                results.append(val[idx0])
                p[idx0] += 1

            if p[0] < len(arr[0]):
                results.extend(schrodinger_merge(arr[0][p[0]:], [t[-1] for t in uncertainty_q]))
            else:
                results.extend(schrodinger_merge(arr[1][p[1]:], [t[-1] for t in uncertainty_q]))

            return results

        def evaluate(arr1: List[int], arr2: List[int]) -> bool:
            for idx in range(self.k):
                if arr1[idx] > arr2[idx]:
                    return True
                elif arr1[idx] < arr2[idx]:
                    return False

            return True
        max_arr: List[int] = [0] * self.k

        def compare(arr1, arr2):
            for val1, val2 in zip(arr1, arr2):
                if val1 != val2:
                    return False
            return True
        for i in range(self.k+1):
            k1, k2 = i, self.k-1
            if k1 > len(self.nums1) or k2 > len(self.nums2):
                continue
            cd_arr1 = find_k_len_arr(self.nums1, k1)
            cd_arr2 = find_k_len_arr(self.nums2, k2)
            cd_arr = schrodinger_merge(cd_arr1, cd_arr2)
            if not evaluate(max_arr, cd_arr):
                max_arr = cd_arr
            if compare(cd_arr, error_result):
                print(cd_arr1)
                print(cd_arr2)

        return max_arr


nums11 = [3,3,3,2,3,7,3,8,6,0,5,0,7,8,9,2,9,6,6,9,9,7,9,7,6,1,7,2,7,5,5,1]
nums21 = [5,6,4,9,6,9,2,2,7,5,4,3,0,0,1,7,1,8,1,5,2,5,7,0,4,3,8,7,3,8,5,3,8,3,4,0,2,3,8,2,7,1,2,3,8,7,6,7,1,1,3,9,0,5,2,8,2,8,7,5,0,8,0,7,2,8,5,6,5,9,5,1,5,2,6,2,4,9,9,7,6,5,7,9,2,8,8,3,5,9,5,1,8,8,4,6,6,3,8,4,6,6,1,3,4,1,6,7,0,8,0,3,3,1,8,2,2,4,5,7,3,7,7,4,3,7,3,0,7,3,0,9,7,6,0,3,0,3,1,5,1,4,5,2,7,6,2,4,2,9,5,5,9,8,4,2,3,6,1,9]

k11 = 160


# def find_k_len_arr(arr: List[int], k: int) -> List[int]:
#     low, high = 0, len(arr) - k
#     results: List[int] = [0] * k
#
#     st: SegmentTree = SegmentTree()
#     st.initialize(arr)
#
#     for idx in range(k):
#         found_idx = st.easy_get(low, high)
#
#         results[idx] = arr[found_idx]
#         low = found_idx + 1
#         high += 1
#     return results
#
#
#
#
# def schrodinger_merge(arr1: List[int], arr2: List[int]) -> List[int]:
#     if not arr1:
#         return arr2
#     if not arr2:
#         return arr1
#
#     results: List[int] = []
#     uncertainty_q: Deque[Tuple[int, int, int]] = deque()
#     arr: Tuple[List[int], List[int]] = (arr1, arr2)
#     p: List[int] = [0, 0]
#
#     while p[0] < len(arr[0]) and p[1] < len(arr[1]):
#         val: List[int] = [arr[0][p[0]], arr[1][p[1]]]
#         idx0, idx1 = 0, 1
#         if val[idx1] > val[idx0]:
#             idx0, idx1 = 1, 0
#
#         if val[1] == val[0]:
#             # while uncertainty_q and uncertainty_q[0][-1] >= val[0]:
#             #     results.append(uncertainty_q.popleft()[-1])
#
#             uncertainty_q.append((p[0], p[1], val[0]))
#             results.append(val[1])
#             p[0] += 1
#             p[1] += 1
#             continue
#
#         while uncertainty_q and uncertainty_q[0][-1] > val[idx0]:
#             results.append(uncertainty_q.popleft()[-1])
#
#         if uncertainty_q:
#             p[idx1] = uncertainty_q[0][idx1]
#         uncertainty_q.clear()
#
#         if arr[0][p[0]] == arr[1][p[1]]:
#             uncertainty_q.append((p[0], p[1], arr[0][p[0]]))
#             p[idx1] += 1
#         results.append(val[idx0])
#         p[idx0] += 1
#
#     if p[0] < len(arr[0]):
#         results.extend(schrodinger_merge(arr[0][p[0]:], [t[-1] for t in uncertainty_q]))
#     else:
#         results.extend(schrodinger_merge(arr[1][p[1]:], [t[-1] for t in uncertainty_q]))
#
#     return results

# res1 = find_k_len_arr(nums11, 80)
# res2 = find_k_len_arr(nums21, 120)
# print(res1)
# print(res2)
# print(schrodinger_merge(res1, res2))


sln = CreateMaximumNumberSolution(nums11, nums21, k11)

print(sln.naive_solve())
