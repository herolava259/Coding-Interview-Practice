from typing import List
from collections import defaultdict


class Node:
    def __init__(self, i: int, j: int, m_row: int, n_col: int, height: int):

        self.c_i = i
        self.c_j = j
        self.height = height
        self.m_row = m_row
        self.n_col = n_col
        self.nid = n_col * i + j
        self.is_out: bool = False
        if i == 0 or i == m_row - 1 or j == 0 or j == n_col - 1:
            self.is_out = True

    def adj_nodes(self, node_arr: list) -> list:

        adj_nodes: list = []

        if self.c_i + 1 < self.m_row:
            adj_nodes.append(node_arr[self.n_col * (self.c_i + 1) + self.c_j])

        if self.c_i - 1 >= 0:
            adj_nodes.append(node_arr[self.n_col * (self.c_i - 1) + self.c_j])

        if self.c_j + 1 < self.n_col:
            adj_nodes.append(node_arr[self.nid + 1])

        if self.c_j - 1 >= 0:
            adj_nodes.append(node_arr[self.nid - 1])

        return adj_nodes


class DSU:
    def __init__(self, n: int, nodes: List[Node]):

        self.par = [-1 for _ in range(n)]
        self.n = n
        self.nodes: List[Node] = nodes

    def find(self, u: int):
        if self.par[u] < 0:
            return u

        self.par[u] = self.find(self.par[u])

        return self.par[u]

    def get_num_node(self, nid: int) -> int:
        root_id = self.find(nid)

        return -self.par[root_id]

    def find_root_node(self, u: int) -> Node:
        root_u = self.find(u)

        return self.nodes[root_u]

    def join(self, u: int, v: int) -> bool:

        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False

        self.par[par_u] += self.par[par_v]
        self.par[par_v] = par_u

        self.nodes[u].is_out = self.nodes[u].is_out or self.nodes[v].is_out

        return True

    def adj_nodes_of(self, nid: int) -> List[Node]:
        return self.nodes[nid].adj_nodes(self.nodes)


class C11WaterSolution:

    def __init__(self, m_row: int, n_col: int, matrix: List[List[int]]):
        self.m_row: int = m_row
        self.n_col: int = n_col
        self.matrix: List[List[int]] = matrix
        self.dsu: DSU | None = None
        self.node_tb: defaultdict = defaultdict(list)

    def build(self):

        nodes: List[Node] = []

        for i in range(self.m_row):
            for j in range(self.n_col):
                new_node = Node(i, j, self.m_row, self.n_col, self.matrix[i][j])
                nodes.append(new_node)
                self.node_tb[self.matrix[i][j]].append(new_node)

        self.dsu = DSU(self.m_row * self.n_col, nodes)

    def find_and_update(self, node: Node) -> int:
        root_node = self.dsu.find_root_node(node.nid)
        res = 0
        for adj_node in self.dsu.adj_nodes_of(node.nid):

            root_adj_node = self.dsu.find_root_node(adj_node.nid)

            if root_node.nid != root_adj_node.nid and root_node.height >= root_adj_node.height:
                if not root_adj_node.is_out:
                    num_nodes = self.dsu.get_num_node(root_adj_node.nid)
                    res += num_nodes * (root_node.height - root_adj_node.height)

                self.dsu.join(root_node.nid, root_adj_node.nid)
        return res

    def solve(self) -> int:

        sorted_heights = list(self.node_tb.keys())

        sorted_heights.sort()

        res = 0

        for height in sorted_heights:
            for node in self.node_tb[height]:
                res += self.find_and_update(node)

        return res
