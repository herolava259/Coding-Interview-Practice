from typing import List, Deque as Queue
from collections import deque as queue

class GardenNoAdjacentSolution:

    def __init__(self,n: int, paths: List[List[int]]):

        self.edges: List[List[int]] = paths
        self.n: int = n

    def solve(self) -> List[int]:

        def build_graph()-> List[List[int]]:

            graph: List[List[int]] = [[] for _ in range(self.n+1)]

            for uid, vid in self.edges:
                graph[uid].append(vid)
                graph[vid].append(uid)

            return graph

        g: List[List[int]] = build_graph()
        ans: List[int] = [0] * (self.n+1)

        q: Queue[int] = queue()


        for nid in range(1, self.n+1):
            if ans[nid] != 0:
                continue

            q.append(nid)

            while q:
                u = q.popleft()
                color = {1, 2, 3, 4}
                for v in g[u]:
                    if ans[v] == 0:
                        q.append(v)
                        continue
                    color -= {ans[v]}

                ans[u] = color.pop()

        return ans[1:]

n1 = 4
paths1 = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]

print(GardenNoAdjacentSolution(n1, paths1).solve())