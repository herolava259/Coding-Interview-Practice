from typing import List


class FindCentroidResolver:
    def __init__(self, g: List[List[int]], root: int):
        self.root: int = root
        self.g: List[List[int]] = g
        self.n: int = len(g)
        self.num_child: List[int] = [0] * (self.n+1)

    def initialize(self) -> None:
        self.count_child(self.root)

    def count_child(self, uid: int, pid: int = -1) -> int:

        def count_num(u: int, par: int) -> int:
            self.num_child[u] = 1
            for v in self.g[u]:
                if v == par:
                    continue
                self.num_child[u] += self.num_child[v]

            return self.num_child[u]

        return self.num_child[uid] if self.num_child[uid] > 0 else count_num(uid, pid)

    def find_centroid(self, uid: int, pid: int = -1)-> int:

        for v in self.g[uid]:
            if v == pid:
                continue

            if self.num_child[v] > (self.n // 2):
                return self.find_centroid(v, uid)

        return uid
