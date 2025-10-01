from typing import List


class SumOfDistanceInTreeSolution:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n: int = n
        self.edges: List[List[int]] = edges

    def solve(self) -> List[int]:

        g: List[List[int]] = [[] for _ in range(self.n)]

        num_desc: List[int] = [0] * self.n

        for uid, vid in self.edges:
            g[uid].append(vid)
            g[vid].append(uid)

        result: List[int] = [0] * self.n

        def dfs_first(u, p=-1):


            for v in g[u]:
                if v == p:
                    continue

                num_desc[u] += 1

                dfs_first(v, u)
                num_desc[u] += num_desc[v]
                result[u] += result[v]

            result[u] += num_desc[u]



        def dfs_second(u, p = -1):

            outer_u = 0
            outer_desc = 0
            if p != -1:
                outer_u = result[p] - result[u] - num_desc[u] - 1
                outer_desc = self.n - num_desc[u] - 1

            result[u] += outer_u + outer_desc

            for v in g[u]:
                if v == p:
                    continue
                dfs_second(v, u)

        dfs_first(0)
        dfs_second(0)

        return result


if __name__ == '__main__':
    n = 2
    edges = [[1,0]]
    print(SumOfDistanceInTreeSolution(n, edges).solve())