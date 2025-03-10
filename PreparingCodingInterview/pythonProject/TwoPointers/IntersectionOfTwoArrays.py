from typing import List

class IntersectionOfArraysSolution:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1: List[int] = nums1
        self.nums2: List[int] = nums2

    def base_solve(self) -> List[int]:
        return list(set(self.nums1) & set(self.nums2))

    def solve(self) -> List[int]:

        self.nums1.sort()
        self.nums2.sort()

        p1, p2 = 0, 0
        results: List[int] = []

        while p1 < len(self.nums1) and p2 < len(self.nums2):

            while p1 < len(self.nums1) and self.nums1[p1] < self.nums2[p2]:
                p1 += 1

            while p2 < len(self.nums2) and self.nums2[p2] < self.nums1[p1]:
                p2 += 1
            if p1 >= len(self.nums1) or p2 >= len(self.nums2):
                break
            if self.nums1[p1] == self.nums2[p2]:
                val = self.nums1[p1]
                if not results or results[-1] < val:
                    results.append(val)
                p1 += 1
                p2 += 1

        return results
    def short_solve(self) -> List[int]:
        self.nums1.sort()
        self.nums2.sort()

        p1, p2 = 0, 0
        results: List[int] = []

        while p1 < len(self.nums1) and p2 < len(self.nums2):
            if self.nums1[p1] < self.nums2[p2]:
                p1 += 1
            elif self.nums1[p1] > self.nums2[p2]:
                p2 += 1
            else:
                if not results or results[-1] < self.nums1[p1]:
                    results.append(self.nums1[p1])
                p1 += 1
                p2 += 1

        return results

nums11 = [4,9,5]
nums21 = [9,4,9,8,4]

print(IntersectionOfArraysSolution(nums11, nums21).base_solve())
