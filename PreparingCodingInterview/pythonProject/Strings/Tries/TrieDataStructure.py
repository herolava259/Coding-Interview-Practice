from typing import List


class Node:
    def __init__(self):
        self.child: List[Node | None] = [None for _ in range(26)]

        self.exist: int = 0
        self.cnt: int = 0


class Trie:
    def __init__(self):
        self.cur: int = 0
        self.root: Node = Node()

    def add_string(self, s: str):

        cur_p: Node = self.root

        for c in s:
            offset = ord(c) - ord('a')

            if cur_p.child[offset] is None:
                cur_p.child[offset] = Node()

            cur_p = cur_p.child[offset]
            cur_p.cnt += 1
        self.cur += 1
        cur_p.exist += 1

    def delete_string_recursive(self, p: Node, s: str, i: int) -> bool:

        if i != len(s):
            c = ord(s[i]) - ord('a')
            is_child_deleted = self.delete_string_recursive(p.child[c], s, i + 1)
            if is_child_deleted:
                p.child[c] = None

        else:
            p.exist -= 1

        if p != self.root:
            p.cnt -= 1

            if p.cnt == 0:
                del p
                return True

        return False

    def delete_string(self, s):

        if not self.find_string(s):
            return

        self.delete_string_recursive(self.root, s, 0)

        self.cur -= 1

    def find_string(self, s: str) -> bool:

        p = self.root

        for f in s:
            off = ord(f) - ord('a')

            if p.child[off] is None:
                return False

            p = p.child[off]

        return p.exist != 0


class BinaryNode:
    def __init__(self):
        self.child: List[int] = [0, 0]
        self.prefix_of: int = 0
        self.num_of_num: int = 0


max_bit_size = 100


class BinaryTrie:
    def __init__(self, num_node: int):

        self.num_node = num_node
        self.nodes: List[BinaryNode] = [BinaryNode() for _ in range(num_node)]
        self.cur: int = 0
        for i in range(2):
            self.nodes[self.cur].child[i] = -1

        self.nodes[self.cur].num_of_num = self.nodes[self.cur].prefix_of = 0

    def new_node(self) -> int:

        self.cur += 1
        for i in range(2):
            self.nodes[self.cur].child[i] = -1
        self.nodes[self.cur].num_of_num = self.nodes[self.cur].prefix_of = 0

        return self.cur

    def add_number(self, x: int):

        pos: int = 0

        for i in range(max_bit_size, -1, -1):

            bit_c = (x >> i) & 1

            if self.nodes[pos].child[bit_c] == -1:
                self.nodes[pos].child[bit_c] = self.new_node()
            pos = self.nodes[pos].child[bit_c]
            self.nodes[pos].prefix_of += 1

        self.nodes[pos].num_of_num += 1

    def delete_number(self, x: int):

        if not self.find_number(x):
            return

        pos = 0

        for i in range(max_bit_size, -1, -1):

            c: int = (x >> i) & 1

            tmp: int = self.nodes[pos].child[c]

            if tmp == -1:
                return

            self.nodes[tmp].prefix_of -= 1

            if self.nodes[tmp].prefix_of == 0:
                self.nodes[pos].child[c] = -1
                return
            pos = tmp
        self.nodes[pos].num_of_num -= 1

    def find_number(self, x: int) -> bool:

        pos: int = 0

        for i in range(max_bit_size, -1, -1):
            c = x & (1 << i)

            if self.nodes[pos].child[c] == -1:
                return False
            pos = self.nodes[pos].child[c]
        return self.nodes[pos].num_of_num != 0
