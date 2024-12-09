from typing import List, Tuple, Dict


class FindingMaxFormSolution:
    def __init__(self, strs: List[str], m: int, n: int):

        self.strs: List[str] = strs
        self.m: int = m
        self.n: int = n

    def solve(self) -> int:

        dp: List[List[int]] = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        tmp_dp: List[List[int]] = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        max_dp = 0

        for s in self.strs:
            num_one, num_zero = count_zeroes_and_ones(s)

            for i in range(num_zero, self.m + 1):
                for j in range(num_one, self.n + 1):
                    tmp_dp[i][j] = max(tmp_dp[i][j], dp[i - num_zero][j - num_one] + 1)
                    max_dp = max(max_dp, tmp_dp[i][j])

            clone(tmp_dp, dp, self.m + 1, self.n + 1)

        return max_dp


def clone(mtx: List[List[int]], clone_mtx: List[List[int]], m: int, n: int):
    for i in range(m):
        for j in range(n):
            clone_mtx[i][j] = mtx[i][j]

    return


def count_zeroes_and_ones(s: str) -> Tuple[int, int]:
    num_one = 0
    num_zero = 0
    for c in s:
        if c == '0':
            num_zero += 1
        elif c == '1':
            num_one += 1

    return num_one, num_zero


strs1 = ["10", "0001", "111001", "1", "0"]
m1 = 5
n1 = 3

sln = FindingMaxFormSolution(strs1, m1, n1)

print(sln.solve())
