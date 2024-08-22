from typing import List

class TargetEdge:
    def __init__(self, v: int, eid: int, weight: int):
        self.v = v
        self.eid = eid
        self.w = weight



class MarathonSolution:
    def __init__(self, g: List[List[TargetEdge]], n: int, m: int):
        self.g: List[List[TargetEdge]] = g
        self.n = n
        self.m = m
        self.used_edge = [False for _ in range(self.m + 1)]

    def solve(self) -> List[int]|None:
        matrix_w: List[List[int]] = [[0 for _ in range(self.n + 1)] for i in range(self.n + 1)]

        for u in range(1, self.n + 1):
            if len(self.g[u]) % 2 != 0:
                return None
            for tar_v in self.g[u]:
                matrix_w[u][tar_v.v] = tar_v.w
                matrix_w[tar_v.v][u] = tar_v.w

        normal_cycle = self.euler_walk(1)

        min_w = 10 ** 9 + 7
        u = normal_cycle[0]
        total_w = 0
        min_id = 0
        for idx, v in enumerate(normal_cycle):
            if idx == 0:
                continue
            total_w += matrix_w[u][v]
            if total_w < min_w:
                min_w = total_w
                min_id = idx

        res_cycle = normal_cycle[min_id:] + normal_cycle[:min_id]

        return res_cycle

    def euler_walk(self, u) -> List[int]:
        res: List[int] = []
        curr = u
        while len(self.g[curr]) != 0:
            edge = self.g[u].pop()

            if self.used_edge[edge.eid]:
                continue
            self.used_edge[edge.eid] = True
            res.append(curr)
            curr = edge.v

        curr_id = 0
        it = list(res)
        for idx, v in enumerate(it):

            curr_id += 1
            if idx == 0:
                continue
            sub_cycle = self.euler_walk(v)
            sub_cycle = sub_cycle[:-1]
            res = res[:curr_id] + sub_cycle + res[curr_id:]
            curr_id += len(sub_cycle)

        return res
