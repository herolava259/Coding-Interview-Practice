from typing import List, DefaultDict as SparseTable, Tuple as Pair
from collections import defaultdict


class DisjointSet:
    def __init__(self):
        self.par: SparseTable[str, str] = defaultdict(lambda : '')

    def find(self, u: str):
        if not self.par[u]:
            return u

        self.par[u] = self.find(self.par[u])

        return self.par[u]


    def join(self, u: str, v: str):

        par_u, par_v = self.find(u), self.find(v)

        if par_u == par_v:
            return False
        self.par[par_v] = par_u

        return True

class RemoveStonesSolution:
    def __init__(self, stones: List[List[int]]):

        self.stones: List[List[int]] = stones


    def solve(self) -> int:

        def build_graph() -> Pair[List[Pair[str, str]], SparseTable[str, int]]:
            edge: List[Pair[str, str]] = []

            num_stone: SparseTable[str, int] = defaultdict(int)

            for x, y in self.stones:
                edge.append((f'row_{x}', f'col_{y}'))
                num_stone[f'row_{x}'] += 1
                num_stone[f'col_{y}'] += 1

            return edge, num_stone

        edges, num_pos = build_graph()
        anchor_stone = len(num_pos.keys())

        dsu: DisjointSet = DisjointSet()
        for u, v in edges:
            if not dsu.join(u, v):
                continue
            anchor_stone -= 1


        return len(self.stones) - anchor_stone


stones1 = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]

print(RemoveStonesSolution(stones1).solve())















