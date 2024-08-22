from typing import List


class DFSInUndirectedGraph:
    def __init__(self, graph: List[List[int]]):
        self.graph = graph

        self.num_node = len(graph)
        self.status = [0 for _ in range(self.num_node)]
        self.parents = [-1 for _ in range(self.num_node)]
        self.marks = [False for i in range(self.num_node)]

        self.inverse_edges = []

    def init_internal(self):
        self.status = [0 for _ in range(self.num_node)]
        self.parents = []
        self.marks = [False for i in range(self.num_node)]

        self.inverse_edges = []

    def run(self, u):

        for v in self.graph[u]:
            if not self.marks[v]:
                self.marks[v] = True
                self.status[v] = 1
                self.parents[v] = u
                self.run(v)
            else:
                self.inverse_edges.append((u, v))
        self.status[u] = 2
        return


class DFSOnGraphUsingStack:

    def __init__(self, graph: List[List[int]]):
        self.graph = graph

        self.num_vertex = len(graph)
        self.status = [-1 for _ in range(self.num_vertex)]
        self.marks = [False for _ in range(self.num_vertex)]
        self.parents = [-1 for _ in range(self.num_vertex)]
        self.inverse_edges = []
        self.tree_dfs = []

    def reset(self):
        self.marks = [False for _ in range(self.num_vertex)]
        self.parents = [-1 for _ in range(self.num_vertex)]
        self.inverse_edges = []
        self.tree_dfs = []

    def run(self, stack: List[int]) -> bool:

        if len(stack) == 0:
            return False
        u = stack.pop()
        for v in self.graph[u]:
            if not self.marks[v]:
                self.marks[v] = True
                self.status[v] = 0
                self.parents[v] = u
                stack.append(v)
                self.tree_dfs.append((u, v))
            else:
                self.inverse_edges.append((u, v))

        return True

    def proceed_dfs(self, begin: int = 0):
        stack = []

        self.reset()
        self.status[begin] = 0
        self.parents[begin] = -1
        self.marks[begin] = True

        stack.append(begin)

        while self.run(stack):
            pass

    def all_dfs(self):
        stack = []

        self.reset()

        for u in range(self.num_vertex):
            if not self.marks[u]:
                self.status[u] = 0
                self.parents[u] = -1
                self.marks[u] = True

                stack.append(u)

                while self.run(stack):
                    pass


class BaseBFSInUndirectedGraph:
    def __init__(self, graph: List[List[int]]):

        self.graph = graph
        self.num_vertex = len(graph)
        self.parents = [-1 for i in range(self.num_vertex)]
        self.marks = [False for _ in range(self.num_vertex)]
        self.status = [-1 for _ in range(self.num_vertex)]
        self.inverse_edges = []
        self.queue = []
        self.bfs_tree = []

    def reset(self):
        self.parents = [-1 for i in range(self.num_vertex)]
        self.marks = [False for _ in range(self.num_vertex)]
        self.status = [-1 for _ in range(self.num_vertex)]
        self.queue = []
        self.bfs_tree = []

    def run(self, u: int, p: int):

        self.parents[u] = p
        self.marks[u] = True
        self.status[u] = 0

        for v in self.graph[u]:
            if not self.marks[u]:
                self.queue.append((v, u))
                self.bfs_tree.append((u, v))
            else:
                self.inverse_edges.append((u, v))

    def bfs(self, beg: int):

        self.reset()

        self.queue.append((beg, -1))

        while self.queue:
            u, p = self.queue.pop(0)
            self.run(u, p)

        return self.bfs_tree

    def all_bfs(self) -> List[List[tuple]]:

        self.reset()

        bfs_forest = []
        for u in range(self.num_vertex):
            if not self.marks[u]:
                self.queue = [(u, -1)]
                self.inverse_edges = []
                self.bfs_tree = []
                while self.queue:
                    u, p = self.queue.pop(0)
                    self.run(u, p)

                bfs_forest.append(self.bfs_tree)

        return bfs_forest


