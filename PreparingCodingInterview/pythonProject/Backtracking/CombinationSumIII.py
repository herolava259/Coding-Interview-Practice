from typing import List


class CombinationSumIIISolution:
    def __init__(self, k: int, n: int):

        self.k: int = k
        self.n: int = n

    def solve(self) -> List[List[int]]:

        result: List[List[int]] = []

        def backtrack(arr: List[int], sums: int, beg: int = 0):

            if len(arr) == self.k:
                if sums == self.n:
                    result.append(list(arr))

            for i in range(beg, 10):
                if sums + i <= self.n:
                    arr.append(i)
                    backtrack(arr, sums+i, i+1)
                    arr.pop()

        backtrack([], 0, 1)

        return result


sln = CombinationSumIIISolution(3, 9)

print(sln.solve())