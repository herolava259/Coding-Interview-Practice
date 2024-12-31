from typing import List
from collections import Counter


class TriangleNumberSolution:
    def __init__(self, nums: List[int]):

        self.nums: List[int] = nums

    def solve(self) -> int:

        frequencies = Counter(self.nums)

        sorted_keys: List[int] = sorted(frequencies.keys())

        n = len(sorted_keys)

        acc_totals: List[int] = [0] * (n+1)

        acc_totals[0] = frequencies[sorted_keys[0]]

        for i in range(1, n):
            acc_totals[i] = acc_totals[i] + acc_totals[i+1]

        def bs_search(val: int, beg: int = 0) -> int:

            low, high = beg, n-1

            while low < high:
                mid = ((low+high) >> 1) + ((low+high) & 1)

                if sorted_keys[mid] >= val:
                    high = mid - 1
                else:
                    low = mid

            return low

        num_triangle = 0

        for i in range(n):
            for j in range(i, n):

                side_i, side_j = sorted_keys[i], sorted_keys[j]
                if side_i == side_j and frequencies[side_i] == 1:
                    continue

                idx = bs_search(side_i + side_j, j)

                mul = 0

                if side_i == side_j:
                    mul = (frequencies[side_i] * (frequencies[side_i]-1)) // 2
                else:
                    mul = frequencies[side_i] * frequencies[side_j]

                num_force = acc_totals[idx] - acc_totals[side_j]
                if idx == j:
                    num_force = frequencies[side_j] - 1

                    if side_i == side_j:
                        num_force -= 1

                num_triangle += mul * num_force
        return num_triangle

    def hash_table_solve(self) -> int:

        frequencies = Counter(self.nums)

        sorted_keys = sorted(frequencies.keys())

        n = len(sorted_keys)

        acc_total_sides: List[int] = [0 for _ in range(1001)]

        acc_total_sides[0] = frequencies.get(1, 0)
        for i in range(2, 1001):

            acc_total_sides[i] = acc_total_sides[i-1] + frequencies.get(i, 0)

        num_triangle = 0

        for i in range(n):
            for j in range(i, n):

                side_i, side_j = sorted_keys[i], sorted_keys[j]
                if side_i == 0 or side_j == 0:
                    continue
                if side_i == side_j and frequencies[side_i] == 1:
                    continue

                mul = 0

                if side_i == side_j:
                    mul = (frequencies[side_i] * (frequencies[side_i]-1)) // 2
                else:
                    mul = frequencies[side_i] * frequencies[side_j]

                num_triangle += mul * (acc_total_sides[side_i+side_j-1]-2)

        return num_triangle

    def two_pointer_solve(self) -> int:

        sorted_arr = sorted(self.nums)
        n = len(sorted_arr)
        num_triangle = 0
        for i in range(1, n-1):

            left, right = 0, i+1

            while left < i and right < n:
                total_two = sorted_arr[left] + sorted_arr[i]

                if total_two <= sorted_arr[right]:
                    left += 1
                else:
                    num_triangle += i-left
                    right += 1

        return num_triangle


nums1 = [4, 2, 3, 4]
sln = TriangleNumberSolution(nums1)

print(sln.two_pointer_solve())





        
