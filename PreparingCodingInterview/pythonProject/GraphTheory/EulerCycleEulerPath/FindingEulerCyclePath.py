from typing import List

class Edge:
    def __init__(self, target: int, eid: int):
        self.target = target
        self.eid = eid


class HierholzerSolution:
    def __init__(self, g: List[List[Edge]], num_edge):
        self.num_node = len(g)
        self.num_edge = num_edge
        self.g: List[List[Edge]] = g
        self.used_edge = [False for _ in range(self.num_edge + 1)]
        self.removed_node = [False for _ in range(self.num_node + 1)]
    def euler_walk(self, u: int) -> List[int]:

        res: List[int] = []

        tar = u
        while len(self.g[tar]) != 0:

            edge = self.g[tar].pop()

            if self.used_edge[edge.eid]:
                continue

            self.used_edge[edge.eid] = True

            tar = edge.target

            res.append(u)

        it = list(res)
        curr_idx = 0
        for idx, v in enumerate(it):
            curr_idx += 1
            if idx == 0:
                continue
            sub_cycle = self.euler_walk(v)
            sub_cycle = sub_cycle[:-1]
            res = res[:curr_idx] + sub_cycle + res[curr_idx:]
            curr_idx += len(sub_cycle)

        return res


