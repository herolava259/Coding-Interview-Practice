from typing import List


class DSU:
    def __init__(self, n: int):

        self.n: int = n
        self.root: List[int] = list(range(self.n+1))

    def find_root(self, u: int) -> int:
        if self.root[u] == u:
            return u

        self.root[u] = self.find_root(self.root[u])

        return self.root[u]

    def merge(self, u: int, v: int) -> bool:

        root_u = self.find_root(u)
        root_v = self.find_root(v)

        if root_u == root_v:
            return False

        self.root[root_v] = root_u

        return True


class RedundantDirectConnectionSolution:

    def __init__(self, edges: List[List[int]]):
        self.edges: List[List[int]] = edges

    def solve(self) -> List[int]:

        n = len(self.edges)

        par: List[List[int]] = [[] for _ in range(n+1)]
        g: List[List[int]] = [[] for _ in range(n+1)]
        two_in_node: int = 0

        for u, v in self.edges:
            par[v].append(u)
            if len(par[v]) > 1:
                two_in_node = v
            if v not in g[u]:
                g[u].append(v)
            else:
                return [u, v]
            if u not in g[v]:
                g[v].append(u)
            else:
                return [u, v]


        if two_in_node:
            u1, u2 = par[two_in_node]
            in_circle = check_in_circle(g, n)
            if in_circle[u2]:
                return [u2, two_in_node]
            return [u1, two_in_node]
        u, v = 0, 0
        dsu: DSU = DSU(n)
        for edge in self.edges:
            u, v = edge
            if not dsu.merge(u, v):
                break

        return [u,v]


def check_in_circle(g: List[List[int]], n: int) -> List[bool]:

    lower: List[int] = [n+1] * (n+1)
    num: List[int] = [0] * (n+1)
    visited: List[bool] = [False] * (n+1)
    result: List[bool] = [False] * (n+1)

    def dfs(uid: int, pid: int = 0):
        lower[uid] = num[uid] = num[pid] + 1
        visited[uid] = True
        for vid in g[uid]:
            if vid == pid:
                continue
            if not visited[vid]:
                dfs(vid, uid)

            if num[vid] <= num[uid]:
                lower[uid] = min(num[vid], lower[uid])
                result[vid] = True
            else:
                lower[uid] = min(lower[uid], lower[vid])

        if lower[uid] < num[uid]:
            result[uid] = True
    dfs(1)

    return result




test1 = {'edges': [[4,1],[1,5],[4,2],[5,1],[4,3]]}
test2 = {'edges': [[1,2],[2,3],[3,4],[4,1],[1,5]]}
test3 = {'edges': [[2,1], [3,1], [4,2], [1,4]]}

sln1 = RedundantDirectConnectionSolution(**test1)
sln2 = RedundantDirectConnectionSolution(**test2)
sln3 = RedundantDirectConnectionSolution(**test3)

print('test1')
print(sln1.solve())

print('test2')
print(sln2.solve())

print('test3')
print(sln3.solve())


