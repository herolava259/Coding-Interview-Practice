from typing import List


class ListAllJointSolution:

    def __init__(self, g: List[List[int]], n: int, m: int):
        self.g = g
        self.num_node = n
        self.num_edge = m
        self.visited = [False for _ in range(self.num_node + 1)]
        self.nums = [0 for _ in range(self.num_node + 1)]
        self.lows = [0 for _ in range(self.num_node + 1)]
        self.time = 0
        self.joints: List[bool] = [False for _ in range(self.num_node + 1)]
        self.par_dfs = [-1 for _ in range(self.num_node + 1)]

    def reset(self):

        self.time = 0

        for i in range(self.num_node + 1):
            self.nums[i] = 0
            self.lows[i] = 0
            self.visited[i] = False
            self.joints[i] = False

    def dfs(self, u, p):

        self.visited[u] = True
        self.time += 1
        self.nums[u] = self.time
        self.lows[u] = self.nums
        self.par_dfs[u] = p

        for v in self.g[u]:
            if v == p:
                continue
            if self.visited[v]:
                self.lows[u] = min(self.nums[v], self.lows[u])
                continue
            self.dfs(v, u)
            self.lows[u] = min(self.lows[u], self.lows[v])

        if self.lows[u] == self.nums[u] and len(self.g[u]) > 1:
            self.joints[u] = True

    def solve(self) -> List[int]:
        self.reset()
        root = 1
        self.dfs(root, 0)

        num_child_root = 0

        for v in self.g[root]:
            if self.par_dfs[v] == root:
                num_child_root += 1

        if num_child_root >= 2:
            self.joints[root] = True
        else:
            self.joints[root] = False

        return [i for i in range(self.num_node + 1) if self.joints[i]]
