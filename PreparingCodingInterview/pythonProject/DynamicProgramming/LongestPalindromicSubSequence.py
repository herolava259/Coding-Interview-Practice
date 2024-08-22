from typing import List, Tuple


class LPSubSequenceSolution:
    def __init__(self, s: str):
        self.s: str = s

    def create_idx_table(self) -> List[List[int]]:
        map_idx: List[List[int]] = [[] for _ in range(26)]

        for idx, c in enumerate(self.s):
            offset = ord(c) - ord('a')
            map_idx[offset].append(idx)

        return map_idx

    def solve(self) -> str:
        idx_tb = self.create_idx_table()
        n = len(self.s)
        dp: List[List[Tuple[int, str]]] = [[(0, '') if j != i else (1, self.s[i]) for j in range(n)] for i in range(n)]

        best_dp = (1, self.s[0])

        for i, c in enumerate(self.s):
            offset = ord(c) - ord('a')
            for idx in idx_tb[offset]:
                if idx == i:
                    break
                tmp_dp = (2, c + c)
                if i > idx + 1:
                    tmp_dp = (tmp_dp[0] + dp[idx + 1][i - 1][0], c + dp[idx + 1][i - 1][1] + c)
                for j in range(idx, -1, -1):
                    for k in range(i, n, 1):
                        if dp[j][k][0] < tmp_dp[0]:
                            dp[j][k] = (tmp_dp[0], tmp_dp[1])

                if tmp_dp[0] > best_dp[0]:
                    best_dp = tmp_dp

        return best_dp[1]


s1 = 'cbbd'

sln = LPSubSequenceSolution(s1)

print(sln.solve())
