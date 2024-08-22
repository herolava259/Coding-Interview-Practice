from typing import List, Set, Tuple


class BinaryNode:
    def __init__(self):
        self.child: List[int] = [-1, -1]

        self.cnt: int = 0
        self.exist: int = 0

        self.indexes: Set[int] = set()


class BinaryTrie:
    def __init__(self):
        self.nodes: List[BinaryNode] = [BinaryNode() for _ in range(100_000_00)]
        self.cur: int = 0

    def new_node(self) -> int:
        self.cur += 1
        cur_node: BinaryNode = self.nodes[self.cur]

        cur_node.child = [-1, -1]
        cur_node.cnt = 0
        cur_node.exist = 0
        cur_node.indexes.clear()
        return self.cur

    def add_num(self, x: int, idx: int):

        pos = 0

        for i in range(32):

            cur_bit = (x >> i) & 1

            cur_node = self.nodes[pos]

            nxt_pos = cur_node.child[cur_bit]

            if nxt_pos == -1:
                nxt_pos = cur_node.child[cur_bit] = self.new_node()
            nxt_node = self.nodes[nxt_pos]

            nxt_node.cnt += 1

            pos = nxt_pos

        self.nodes[pos].exist += 1
        self.nodes[pos].indexes.add(idx)

    def find_prefix_nums(self, x: int) -> Set[int]:

        res: Set[int] = set()

        pos = 0
        cur_val = 0
        for i in range(32):
            cur_bit = (x >> i) & 1
            cur_node = self.nodes[pos]

            nxt_pos = cur_node.child[cur_bit]

            if nxt_pos == -1:
                break
            nxt_node = self.nodes[nxt_pos]
            nxt_val = cur_val + (cur_bit << i)
            if nxt_node.exist > 0:
                res |= nxt_node.indexes

            pos = nxt_pos
            cur_val = nxt_val

        return res


class VeraModernArtSolution:

    def __init__(self, paint_drops: List[Tuple]):
        self.paint_drops: List[Tuple] = paint_drops
        self.x_trie: BinaryTrie = BinaryTrie()
        self.y_trie: BinaryTrie = BinaryTrie()
        self.colours: List[int] = []

    def build(self):

        for i, pd in enumerate(self.paint_drops):
            x, y, v = pd
            self.colours.append(v)
            self.x_trie.add_num(x, i)
            self.y_trie.add_num(y, i)

    def query_color(self, r: int, c: int) -> int:

        cd_x = self.x_trie.find_prefix_nums(r)
        cd_y = self.y_trie.find_prefix_nums(c)

        indexes = cd_y & cd_x

        total_c = 0

        for idx in indexes:
            total_c += self.colours[idx]

        return total_c
