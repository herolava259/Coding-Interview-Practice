from typing import List

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
class SpanningTree:
    def __init__(self, edges: List[Edge], ex_edges: List[Edge]):
        self.edges = edges
        self.external_edges = ex_edges


class BuildingSpanningTreeSolution:

    def __init__(self, g: List[List[int]], n: int, m: int):
        self.g = g
        self.num_node = n
        self.num_edge = m
        self.dfs_forest: List[SpanningTree] = []
        self.bfs_forest: List[SpanningTree] = []
        self.visited = [False for _ in range(n + 1)]
        self.par: List[int] = [0 for i in range(self.num_node + 1)]

    def reset_session(self):
        for i in range(self.num_node + 1):
            self.visited[i] = False
            self.par[i] = 0

    def dfs(self, u: int, p: int) -> (List[Edge], List[Edge]):

        self.visited[u] = True
        st: List[Edge] = []
        ex_edges = []
        for v in self.g[u]:
            if v == p or self.visited[v]:
                ex_edges.append(Edge(u, v))
                continue
            st.append(Edge(u, v))
            ex_child_edges, child_st = self.dfs(v, u)
            st.extend(child_st)
            ex_edges.extend(ex_child_edges)
        return ex_edges, st

    def bfs_all(self) -> List[SpanningTree]:
        self.reset_session()

        for i in range(1, self.num_node + 1):
            if not self.visited[i]:
                self.bfs_forest.append(self.bfs_solve(i))
        return self.bfs_forest

    def bfs_solve(self, root) -> SpanningTree:
        q: List[int] = [root]
        self.visited[root] = True

        st: List[Edge] = []
        ex: List[Edge] = []
        while len(q) != 0:

            u = q.pop(0)
            p = self.par[u]
            tmp_st, tmp_ex = self.bfs(u, p, q)
            st.extend(tmp_st)
            ex.extend(tmp_ex)
        return SpanningTree(st, ex)

    def bfs(self, u: int, p: int, q: List[int]) -> (List[Edge], List[Edge]):

        st: List[Edge] = []
        ex: List[Edge] = []
        for v in self.g[u]:
            if v == p:
                continue
            if self.visited[v]:
                ex.append(Edge(u, v))
                continue
            self.visited[v] = True
            self.par[v] = u
            st.append(Edge(u, v))
            q.append(v)
        return st, ex

    def dfs_all(self) -> List[SpanningTree]:

        for i in range(1, self.num_node + 1):
            if not self.visited[i]:
                ex_edges, st = self.dfs(i, 0)
                self.dfs_forest.append(SpanningTree(st, ex_edges))

        return self.dfs_forest
