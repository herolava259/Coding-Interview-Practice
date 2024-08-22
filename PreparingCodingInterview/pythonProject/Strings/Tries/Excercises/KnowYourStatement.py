from typing import List


class Node:
    def __init__(self):
        self.child: List[Node | None] = [Node() for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0
        self.idx: List[int] = []
        self.exist_id: List[int] = []


class Trie:
    def __init__(self):
        self.root: Node = Node()

    def add_string(self, chain: str, idx: int = 0):

        cur_node: Node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                nxt_node = cur_node.child[offset] = Node()

            nxt_node.cnt += 1
            nxt_node.idx.append(idx)

            cur_node = nxt_node

        cur_node.exist += 1
        cur_node.exist_id.append(idx)
        return cur_node

    def find_string(self, chain: str) -> bool:
        cur_node: Node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return False

            cur_node = nxt_node

        return cur_node.exist > 0

    def delete_string(self, chain: str, idx: int) -> bool:

        if not self.find_string(chain):
            return False

        cur_node: Node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return True

            nxt_node.cnt -= 1
            nxt_node.idx.remove(idx)

            if nxt_node.cnt == 0:
                cur_node.child[offset] = None

            cur_node = nxt_node

        cur_node.exist -= 1
        cur_node.exist_id.remove(idx)
        return True


class KnowYourStatementSolution(Trie):

    def __init__(self, v: List[str]):
        super(KnowYourStatementSolution, self).__init__()

        self.v: List[str] = v
        self.n: int = len(v)

    def initialize(self):

        for chain in self.v:
            self.add_string(chain)

    def update(self, i: int, s: str):

        self.delete_string(self.v[i], i)

        self.v[i] = s

        self.add_string(s, i)

    def vprefix(self, l: int, r: int, s: str):

        cur_node = self.root
        list_idx = []
        for c in s:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                break
            list_idx.extend(nxt_node.exist_id)
            cur_node = nxt_node

        for e in list_idx:
            if l <= e <= r:
                return True

        return False

    def sprefix(self, l: int, r: int, s: str):

        cur_node = self.root

        for c in s:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return False

            cur_node = nxt_node

        for e in cur_node.idx:
            if l <= e <= r:
                return True

        return False
