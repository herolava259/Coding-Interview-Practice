from typing import List


class TargetEdge:
    def __init__(self, freq: int, v: int):
        self.freq: int = freq
        self.v: int = v


class BicycleRoundSolution:
    def __init__(self, n: int, g: List[List[TargetEdge]], src: int = 1, dst: int = 2):
        self.n: int = n
        self.g: List[List[TargetEdge]] = g
        self.states: List[int] = [0 for _ in range(self.n + 1)]
        self.src: int = src
        self.dst: int = dst
        self.set_dst: set = set()

        for edge in self.g[self.dst]:
            self.set_dst.add(edge.v)

    def dfs_find_path(self, u: int, path: List[int]) -> (bool, List[List[int]]):
        new_path = list(path)
        new_path.append(u)
        if u == self.dst:
            set_path = set(new_path)
            if not set_path.isdisjoint(self.set_dst):
                return False, [-1]
            return [new_path]
        self.states[u] = 1
        res_paths: List[List[int]] = []
        for edge in self.g[u]:
            v = edge.v
            if self.states[v] == 1:
                self.states[u] = 2
                return True, []
            no_cycle, v_paths = self.dfs_find_path(v, new_path)
            if no_cycle is False:
                self.states[u] = 2
                return False, v_paths
            res_paths.extend(v_paths)
        self.states[u] = 2
        return True, res_paths

    def solve(self) -> int:

        no_cycle, all_paths = self.dfs_find_path(self.src, [])

        if not no_cycle:
            return -1
        res = 0
        for path in all_paths:
            res += self.calc_path(path)
        return res

    def calc_path(self, path: List[int]) -> int:

        res: int = 1
        u = path[0]
        for v in path[1:]:
            for edge in self.g[u]:
                if edge.v == v:
                    res *= edge.freq
                    break

            u = v
        return res


