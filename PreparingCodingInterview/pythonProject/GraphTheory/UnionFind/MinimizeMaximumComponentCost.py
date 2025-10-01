from typing import List


class DSU:
    def __init__(self, n: int):
        self.par: List[int] = list(range(n))
        self.n = n

    def find(self, u: int) -> int:
        if self.par[u] == u:
            return u
        self.par[u] = self.find(self.par[u])

        return self.par[u]
    def join(self, u: int, v: int) -> bool:

        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False

        self.par[par_v] = par_u

        return True

class MinimizeCostSolution:
    def __init__(self, n: int, edges: List[List[int]], k: int):
        self.n: int = n
        self.edges: List[List[int]] = edges
        self.k = k

    def solve(self,) -> int:

        sorted_edges = sorted(self.edges, key = lambda c: c[2])

        if self.n <= self.k:
            return 0

        def count_connected_components(upper_bound: int) -> int:
            cd_edges = sorted_edges[:upper_bound]

            dsu: DSU = DSU(self.n)
            num_components = self.n

            for uid, vid, _ in cd_edges:

                if dsu.join(uid, vid):
                    num_components -= 1

            return num_components

        low, high = 0, len(self.edges) - 1


        while low < high:
            mid = (low + high) >> 1

            nc = count_connected_components(mid+1)

            if nc > self.k:
                low = mid + 1
            else:
                high = mid



        return sorted_edges[low][2] if low >= 0 else 0

if __name__ == '__main__':
    n = 5
    edges = [[0,1,4],[1,2,91],[2,3,45],[0,4,18],[2,4,14],[0,3,63],[0,2,43],[1,4,2]]
    k = 1

    print(MinimizeCostSolution(n, edges, k).solve())






