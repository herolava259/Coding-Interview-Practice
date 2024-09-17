import re
import math
from typing import List


class HLDBase:

    def __init__(self, graph: List[List[int]], num_vertex=None):

        self.graph = graph
        self.num_vertex = num_vertex

        if self.num_vertex is None:
            self.num_vertex = len(self.graph)
        self.sz = [0 for _ in range(self.num_vertex)]
        self.depths = [0 for _ in range(self.num_vertex)]
        self.parents = [0 for _ in range(self.num_vertex)]
        self.head_of_chains = [-1 for _ in range(self.num_vertex)]
        self.chain_ids = [-1 for _ in range(self.num_vertex)]
        self.pos_of_vertexes = [-1 for _ in range(self.num_vertex)]
        self.flatten_edges = [-1 for _ in range(self.num_vertex)]

    def Dfs(self, u: int, p: int = -1):
        self.sz[u] = 1

        for v in self.graph[u]:
            if v == p:
                continue
            self.parents[v] = u
            self.depths[v] = self.depths[u] + 1
            self.Dfs(v, u)
            self.sz[u] += self.sz[v]

    def Hld(self, u: int, p: int = -1, chain_num: int = 0, cur_pos: int = 0) -> int:
        if self.head_of_chains[chain_num] == -1:
            self.head_of_chains[chain_num] = u
        self.chain_ids[u] = chain_num
        self.pos_of_vertexes[u] = cur_pos
        self.flatten_edges[cur_pos] = u

        sub_nodes = [node for node in self.graph[u] if node != p]
        nxt = sub_nodes[0]
        for v in sub_nodes[1:]:
            tmp = v
            if self.sz[tmp] > self.sz[nxt]:
                nxt = tmp
        last_chain_num = chain_num
        if nxt != 0:
            last_chain_num = self.Hld(nxt, u, last_chain_num, cur_pos + 1)
            cur_pos += self.sz[u]

        for v in sub_nodes:
            if v != nxt:
                last_chain_num = self.Hld(v, u, last_chain_num + 1, cur_pos + 1)
                cur_pos += self.sz[v]

        return last_chain_num

    def LCA(self, u: int, v: int) -> int:
        while self.chain_ids[u] != self.chain_ids[v]:
            if self.chain_ids[u] > self.chain_ids[v]:
                u = self.parents[self.head_of_chains[self.chain_ids[u]]]
            else:
                v = self.parents[self.head_of_chains[self.chain_ids[v]]]

        if self.depths[u] < self.depths[v]:
            return u
        return v


class SegmentTreeSolutionForXorTree:
    def __init__(self, tree: List[List[int]], num_vertex: int, val_of_vertex: List[int]):

        self.HLD = HLDBase(tree, num_vertex)
        self.segment_tree = [0 for _ in range(num_vertex * 4)]
        self.val_of_vertexes = val_of_vertex
        self.num_vertex = num_vertex

    def begin(self):
        self.HLD.Dfs(0)
        self.HLD.Hld(0)

    def build(self, ide: int, left: int, right: int):

        if left == right:
            self.segment_tree[ide] = self.val_of_vertexes[self.HLD.flatten_edges[left]]
            return

        mid = (left + right) // 2

        self.build(ide * 2, left, mid)
        self.build(ide * 2 + 1, mid + 1, right)

        self.segment_tree = self.segment_tree[ide * 2] ^ self.segment_tree[ide * 2 + 1]

    def update(self, nid: int, left: int, right: int, pos: int, val: int):

        if left > pos or right < pos:
            return

        if left == right:
            self.segment_tree[nid] = val
            return

        mid = (left + right) // 2

        self.update(nid * 2, left, mid, pos, val)
        self.update(nid * 2 + 1, mid + 1, right, pos, val)

        self.segment_tree[nid] = self.segment_tree[nid * 2] + self.segment_tree[nid * 2 + 1]

    def calc(self, nid: int, tleft: int, tright: int, left: int, right: int) -> int:

        if tleft > tright or tright < left:
            return 0

        if left <= tleft and tright <= right:
            return self.segment_tree[id]

        mid = (tleft + tright) // 2

        return self.calc(nid * 2, tleft, mid, left, right) ^ self.calc(nid * 2 + 1, mid + 1, tright, left, right)

    def update(self, x: int, val: int):
        self.update(1, 1, self.num_vertex, self.HLD.pos_of_vertexes[x], val)

    def query(self, u: int, v: int) -> int:

        lca = self.HLD.LCA(u, v)
        ans = 0
        while self.HLD.chain_ids[u] != self.HLD.chain_ids[lca]:
            ans ^= self.calc(1, 1, self.num_vertex,
                             self.HLD.pos_of_vertexes[self.HLD.head_of_chains[self.HLD.chain_ids[u]]],
                             self.HLD.pos_of_vertexes[u])
            u = self.HLD.parents[self.HLD.head_of_chains[self.HLD.chain_ids[u]]]

        while self.HLD.chain_ids[v] != self.HLD.chain_ids[lca]:
            ans ^= self.calc(1, 1, self.num_vertex,
                             self.HLD.pos_of_vertexes[self.HLD.head_of_chains[self.HLD.chain_ids[v]]],
                             self.HLD.pos_of_vertexes[v])
            v = self.HLD.parents[self.HLD.head_of_chains[self.HLD.chain_ids[v]]]

        if self.HLD.depths[u] < self.HLD.depths[v]:
            ans ^= self.calc(1, 1, self.num_vertex, self.HLD.pos_of_vertexes[u], self.HLD.pos_of_vertexes[v])
        else:
            ans ^= self.calc(1, 1, self.num_vertex, self.HLD.pos_of_vertexes[v], self.HLD.pos_of_vertexes[u])

        return ans
