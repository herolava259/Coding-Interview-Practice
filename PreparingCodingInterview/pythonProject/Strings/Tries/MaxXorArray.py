from builtins import int
from typing import List


class BinaryNode:
    def __init__(self):
        self.child: List[int] = [-1, -1]
        self.num_prefix: int = 0
        self.num_existed: int = 0


max_bit_size = 32
num_of_nodes = 200


class BinaryTrie:
    def __init__(self, num_bit: int = max_bit_size):

        self.height = num_bit
        self.bit_nodes: List[BinaryNode] = [BinaryNode() for _ in range(num_of_nodes + 1)]
        self.cur: int = 0

    def init_new_node(self) -> int:

        self.cur += 1

        self.bit_nodes[self.cur].child = [-1, -1]
        self.bit_nodes[self.cur].num_prefix = 0
        self.bit_nodes[self.cur].num_existed = 0

        return self.cur

    def add_num(self, num: int):

        pos = 0

        for i in range(self.height - 1, -1, -1):
            bit_num = (num >> i) & 1

            if self.bit_nodes[pos].child[bit_num] == -1:
                self.bit_nodes[pos].child[bit_num] = self.init_new_node()

            pos = self.bit_nodes[pos].child[bit_num]

            self.bit_nodes[pos].num_prefix += 1

        self.bit_nodes[pos].num_existed += 1

    def delete_num(self, x: int) -> bool:
        if not self.find_num(x):
            return False
        pos: int = 0
        for i in range(self.height, -1, -1):

            bit_num = (x >> i) & 1

            if self.bit_nodes[pos].child[bit_num] == -1:
                return False

            nxt_pos = self.bit_nodes[pos].child[bit_num]

            self.bit_nodes[nxt_pos].num_prefix -= 1

            if self.bit_nodes[nxt_pos].num_prefix <= 0:
                self.bit_nodes[pos].child[bit_num] = -1
                return True
            pos = nxt_pos

        self.bit_nodes[pos].num_existed -= 1

        return True

    def find_num(self, x) -> bool:

        pos: int = 0

        for i in range(self.height, -1, -1):
            bit_num = (x >> i) & 1

            if self.bit_nodes[pos].child[bit_num] == -1:
                return False
            pos = self.bit_nodes[pos].child[bit_num]

        return self.bit_nodes[pos].num_existed > 0


class MaxXorArraySolution(BinaryTrie):
    def __init__(self, arr: List[int]):
        super().__init__(max_bit_size)
        self.arr: List[int] = arr

    def build(self):

        for e in self.arr:
            self.add_num(e)

    def query_max_xor(self, x: int) -> int | None:
        return self.find_xor_max(0, 0, self.height + 1, x)

    def find_xor_max(self, cur_pos: int, cur_bit, cur_h: int, x: int) -> int | None:

        cur_node = self.bit_nodes[cur_pos]

        if cur_node.num_prefix <= 0:
            return None

        if cur_h == 0:
            return cur_bit

        bit_num = (x >> (cur_h - 1)) & 1

        primary_bit = 1 ^ bit_num
        nxt_pos = cur_node.child[primary_bit]
        if nxt_pos != -1:
            nxt_val = self.find_xor_max(nxt_pos, primary_bit, cur_h - 1, x)
            if nxt_val is not None:
                return (cur_bit << cur_h) | nxt_val

        secondary_bit = 1 - primary_bit
        nxt_pos = cur_node.child[secondary_bit]

        if nxt_pos == -1:
            return

        nxt_val = self.find_xor_max(nxt_pos, secondary_bit, cur_h - 1, x)

        if nxt_val is not None:
            return (cur_bit << cur_h) | nxt_val
        return None
