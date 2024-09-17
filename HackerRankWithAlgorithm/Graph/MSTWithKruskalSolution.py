from DisjoinSet import Dsu
from DisjoinSet import Edge
from typing import List


class KruskalSolution:
    @staticmethod
    def solve(graph: List[Edge], num_vertex: int) -> int:
        graph.sort(key=lambda e: e.c)
        dsu = Dsu(graph, num_vertex)

        min_total_weight = 0
        for edge in graph:

            if not dsu.join_dsu(edge.u, edge.v):
                continue
            min_total_weight += edge.c

        return min_total_weight

