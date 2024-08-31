from typing import List, Set


class DifferenceOfTwoArray:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1: List[int] = nums1
        self.nums2: List[int] = nums2

    def efficient_solve(self) -> List[List[int]]:

        set1: Set[int] = set(self.nums1)
        set2: Set[int] = set(self.nums2)

        res: List[List[int]] = [list(set1 - set2), list(set2 - set1)]

        return res

    def solve(self) -> List[List[int]]:

        existed1: List[bool] = [False] * 2003
        existed2: List[bool] = [False] * 2003

        for c in self.nums1:
            existed1[c] = True
        for c in self.nums2:
            existed2[c] = True

        diff1: Set[int] = set()
        diff2: Set[int] = set()
        for c in self.nums1:
            if not existed2[c]:
                diff1.add(c)

        for c in self.nums2:
            if not existed1[c]:
                diff2.add(c)

        return [list(diff1), list(diff2)]


nums1 = [1,2,3]
nums2 = [2,4,6]

sln = DifferenceOfTwoArray(nums1, nums2)

print(sln.solve())
print(sln.efficient_solve())
