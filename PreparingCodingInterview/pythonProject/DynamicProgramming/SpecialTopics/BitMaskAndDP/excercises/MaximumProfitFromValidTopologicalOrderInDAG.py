from typing import List, Dict as SparseTable, Tuple as Pair

class MaxProfitSolution:
    def __init__(self, n: int, edges: List[List[int]], score: List[int]):
        self.n: int = n
        self.edges: List[List[int]] = edges
        self.score: List[int] = score

    def solve(self) -> int:
        if len(self.edges) == 0:
            return sum((i + 1) * sc for i, sc in enumerate(sorted(self.score)))

        out_deg: List[List[int]] = [[] for _ in range(self.n)]
        degree: List[int] = [0] * self.n

        loss: List[int] = [0] * self.n

        for u, v in self.edges:
            out_deg[u].append(v)
            degree[v] += 1

        dp: SparseTable[int, Pair[int, List[int]]] = dict()
        nxt_dp: SparseTable[int, Pair[int, List[int]]] = dict()

        dp[0] = (0, loss)


        for no in range(1, self.n+1):
            nxt_dp.clear()
            for msk in dp.keys():
                profit, cur_loss = dp[msk]
                for u in range(self.n):
                    if ((msk >> u) & 1) == 1 or degree[u] - cur_loss[u] > 0:
                        continue

                    nxt_msk = msk | (1 << u)
                    cd_profit = profit + no * self.score[u]

                    nxt_loss = list(cur_loss)

                    for v in out_deg[u]:
                        nxt_loss[v] += 1

                    if not nxt_dp.get(nxt_msk, None):
                        nxt_dp[nxt_msk] = (cd_profit, nxt_loss)
                    elif nxt_dp[nxt_msk][0] < cd_profit:
                        nxt_dp[nxt_msk] = (cd_profit, nxt_loss)

            dp.clear()
            dp.update(nxt_dp)
        return dp[(1 << self.n) - 1][0]


if __name__ == '__main__':
    n = 3
    edges = [[0,1],[0,2]]
    score = [1,6,3]

    print(MaxProfitSolution(n, edges, score).solve())



