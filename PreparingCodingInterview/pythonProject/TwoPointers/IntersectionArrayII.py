from typing import List

class IntersectionOfTwoArraysSolution:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1: List[int] = nums1
        self.nums2: List[int] = nums2

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
                results.append(self.nums1[p1])
                p1 += 1
                p2 += 1

        return results