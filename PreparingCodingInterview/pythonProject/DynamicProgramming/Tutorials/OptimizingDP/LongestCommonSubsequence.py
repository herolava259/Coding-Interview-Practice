from typing import List


class LCSSolution:
    def __init__(self, chain_m: str, chain_n: str):

        self.chain_m: str = chain_m
        self.chain_n: str = chain_n

    def simple_solve(self) -> int:

        len_m, len_n = len(self.chain_m), len(self.chain_n)
        dp: List[List[int]] = [[0] * (len_n+1) for _ in range(len_m+1)]

        for len_i in range(1, len_m+1):
            for len_j in range(1, len_n+1):
                char_i, char_j = self.chain_m[len_i-1], self.chain_n[len_j-1]
                dp[len_i][len_j] = dp[len_i - 1][len_j - 1]
                if char_i == char_j:
                    dp[len_i][len_j] += 1

                dp[len_i][len_j] = max(dp[len_i][len_j], dp[len_i-1][len_j], dp[len_i][len_j-1])

        return dp[len_m][len_n]

    def opt_solve(self) -> int:

        len_m, len_n = len(self.chain_m), len(self.chain_n)

        def offset_of(c: str)-> int:
            return ord(c) - ord('A')

        def minimize(a: int, b: int):
            return b if a == -1 or a > b else a

        nxt_pos: List[List[int]] = [[0] * 26 for _ in range(len_m)]

        for i in range(26):
            for j in range(len_m-1, -1, -1):
                nxt_pos[j][i] = j+1 if (ord(self.chain_m[j + 1]) - ord('A') == i) else nxt_pos[j+1][i]


        max_len = min(len_m, len_n)

        dp: List[List[int]] = [[-1] * len_n for _ in range(len_n)]

        dp[0][0] = 0

        for i in range(len_n):
            for j in range(i+1):
                if dp[i][j] < 0:
                    continue

                dp[i+1][j] = minimize(dp[i+1][j], dp[i][j])

                new_idx = nxt_pos[dp[i][j]][offset_of(self.chain_n[i])]

                if new_idx > 0:
                    dp[i+1][j+1] = minimize(dp[i+1][j+1], new_idx)



        for j in range(max_len,0, -1):
            for i in range(j, len_n+1):
                if dp[i][j] >=0:
                    return j

        return 0




