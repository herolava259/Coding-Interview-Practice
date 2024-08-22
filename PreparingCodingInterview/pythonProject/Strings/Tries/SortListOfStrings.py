from typing import List
from TrieDataStructure import Trie, Node


class DFSTrie(Trie):
    def __init__(self):
        self.sorted_str: List[str] = []
        Trie.__init__(self)

    def dfs_search(self, u: Node, cur_str: str):

        for _ in range(u.exist):
            self.sorted_str.append(cur_str)

        a_int = ord('a')
        for i in range(26):
            nxt_child: Node | None = u.child[i]

            if nxt_child is None:
                continue
            next_str = cur_str + chr(i + a_int)

            self.dfs_search(nxt_child, next_str)

    def get_ordered_list(self) -> List[str]:

        if not self.sorted_str:
            self.dfs_search(self.root, '')

        return self.sorted_str


class SortListOfStringsSolution:
    def __init__(self, arr: List[str]):
        self.n = len(arr)
        self.arr: List[str] = arr
        self.trie: DFSTrie = DFSTrie()

    def initialize(self):
        for s in self.arr:
            self.trie.add_string(s)

    def solve(self) -> List[str]:
        self.initialize()
        return self.trie.get_ordered_list()
