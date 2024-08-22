from typing import List
from TrieDataStructure import Trie, Node


class KthStringOfListSolution:

    def __init__(self, arr: List[str]):

        self.arr: List[str] = arr
        self.trie: Trie = Trie()
        self.n: int = len(arr)

    def build(self):
        for chain in self.arr:
            self.trie.add_string(chain)

    def query_k_string(self, k: int) -> str | None:
        return self.dfs_query(self.trie.root, k)

    def dfs_query(self, node: Node, k: int) -> str | None:

        if node.exist == 1:
            return ''
        if k > node.cnt:
            return None
        upper_bound = 0
        lower_bound = 0
        offset = -1
        selected_node: None | Node = None
        for child_node in node.child:
            offset += 1
            if child_node is None:
                continue
            upper_bound, lower_bound = lower_bound + child_node.cnt, upper_bound

            if upper_bound >= k:
                selected_node = child_node
                break

        if upper_bound < k or offset == -1 or not selected_node:
            return None

        cur_s = chr(ord('a') + offset)

        nxt_k = k - lower_bound

        nxt_s = self.dfs_query(selected_node, nxt_k)

        if nxt_s is None:
            return None

        return cur_s + nxt_s
