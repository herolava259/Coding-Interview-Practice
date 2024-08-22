from typing import List


class Node:
    def __init__(self):
        self.child: List[List[Node | None]] = [[None for _ in range(26)] for _ in range(26)]
        self.num_exist = 0
        self.num_prefix = 0


def transform_double(s):
    return [(ord(c) - ord('a'), ord(i_c) - ord('a')) for c, i_c in zip(s, s[::-1])]


class DoubleTrie:

    def __init__(self):
        self.root: Node = Node()
        self.root.num_exist = -1
        self.root.num_prefix = -1
        self.cur: int = 0

    def add_string(self, s: str):

        d_s = transform_double(s)

        cur_node = self.root
        for c, i_c in d_s:

            if cur_node.child[c][i_c] is None:
                cur_node.child[c][i_c] = Node()
            cur_node = cur_node.child[c][i_c]
            cur_node.num_prefix += 1
        cur_node.num_exist += 1

    def find_string(self, s: str) -> bool:

        d_s = transform_double(s)
        cur_node = self.root
        for c, i_c in d_s:

            if cur_node.child[c][i_c] is None:
                return False
            cur_node = cur_node.child[c][i_c]

        return cur_node.num_exist >= 1

    def delete_string(self, s: str) -> bool:

        if not self.find_string(s):
            return False

        d_s = transform_double(s)

        cur_node = self.root

        for c, i_c in d_s:

            nxt_node = cur_node.child[c][i_c]

            if cur_node.num_prefix == 0:
                del cur_node

            if nxt_node is None:
                return False

            nxt_node.num_prefix -= 1
            cur_node = nxt_node

        cur_node.num_exist -= 1

        if cur_node.num_exist <= 0:
            del cur_node
        return True


class BeautifulEnglishSolution:
    def __init__(self, words: List[str]):
        self.words: List[str] = words
        self.d_trie: DoubleTrie = DoubleTrie()
        self.root: Node = self.d_trie.root

    def build(self):
        for w in self.words:
            self.d_trie.add_string(w)

    def solve(self) -> int:
        res = 0
        for i in range(26):
            for j in range(26):
                beg_node = self.root.child[i][j]
                if beg_node:
                    res += self.dfs_solve(beg_node, 1)

        return res

    def dfs_solve(self, cur_node: Node, dept: int) -> int:

        res: int = (cur_node.num_prefix // 2)*(dept ** 2 - (dept-1) ** 2)

        for i in range(26):
            for j in range(26):
                nxt_node = cur_node.child[i][j]

                if nxt_node is not None:
                    res += self.dfs_solve(nxt_node, dept + 1)

        return res
