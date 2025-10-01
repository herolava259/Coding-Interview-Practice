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

class MinimumTimeSolution:
    def __init__(self, n: int, edges: List[List[int]], k: int):
        self.n: int = n
        self.edges: List[List[int]] = edges
        self.k: int = k

    def solve(self) -> int:



        sorted_edges: List[List[int]] = sorted(self.edges, key = lambda c: c[2])

        def count_connected_components(lower_bound: int = 0):
            f_edges = sorted_edges[lower_bound:]

            dsu: DSU = DSU(self.n)

            num_component = self.n



            for uid, vid, _ in f_edges:
                if dsu.join(uid, vid):
                    num_component -= 1
            return num_component


        low, high = 0, len(sorted_edges) - 1

        while low < high:
            mid = (low + high) >> 1

            nc = count_connected_components(mid+1)

            if nc < self.k:
                low = mid + 1
            else:
                high = mid

        if low == 0 and count_connected_components() >= self.k:
            return 0

        return sorted_edges[low][2]


if __name__ == '__main__':
    n = 2
    edges = [[0,1,3]]
    k = 2

    print(MinimumTimeSolution(n, edges, k).solve())




