from typing import List


class CountNumLengthKPathSolution:
    def __init__(self, g: List[List[int]], k: int):
        self.g: List[List[int]] = g
        self.k: int = k
        self.n_total: int = len(self.g)
        self.child: List[int] = [1] * (self.n_total + 1)
        self.delete: List[bool] = [False] * (self.n_total + 1)

    def count_child(self, u: int, parent: int = -1) -> int:

        self.child[u] = 1
        for v in self.g[u]:
            if v != parent and not self.delete[v]:
                self.child[u] += self.count_child(v, u)

        return self.child[u]

    def find_centroid(self, u: int, p: int, n: int) -> int:
        for v in self.g[u]:
            if v != p and self.child[v] > (n//2) and not self.delete[v]:
                return self.find_centroid(v, u, n)

        return u

    def calc_num_k_path_of(self, root: int) -> int:

        len_k_child: List[List[int]] = []

        def length_to_root(uid: int, pid: int, depth: int = 1):
            new_depth = depth + 1
            for vid in self.g[u]:
                if self.delete[vid] or pid == vid:
                    continue
                len_k_child[-1][new_depth] += 1
                length_to_root(vid, uid, new_depth)
            return
        def convolution(arr: List[int]) -> int:
            len_arr = len(arr)
            return sum(arr[i] * arr[len_arr-i] for i in range(len_arr))

        for u in self.g[root]:
            if self.delete[u]:
                continue
            len_k_child.append([0] * (self.k + 1))
            length_to_root(u, root)

        col_total = [sum(map(lambda arr: arr[i], len_k_child)) for i in range(1, self.k+1)]
        k_total = col_total.pop()
        col_total.pop(0)
        return (convolution(col_total) - sum(convolution(len_k_child[i]) for i in range(len(len_k_child)))
                + k_total)
    def solve(self, u: int = 1) -> int:
        self.count_child(u)
        n = self.child[u]
        centroid: int = self.find_centroid(u, -1, n)

        num_k_path = self.calc_num_k_path_of(centroid)
        self.delete[centroid] = True

        for v in self.g[centroid]:
            if self.delete[v]:
                continue
            num_k_path += self.solve(v)
        return num_k_path