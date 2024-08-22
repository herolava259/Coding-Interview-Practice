from typing import List

class Node:
    def __init__(self, nid: int, color: int):
        self.nid: int = nid
        self.color: int = color

class FlatteningTreeResolver:
    def __init__(self, n: int, tree: List[List[int]], root: int):
        self.n: int = n
        self.tree: List[List[int]] = tree
        self.root: int = root
        self.time: int = 0
        self.tour: List[int] = []
        self.st: List[int] = [-1 for _ in range(self.n + 1)]
        self.en: List[int] = [-1 for _ in range(self.n + 1)]
        self.parents: List[int] = [-1 for _ in range(self.n +1)]

    def dfs_build(self, u: int, p: int):
        self.time += 1
        self.st[u] = self.en[u] = self.time
        self.tour.append(u)
        self.parents[u] = p

        for v in self.tree[u]:
            if u != p:
                self.dfs_build(v, u)

        self.time += 1
        self.tour.append(u)
        self.en[u] = self.time
    
    def resolve(self) -> List[int]:
        if self.time == 0:
            self.dfs_build(self.root, -1)

        return self.tour




class DistinctColorsSolution:

    def __init__(self,n: int, colors: List[int], tree: List[List[int]], root: int):
        self.root = root
        self.tree = tree
        self.colors = colors
        self.n: int = n
        self.flatten_tree = FlatteningTreeResolver(n, tree,  root)
        self.count_distinct = [0 for i in range(self.n+1)]

    def dfs_solve(self,u: int, p: int) -> set:

        distinct_colors: set = {self.colors[u]}
        for v in self.tree[u]:
            if v != p:
                distinct_colors = distinct_colors | self.dfs_solve()
        self.count_distinct = len(distinct_colors)
        return distinct_colors

    def resolve_by_dfs(self) -> List[int]:

        self.dfs_solve(self.root, -1)

        return self.count_distinct

    def resolve_by_flatten_tree(self) -> List[int]:

        tour: List[int] = self.flatten_tree.resolve()
        st: List[int] = self.flatten_tree.st
        en: List[int] = self.flatten_tree.en
        time: int = self.flatten_tree.time

        s: List[(int, set)] = []
        for t in range(time):
            curr_node = tour[t]

            if t + 1 == st[curr_node]:
                s.append((curr_node, {self.colors[curr_node]}))
            elif t + 1 == en[curr_node]:
                dist_colors: set = set()

                while len(s) > 0 and s[-1][0] != curr_node:
                    top_node, tmp_colors = s.pop()

                    dist_colors = dist_colors | tmp_colors

                if len(s) > 0 and s[-1][0] == curr_node:
                    s[-1] = (curr_node, dist_colors | s[-1][1])
                    self.count_distinct[curr_node] = s[-1][1]

        return self.count_distinct







