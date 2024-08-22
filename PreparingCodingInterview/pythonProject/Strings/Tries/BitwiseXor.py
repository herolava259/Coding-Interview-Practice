from typing import List

max_bit_size = 33
max_node = 10000


class BinaryNode:
    def __init__(self):
        self.child: List[int] = [-1, -1]
        self.cnt: int = 0
        self.exist: int = 0


class BinaryTrie:
    def __init__(self, height: int = max_bit_size):
        self.height = height
        self.nodes: List[BinaryNode] = [BinaryNode() for _ in range(max_node)]
        self.cur: int = 0

    def new_node(self) -> int:
        self.cur += 1
        cur_node = self.nodes[self.cur]

        cur_node.child = [-1, -1]
        cur_node.cnt = 0
        cur_node.exist = 0

        return self.cur

    def add_num(self, x: int):

        pos = 0

        for i in range(self.height, -1, -1):
            cur_node = self.nodes[pos]
            c = (x >> i) & 1
            if cur_node.child[c] == -1:
                cur_node.child[c] = self.new_node()
            nxt_pos = cur_node.child[c]

            nxt_node = self.nodes[nxt_pos]

            nxt_node.cnt += 1

            pos = nxt_pos

        self.nodes[pos].exist += 1

    def find_num(self, x: int) -> bool:

        pos = 0

        for i in range(self.height, -1, -1):

            c = (x >> i) & 1

            nxt_pos = self.nodes[pos].child[c]

            if nxt_pos == -1:
                return False

            pos = nxt_pos

        return self.nodes[pos].exist > 0

    def delete_num(self, x: int) -> bool:

        if not self.find_num(x):
            return False
        pos = 0

        for i in range(self.height, -1, -1):

            c = (x >> i) & 1

            nxt_pos = self.nodes[pos].child[c]

            if nxt_pos == -1:
                return True
            nxt_node = self.nodes[nxt_pos]

            if nxt_node.cnt == -1:
                self.nodes[pos].child[c] = -1
            pos = nxt_pos

        self.nodes[pos].exist -= 1

        return True


class TemporaryNode:
    def __init__(self, ll: BinaryNode | None, lr: BinaryNode | None, rl: BinaryNode | None, rr: BinaryNode | None,
                 par_h: int):
        self.ll: BinaryNode | None = ll
        self.lr: BinaryNode | None = lr
        self.rl: BinaryNode | None = rl
        self.rr: BinaryNode | None = rr
        self.par_h: int = par_h


class BitwiseXorSolution(BinaryTrie):

    def __init__(self, arr: List[int], x: int):
        super(BitwiseXorSolution, self).__init__()
        self.arr: List[int] = arr
        self.x: int = x

    def build(self):

        for num in self.arr:
            self.add_num(num)

    def solve(self) -> int:
        return self.calc_set(0, self.height)

    def calc_set(self, cur_pos: int, h: int) -> int:

        if cur_pos == -1:
            return 0

        if h == 0:
            return 1

        cur_node = self.nodes[cur_pos]

        nxt_bit = (self.x >> (h-1)) & 1

        if nxt_bit == 1:
            return self.count_elem(cur_pos, h)

        nxt_pos_l, nxt_pos_r = cur_node.child

        p_left = self.calc_set(nxt_pos_l, h - 1)
        p_right = self.calc_set(nxt_pos_r, h - 1)

        res = p_left + p_right + p_left * p_right

        return res

    def count_elem(self, cur_pos: int, h: int) -> int:

        if cur_pos == -1:
            return 0
        if h < 0:
            return 0

        cur_bit = (self.x >> h) & 1

        if cur_bit == 0:
            return 0

        tmp_node = self.decay_node(cur_pos, h)

        return self.numbers_valid(tmp_node)

    def decay_node(self, cur_pos: int, h: int) -> TemporaryNode:

        ll, lr, rl, rr = None, None, None, None

        cur_node = self.nodes[cur_pos]

        if cur_node.child[0] != -1:
            left_node = self.nodes[cur_node.child[0]]
            if left_node.child[0] != -1:
                ll = self.nodes[left_node.child[0]]
            if left_node.child[1] != -1:
                lr = self.nodes[left_node.child[1]]

        if cur_node.child[1] != -1:
            right_node = self.nodes[cur_node.child[0]]
            if right_node.child[0] != -1:
                ll = self.nodes[right_node.child[0]]
            if right_node.child[1] != -1:
                lr = self.nodes[right_node.child[1]]

        return TemporaryNode(ll, lr, rl, rr, h)

    def split_node(self, left_node, right_node, h: int) -> TemporaryNode:

        ll, lr, rl, rr = None, None, None, None

        if left_node and left_node.child[0] != -1:
            ll = self.nodes[left_node.child[0]]
        if left_node and left_node.child[1] != -1:
            lr = self.nodes[left_node.child[1]]
        if right_node and right_node.child[0] != -1:
            rl = self.nodes[right_node.child[0]]
        if right_node and right_node.child[1] != -1:
            rr = self.nodes[right_node.child[1]]

        return TemporaryNode(ll, lr, rl, rr, h)

    def numbers_valid(self, p: TemporaryNode) -> int:

        if p.par_h == 0:
            return 0

        h = p.par_h - 1

        cur_bit = (self.x >> h) & 1

        f_p = self.split_node(p.ll, p.rr, h)
        l_p = self.split_node(p.lr, p.rl, h)

        if cur_bit == 1:
            return self.numbers_valid(f_p) + self.numbers_valid(l_p)

        num_left = 0
        num_right = 0

        if p.ll:
            num_left += p.ll.cnt
        if p.lr:
            num_left += p.lr.cnt

        if p.rl:
            num_right += p.rl.cnt

        if p.rr:
            num_right += p.rr.cnt

        res = self.numbers_valid(f_p) + self.numbers_valid(l_p)

        return res + num_left * num_right
