from typing import List


class NaiveMaxAreaSolution:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr

    def solve(self):

        max_area = -1

        n = len(self.arr)

        for i in range(n):
            for j in range(i + 1, n):
                new_area = (j - i) * min(self.arr[i], self.arr[j])

                max_area = max(new_area, max_area)

        return max_area


class DPMaxAreaSolution:

    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr

    def solve(self) -> int:

        p1 = 0

        max_area = 0
        n = len(self.arr)

        for i in range(1, n):
            if self.arr[i] > max(self.arr[i - 1], self.arr[p1]):
                tmp_max = 0
                tmp_p = p1
                while tmp_p <= i - 1:
                    if min(self.arr[tmp_p], self.arr[i]) * (i - tmp_p) >= tmp_max:
                        p1 = tmp_p
                        tmp_max = min(self.arr[tmp_p], self.arr[i]) * (i - tmp_p)
                    tmp_p += 1
                max_area = max(max_area, tmp_max)
            elif self.arr[i] < min(self.arr[i - 1], self.arr[p1]):
                tmp_max = 0
                tmp_p = p1
                while tmp_p >= 0:
                    if min(self.arr[tmp_p], self.arr[i]) * (i - tmp_p) > tmp_max:
                        p1 = tmp_p
                        tmp_max = min(self.arr[tmp_p], self.arr[i]) * (i - tmp_p)
                    tmp_p -= 1
                max_area = max(max_area, tmp_max)
            else:
                max_area = max(min(self.arr[p1], self.arr[i]) * (i - p1), max_area)

        return max_area


class TwoPointerMaxAreaSolution:

    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr

    def solve(self):

        p1, p2 = 0, len(self.arr)-1
        max_area = min(self.arr[p1], self.arr[p2]) * (p2 - p1)
        while p1 < p2:

            if self.arr[p1] < self.arr[p2]:
                p1 += 1
            else:
                p2 -= 1

            max_area = max(max_area, min(self.arr[p1], self.arr[p2]) * (p2 - p1))

        return max_area


height1 = [1, 2, 4, 3]

sln = NaiveMaxAreaSolution(height1)
opt_sln = TwoPointerMaxAreaSolution(height1)
dp_sln = DPMaxAreaSolution(height1)
print(opt_sln.solve())
