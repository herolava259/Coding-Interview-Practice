from typing import List
from queue import Queue


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class TargetEdge:
    def __init__(self, v: int, eid: int):
        self.v = v
        self.eid = eid


class PoliceStationsSolution:

    def __init__(self, edges: List[Edge], n: int, d: int, stations: List[int]):
        self.edges: List[Edge] = edges
        self.n = n
        self.d = d
        self.stations = stations

    def bfs_solve(self) -> List[int]:

        g: List[List[TargetEdge]] = [[] for _ in range(self.n + 1)]
        for idx, edge in enumerate(self.edges):
            g[edge.u].append(TargetEdge(edge.v, idx))
            g[edge.v].append(TargetEdge(edge.u, idx))

        visited = [False for _ in range(self.n + 1)]
        visited_edge = [False for _ in range(len(self.edges))]
        prev = [(-1, 0) for _ in range(self.n + 1)]
        d_station = [-1 for _ in range(self.n + 1)]
        for u in range(1, self.n + 1):
            if visited[u] or u in self.stations:
                continue

            through = set()
            through.add(u)
            cur_u = u
            curr_d = 0
            q: Queue = Queue()
            q.put((cur_u, curr_d))
            while q:
                cur_u, curr_d = q.get()
                if cur_u in self.stations:
                    break
                if visited[cur_u] and curr_d + d_station[cur_u] <= self.d:
                    break
                elif visited[cur_u] and curr_d + d_station[cur_u] > self.d:
                    continue
                for e in g[cur_u]:
                    if e.v in through:
                        continue

                    prev[e.v] = (cur_u, e.eid)
                    q.put((e.v, curr_d + 1))
                    through.add(e.v)

            cur_d = 0
            if cur_u not in self.stations:
                cur_d = d_station[cur_u]

            while cur_u != u:
                cur_d += 1
                prev_u, eid = prev[cur_u]
                d_station[prev_u] = cur_d
                visited[prev_u] = True
                visited_edge[eid] = True
                cur_u = prev_u

        roads: List[int] = []

        for eid in range(len(self.edges)):
            if visited_edge[eid]:
                continue
            roads.append(eid + 1)

        return roads


n1, k1, d1 = 6, 3, 2
s1 = [1, 5, 6]

edge_str = '''1 2
1 3
1 4
1 5
5 6'''

edges1 = []
for line in edge_str.split('\n'):
    es = line.split(' ')
    edges1.append(Edge(int(es[0]), int(es[1])))

sln = PoliceStationsSolution(edges1, n1, d1, s1)

print(sln.bfs_solve())
