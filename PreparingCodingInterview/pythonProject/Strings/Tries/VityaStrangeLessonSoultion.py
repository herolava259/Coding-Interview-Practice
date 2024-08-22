from typing import List


class BinaryNode:
    def __init__(self):
        self.child: List[int] = [-1, -1]
        self.num_prefix = 0
        self.num_exist = 0
        self.num_node = 1


max_nodes = 10000
max_bit_size = 32


class BinaryTrieResolver:

    def __init__(self, max_height: int = max_bit_size):
        self.nodes: List[BinaryNode] = [BinaryNode() for _ in range(max_nodes)]
        self.cur: int = 0
        self.height: int = max_height

    def new_node(self) -> int:
        self.cur += 1
        new_node: BinaryNode = self.nodes[self.cur]

        new_node.num_exist = 0
        new_node.num_prefix = 0

        new_node.child = [-1, -1]

        new_node.num_node = 0

        return self.cur

    def add_num(self, x: int):
        pos = 0

        for i in range(self.height - 1, -1, -1):
            bit_num = (x >> i) & 1
            cur_node: BinaryNode = self.nodes[pos]

            if cur_node.child[bit_num] == -1:
                cur_node.child[bit_num] = self.new_node()

            nxt_pos = cur_node.child[bit_num]
            nxt_node = self.nodes[nxt_pos]

            nxt_node.num_prefix += 1
            nxt_node.num_node += 1

            pos = nxt_pos

        self.nodes[pos].num_exist += 1

    def find_num(self, x: int) -> bool:

        pos: int = 0

        for i in range(self.height - 1, -1, -1):
            cur_node = self.nodes[pos]
            bit_num: int = (x >> i) & 1

            if cur_node.child[bit_num] == -1:
                return False
            nxt_pos = cur_node.child[bit_num]

            pos = nxt_pos

        return self.nodes[pos].num_exist > 0

    def delete_num(self, x: int) -> bool:

        if not self.find_num(x):
            return False
        pos = 0
        for i in range(self.height - 1, -1, -1):
            cur_node = self.nodes[pos]

            bit_num: int = (x >> i) & 1

            if cur_node.child[bit_num] == -1:
                return False

            nxt_pos = cur_node.child[bit_num]

            nxt_node = self.nodes[nxt_pos]

            nxt_node.num_prefix -= 1
            nxt_node.num_node -= 1

            if nxt_node.num_prefix <= 0:
                return True
            pos = nxt_pos

        self.nodes[pos].num_exist -= 1
        return True


class VityaAndStrangeLessonSolution(BinaryTrieResolver):

    def __init__(self, arr: List[int]):
        super().__init__()
        self.arr: List[int] = arr
        self.xor_x = 0

    def build(self):
        for e in self.arr:
            self.add_num(e)

    def find_med(self, x: int, cur_h: int, pos: int, acc_v: int) -> int:

        if cur_h == 0 or pos == -1:
            return acc_v

        nxt_h = cur_h - 1
        bit_num: int = (x >> nxt_h) & 1

        primary_bit = 0 ^ bit_num
        cur_node = self.nodes[pos]
        nxt_pos = cur_node.child[primary_bit]

        if not self.is_perfect(nxt_pos):
            nxt_v = acc_v | (primary_bit << nxt_h)
            return self.find_med(x, nxt_h, nxt_pos, nxt_v)

        secondary_bit = 1 - primary_bit
        nxt_pos = cur_node.child[secondary_bit]

        if self.is_perfect(nxt_pos):
            return acc_v + ((1 << cur_h) - 1)

        nxt_v = acc_v | (primary_bit << nxt_h)
        return self.find_med(x, nxt_h, nxt_pos, nxt_v)

    def is_perfect(self, pos: int) -> bool:
        if pos == -1:
            return False

        cur_node = self.nodes[pos]
        left_pos, right_pos = cur_node.child[0], cur_node.child[1]

        if left_pos == -1 and right_pos == -1:
            return True
        elif left_pos == -1 or right_pos == -1:
            return False

        left_node = self.nodes[left_pos]
        right_node = self.nodes[right_pos]
        return left_node.num_node == right_node.num_node

    def change_and_query(self, x: int) -> int:
        self.xor_x ^= x
        return self.find_med(self.xor_x, self.height - 1, pos=0, acc_v=0)
