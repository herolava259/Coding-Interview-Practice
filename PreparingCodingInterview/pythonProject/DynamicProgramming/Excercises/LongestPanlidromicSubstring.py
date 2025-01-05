from typing import List, Tuple


class LPSubstringSolution:
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
        dp: List[List[bool]] = [[False if j != i else True for j in range(n)] for i in range(n)]

        best_dp = 1
        bst_beg, bst_end = 0, 0

        for i, c in enumerate(self.s):
            offset = ord(c) - ord('a')
            for idx in idx_tb[offset]:
                if i == idx:
                    break
                if i == idx + 1:
                    dp[idx][i] = True
                else:
                    dp[idx][i] = dp[idx + 1][i - 1]
                if dp[idx][i] and (i - idx + 1) > best_dp:
                    best_dp = i - idx + 1
                    bst_beg, bst_end = idx, i
        return self.s[bst_beg: bst_end + 1]

s1 = "aacabdkacaa"

sln = LPSubstringSolution(s1)

print(sln.solve())
