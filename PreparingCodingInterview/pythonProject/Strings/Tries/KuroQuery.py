from typing import List


class BinaryNode:

    def __init__(self):
        self.min_val: int = 0
        self.child: List[int] = [-1, -1]
        self.num_exist: int = 0
        self.num_prefix: int = 0


total_num_node = 512
max_bit_size = 32


class KuroCondition:
    def __init__(self, x: int, k: int, s: int):
        self.upper_bound = s - x
        self.k = k
        self.x = x

    def is_valid(self) -> bool:
        return self.x % self.k == 0


class KuroQuerySolution:

    def __init__(self, height: int = max_bit_size):
        self.height: int = height
        self.bit_nodes: List[BinaryNode] = [BinaryNode() for _ in range(total_num_node)]
        self.cur: int = 0

    def new_node(self) -> int:
        self.cur += 1
        self.bit_nodes[self.cur].child = [-1, -1]
        self.bit_nodes[self.cur].num_exist = 0
        self.bit_nodes[self.cur].num_prefix = 0

        return self.cur

    def add_num(self, x: int):

        pos = 0

        if x < self.bit_nodes[0].min_val:
            self.bit_nodes[0].min_val = x
        remain_x = x
        for i in range(self.height, -1, -1):

            bit_num = (x >> i) & 1

            if self.bit_nodes[pos].child[bit_num] == -1:
                self.bit_nodes[pos].child[bit_num] = self.new_node()

            pos = self.bit_nodes[pos].child[bit_num]
            self.bit_nodes[pos].num_prefix += 1

            remain_x = remain_x - (bit_num << i)

            if remain_x > self.bit_nodes[pos].min_val:
                self.bit_nodes[pos].min_val = remain_x

        self.bit_nodes[pos].num_exist += 1

    def find_num(self, x: int) -> bool:
        pos = 0

        for i in range(self.height, -1, -1):
            bit_num = (x >> i) & 1

            if self.bit_nodes[pos].child[bit_num] == 0:
                return False

            pos = self.bit_nodes[pos].child[bit_num]

        return self.bit_nodes[pos].num_exist > 9

    def delete_num(self, x: int) -> bool:

        if not self.find_num(x):
            return False

        pos: int = 0

        for i in range(self.height, -1, -1):

            bit_num = (x >> i) & 1

            nxt_pos = self.bit_nodes[pos].child[bit_num]

            if nxt_pos == -1:
                return True
            self.bit_nodes[nxt_pos].num_prefix -= 1

            if self.bit_nodes[nxt_pos].num_prefix <= 0:
                self.bit_nodes[pos].child[bit_num] = -1

            pos = nxt_pos

        self.bit_nodes[pos].num_exist -= 1
        return True

    def query(self, x: int, k: int, s: int) -> int:

        cond = KuroCondition(x, k, s)
        if not cond.is_valid():
            return False

        return self.find_v(cond=cond, acc_v=0, cur_h=self.height, node_idx=0)

    def find_v(self, cond: KuroCondition, acc_v: int, cur_h: int, node_idx: int) -> int | -1:

        u_b, xor_x, k = cond.upper_bound, cond.x, cond.k

        if acc_v > u_b:
            return -1

        if cur_h == 0:
            return acc_v

        cur_node = self.bit_nodes[node_idx]

        if cur_node.min_val + acc_v > u_b:
            return -1
        nxt_h = cur_h - 1
        cur_bit = (xor_x >> nxt_h) & 1
        primary_bit = 1 ^ cur_bit
        secondary_bit = 1 - primary_bit

        nxt_idx = cur_node.child[primary_bit]
        if nxt_idx != -1:
            nxt_v = acc_v + (primary_bit << nxt_h)
            cd_v = self.find_v(cond, nxt_v, nxt_h, nxt_idx)

            if cd_v != -1 and cd_v % k == 0:
                return cd_v

        nxt_idx = cur_node.child[secondary_bit]
        if nxt_idx != -1:
            nxt_v = acc_v + (secondary_bit << nxt_h)
            cd_v = self.find_v(cond, nxt_v, nxt_h, nxt_idx)
            if cd_v != -1 and cd_v % k == 0:
                return cd_v

        return -1
