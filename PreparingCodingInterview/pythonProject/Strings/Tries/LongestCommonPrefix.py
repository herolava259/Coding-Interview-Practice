import math
from typing import List
from collections import defaultdict


class Node:
    def __init__(self):
        self.childs: List[Node | None] = [None for _ in range(26)]
        self.num_prefix: int = 0
        self.num_existed: int = 0
        self.par: Node | None = None
        self.dept: int = 0


def find_lca(u: Node, v: Node) -> Node | None:
    cur_u, cur_v = u, v

    if cur_v.dept > cur_u.dept:
        cur_v, cur_u = cur_u, cur_v

    while cur_u and cur_u.dept > cur_v.dept:
        cur_u = cur_u.par

    if cur_u is None:
        return None

    while cur_u != cur_v:
        cur_u = cur_u.par
        cur_v = cur_v.par

    return cur_u


class NaiveLCAResolver:
    pass


class Trie:
    def __init__(self):
        self.root: Node = Node()
        self.num_str: int = 0
        self.str_dict: defaultdict = defaultdict(None)

    def add_str(self, chain: str):

        cur_node: Node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            if cur_node.childs[offset] is None:
                cur_node.childs[offset] = Node()
                cur_node.childs[offset].par = cur_node
                cur_node.childs[offset].dept = cur_node.dept + 1
            cur_node.childs[offset].num_prefix += 1
            cur_node = cur_node.childs[offset]

        cur_node.num_existed += 1
        if self.str_dict[chain] is None:
            self.str_dict[chain] = cur_node

    def find_str(self, chain: str) -> Node | None:

        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')
            nxt_node = cur_node.childs[offset]

            if nxt_node is None:
                return None

            if nxt_node.num_prefix == 0 or nxt_node.num_existed == 0:
                return None

            cur_node = nxt_node

        return cur_node

    def delete_str_recursive(self, p: Node | None, chain: str, i: int) -> bool:

        if p is None:
            return False

        if i != len(chain):
            c = ord(chain[i]) - ord('a')
            check = self.delete_str_recursive(p.childs[c], chain, i + 1)

            if check:
                p.childs[c] = None
        else:
            p.num_existed -= 1

        if p != self.root:
            p.num_prefix -= 1

            if p.num_prefix == 0:
                del p
                return True

        return False


class SparseTableLCAResolver:
    def __init__(self, trie: Trie):
        self.node_map = trie.str_dict
        self.par_table: defaultdict = defaultdict(list)

        for k in self.node_map.keys():
            self.par_table[k] = [None for _ in range(22)]
            self.par_table[k][0] = k[:-1]

    def build(self):
        for j in range(1, 22):
            for k in self.node_map.keys():
                par_j_1 = self.par_table[k][j - 1]
                if par_j_1 is not None:
                    self.par_table[k][j] = self.par_table[par_j_1][j - 1]

    def find_lca(self, u: str, v: str) -> str:

        if len(u) > len(v):
            u, v = v, u

        diff_d = len(v) - len(u)

        for log_h in range(21, -1, -1):
            h = 1 << log_h

            if h < diff_d:
                v = self.par_table[v][log_h]
                diff_d -= log_h

        if u == v:
            return u

        log_h = math.ceil(math.log(len(u)))

        for k in range(log_h, -1, -1):
            if self.par_table[u] is None or self.par_table[u][k] == self.par_table[v][k]:
                continue

            u = self.par_table[u][k]
            v = self.par_table[v][k]

        return self.par_table[u][0]


class LongestCommonPrefixSolution:
    def __init__(self, arr: List[str]):
        self.arr = arr
        self.trie: Trie = Trie()
        self.resolver: NaiveLCAResolver = NaiveLCAResolver()

    def build(self):

        for chain in self.arr:
            self.trie.add_str(chain)

    def query(self, u: str, v: str) -> str:

        lca_node = find_lca(self.trie.find_str(u), self.trie.find_str(v))

        if lca_node is None:
            return ''

        res = ''

        while lca_node != self.trie.root:

            par = lca_node.par

            for idx, child in enumerate(par.childs):
                if child == lca_node:
                    res = chr(idx + ord('a')) + res
                    break
        return res
