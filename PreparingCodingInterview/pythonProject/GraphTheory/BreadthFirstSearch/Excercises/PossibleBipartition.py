from typing import List, Deque as Queue
from collections import  deque as queue

class PossibleBipartitionSolution:
    def __init__(self,n: int, dislikes: List[List[int]]):

        self.dislikes: List[List[int]] = dislikes
        self.n: int = n

    def solve(self) -> bool:

        state: List[int] = [0] * (self.n+1)

        g: List[List[int]] = [[] for _ in range(self.n+1)]

        for u, v in self.dislikes:
            g[u].append(v)
            g[v].append(u)

        for nid in range(1, self.n+1):

            if state[nid] != 0:
                continue

            state[nid] = 1
            q: Queue[int] = queue()

            q.append(nid)
            while q:
                uid = q.pop()
                cur_st = state[uid]
                near_st = 1 if cur_st == 2 else 2
                for vid in g[uid]:
                    if state[vid] == cur_st:
                        return False
                    elif state[vid] == near_st:
                        continue

                    state[vid] = near_st

                    q.append(vid)

        return True

n = 3
dislikes = [[1,2],[1,3],[2,3]]

print(PossibleBipartitionSolution(n, dislikes).solve())