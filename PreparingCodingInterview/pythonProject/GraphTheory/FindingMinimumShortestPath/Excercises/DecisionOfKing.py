from typing import List, DefaultDict, Dict
from collections import defaultdict, deque


class Constraint:
    def __init__(self, s: int, n: int, k: int, o: str):
        self.s: int = s
        self.n: int = n
        self.k: int = k
        self.o: str = o


class DecisionOfKingSolution:
    def __init__(self, n: int, m: int, constraints: List[Constraint]):
        self.n: int = n
        self.m: int = m
        self.constraints: List[Constraint] = constraints

    def simulate(self) -> DefaultDict[int, Dict[int, int]]:
        g: DefaultDict[int, Dict[int, int]] = defaultdict(lambda : dict())

        for cs in self.constraints:

            if cs.o == 'lt':
                g[cs.s + cs.n][cs.s - 1] = cs.k
            elif cs.o == 'gt':
                g[cs.s - 1][cs.s + cs.n] = -cs.k

        return g

    def solve(self) -> bool:

        inf = 10**9
        min_dist: List[int] = [inf for _ in range(self.n+1)]
        in_queue: List[bool] = [False for _ in range(self.n+1)]
        visited: List[bool] = [False for _ in range(self.n+1)]
        cnt: List[int] = [0 for _ in range(self.n+1)]
        g: DefaultDict[int, Dict[int, int]] = self.simulate()
        for u in range(1, self.n+1):
            if not visited[u]:
                q: deque = deque()
                q.append(u)
                min_dist[u] = 0
                in_queue[u] = True
                visited[u] = True
                while q:
                    cur_n = q.popleft()
                    in_queue[cur_n] = False
                    dist_cur = min_dist[cur_n]
                    for v in g[cur_n].keys():
                        new_dist = dist_cur + g[cur_n][v]

                        if new_dist <= min_dist[v]:
                            visited[v] = True
                            min_dist[v] = new_dist

                            if not in_queue[v]:
                                q.append(v)
                                in_queue[v] = True
                                cnt[v] += 1
                                if cnt[v] > self.m:
                                    return False

        return True


n1, m1 = 1, 2

constraints1 = [Constraint(1, 0, 0, 'gt'), Constraint(1, 0, 0, 'lt')]

sln = DecisionOfKingSolution(n1, m1, constraints1)

print(sln.solve())




