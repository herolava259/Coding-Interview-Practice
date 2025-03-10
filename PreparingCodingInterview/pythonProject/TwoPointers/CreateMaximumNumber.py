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
    def __init__(self, ):
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

        def evaluate(arr1: List[int], arr2: List[int]) -> bool:
            for idx in range(self.k):
                if arr1[idx] > arr2[idx]:
                    return True
                elif arr1[idx] < arr2[idx]:
                    return False
            return True



        max_arr: List[int] = [0] * self.k

        for i in range(self.k+1):
            k1, k2 = i, self.k-i
            if k1 > len(self.nums1) or k2 > len(self.nums2):
                continue
            cd_arr1 = max_sub_k_length_arr(self.nums1, k1)
            cd_arr2 = max_sub_k_length_arr(self.nums2, k2)
            cd_arr = schrodinger_merge(cd_arr1, cd_arr2)
            if not evaluate(max_arr, cd_arr):
                max_arr = cd_arr


        return max_arr


nums11 = [2,1,2,1,2,2,1,2,2,1,1,2,1,0,2,0,1,0,1,1,2,0,0,2,2,2,2,1,1,1,2,1,2,0,2,0,1,1,0,1,0,2,0,1,0,2,0,1,1,0,0,2,0,1,1,2,0,2,2,1,2,1,2,1,0,1,2,0,2,1,2,2,2,0,1,1,0,2,0,1,1,0,0,0,2,1,1,1,0,1,1,0,1,2,1,2,0,0,0,2,1,2,2,1,1,0,1,1,0,0,1,0,0,0,2,1,1,0,2,0,2,2,0,2,0,0,2,0,1,2,1,1,1,2,1,0,1,1,0,2,1,2,2,1,0,1,1,1,2,0,2,2,2,0,2,1,1,2,1,1,2,0,2,1,0,2,0,0,2,2,2,0,2,1,2,2,1,2,1,2,2,2,1,1,2,0,2,0,0,2,2,2,0,2,2,1,0,0,2,2,2,1,1,0,2,1,0,1,2,1,1,2,2,1,1,0,2,1,2,2,1,2,1,0,0,0,0,1,1,0,2,2,2,2,2,2,2,2,1,1,0,2,1,0,0,0,0,2,1,1]
nums21 = [1,1,0,2,0,1,1,1,0,2,2,2,1,1,0,1,2,1,2,1,0,1,2,2,2,2,1,1,0,2,0,1,0,0,1,1,0,1,2,1,2,1,2,0,1,1,1,1,2,0,1,1,1,0,0,1,0,1,2,1,1,0,2,2,1,2,0,2,0,1,1,2,0,1,1,2,2,1,0,1,2,2,0,1,1,2,2,0,2,2,0,2,1,0,0,2,1,0,0,2,1,2,1,2,0,2,0,1,1,2,1,1,1,2,0,2,2,0,2,2,0,2,1,2,1,2,0,2,0,0,1,2,2,2,2,1,2,2,0,1,0,0,2,2,2,2,0,1,0,2,1,2,2,2,1,1,1,1,2,0,0,1,0,0,2,2,1,0,0,1,1,0,0,1,1,0,2,2,2,2,2,1,0,2,2,0,0,1,0,0,1,1,1,2,2,0,0,2,0,0,0,1,2,0,2,0,1,2,0,1,2,0,1,1,0,0,1,2,1,0,2,1,0,1,2,0,1,1,2,1,0,2,1,2,1,1,0,2,2,1,0,2,1,1,1,0,0,0,1,0]

k11 = 500


def max_sub_k_length_arr(arr: List[int], k: int) -> List[int]:
    if k <= 0:
        return []
    low, high = 0, len(arr) - k
    results: List[int] = [0] * k

    st: SegmentTree = SegmentTree()
    st.initialize(arr)

    for idx in range(k):
        found_idx = st.easy_get(low, high)
        results[idx] = arr[found_idx]
        low = found_idx + 1
        high += 1
    return results


def compare(digits1: List[int], digits2: List[int]) -> bool:

    for val1, val2 in zip(digits1, digits2):
        if val1 > val2:
            return True
        elif val1 < val2:
            return False
    return True

def recursive_merge(arr1: List[int], arr2: List[int]) -> List[int]:


    if not arr1:
        return arr2
    if not arr2:
        return arr1

    if arr1[0] < arr2[0]:
        arr1, arr2 = arr2, arr1

    if arr1[0] != arr2[0]:
        return [arr1[0]] + recursive_merge(arr1[1:], arr2)

    val = arr1[0]
    merged_arr1: List[int] = recursive_merge(arr1[1:], arr2)
    merged_arr2: List[int] = recursive_merge(arr1, arr2[1:])

    return [val] + (merged_arr1 if compare(merged_arr1, merged_arr2) else merged_arr2)

def dp_merge(arr1: List[int], arr2: List[int]) -> List[int]:
    m, n = len(arr1), len(arr2)
    dp: List[List[List[int] | None]] = [[None for _ in range(n+1)] for _ in range(m + 1)]
    dp[m][n] = []

    for i in range(m):
        dp[i][n] = arr1[i:]
    for i in range(n):
        dp[m][i] = arr2[i:]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if arr1[i] > arr2[j]:
                dp[i][j] = [arr1[i]] + dp[i+1][j]
            elif arr1[i] < arr2[j]:
                dp[i][j] = [arr2[j]] + dp[i][j+1]
            else:
                cd_arr1 = [arr1[i]] + dp[i+1][j]
                cd_arr2 = [arr2[j]] + dp[i][j+1]
                dp[i][j] = cd_arr1 if compare(cd_arr1, cd_arr2) else cd_arr1

    return dp[0][0]

def save_memory_dp_merge(arr1: List[int], arr2: List[int]) -> List[int]:
    m, n = len(arr1), len(arr2)
    prev_dp: List[List[int]] = [arr2[i:] for i in range(n+1)]


    for i in range(m-1, -1, -1):
        dp: List[List[int] | None] = [None for i in range(n+1)]
        dp[n] = arr1[i:]
        for j in range(n-1, -1, -1):
            if arr1[i] > arr2[j]:
                dp[j] = [arr1[i]] + prev_dp[j]
            elif arr1[i] < arr2[j]:
                dp[j] = [arr2[j]] + dp[j+1]
            else:
                cd_arr1 = [arr1[i]] + prev_dp[j]
                cd_arr2 = [arr2[j]] + dp[j+1]
                dp[j] = cd_arr1 if compare(cd_arr1, cd_arr2) else cd_arr1

        del prev_dp
        prev_dp = dp

    return prev_dp[0]

def schrodinger_merge(arr1: List[int], arr2: List[int]) -> List[int]:
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    results: List[int] = []
    uncertainty_q: Deque[Tuple[int, int, int]] = deque()
    p1, p2 = 0, 0

    def greater(low1: int, high1: int, low2: int, high2: int) -> int:
        while low1 < high1 and low2 < high2:
            if arr1[low1] > arr2[low2]:
                return 1
            elif arr1[low1] < arr2[low2]:
                return -1
            low1 += 1
            low2 += 1


        if low1 < high1:
            return 1
        elif low2 < high2:
            return -1
        return 0

    def equal(low1: int, low2: int) -> int:
        p_1, p_2 = low1, low2

        if low2 >= len(arr2):
            return 1
        if low1 >= len(arr1):
            return -1

        while p_1 < len(arr1) and p_2 < len(arr2) :
            if arr1[p_1] > arr2[p_2]:
                return 1
            elif arr1[p_1] < arr2[p_2]:
                return -1
            p_1 += 1
            p_2 += 1
        if p_1 < len(arr1):
            return equal(p_1, low2)
        elif p_2 < len(arr2):
            return equal(low1, p_2)
        return 1


    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] > arr2[p2]:
            results.append(arr1[p1])
            p1+=1
            continue
        if arr2[p2] > arr1[p1]:
            results.append(arr2[p2])
            p2 += 1
            continue

        val = arr2[p2]
        results.append(val)

        nxt_p1 = p1 + 1
        nxt_p2 = p2 + 1

        while nxt_p1 < len(arr1) and arr1[nxt_p1] >= val:
            nxt_p1 += 1
        while nxt_p2 < len(arr2) and arr2[nxt_p2] >= val:
            nxt_p2 += 1

        state: int = greater(p1+1, nxt_p1, p2+1, nxt_p2)

        if state == 0:
            state = equal(nxt_p1, nxt_p2)

        if state == 1:
            p1 += 1
        else:
           p2 += 1

    if p1 < len(arr1):
        p1 = max(uncertainty_q[-1][0] + 1 if uncertainty_q else p1, p1)
        results.extend(schrodinger_merge(arr1[p1:], [t[-1] for t in uncertainty_q]))
    else:
        p2 = max(uncertainty_q[-1][1] + 1 if uncertainty_q else p2, p2)
        results.extend(schrodinger_merge(arr2[p2:], [t[-1] for t in uncertainty_q]))

    return results
# print(len(nums21))
# print(len(nums11))
# res1 = find_k_len_arr(nums11, 250)
# res2 = find_k_len_arr(nums21, 250)
# print(res1)
# print(res2)
# print(schrodinger_merge(res1, res2))

print(schrodinger_merge([5,0,2,1,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3], [7,6,7,1,0,1,0,5,6,0,5,0]))

sln = CreateMaximumNumberSolution(nums11, nums21, k11)

print(sln.naive_solve())
