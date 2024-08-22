from typing import List


class BinaryNode:
    def __init__(self, idx: int = -1):
        self.idx: int = idx
        self.child: List[int] = [-1, -1]
        self.exist: int = 0
        self.cnt: int = 0


class BinaryTrie:
    def __init__(self):
        self.nodes: List[BinaryNode] = [BinaryNode() for _ in range(100_000)]
        self.cur: int = 0

    def new_node(self) -> int:

        self.cur += 1

        new_node: BinaryNode = self.nodes[self.cur]

        new_node.child = [-1, -1]
        new_node.exist = 0
        new_node.cnt = 0

        return self.cur

    def add_num(self, x: int, idx: int):

        pos = 0

        for i in range(31, -1, -1):
            cur_bit = (x >> i) & 1

            cur_node = self.nodes[pos]
            nxt_pos = cur_node.child[cur_bit]

            if nxt_pos == -1:
                nxt_pos = cur_node.child[cur_bit] = self.new_node()

            nxt_node = self.nodes[nxt_pos]

            nxt_node.cnt += 1

            pos = nxt_pos

        self.nodes[pos].exist += 1
        self.nodes[pos].idx = idx

    def find_num(self, x: int) -> bool:

        pos: int = 0

        for i in range(31, -1, -1):

            cur_bit = (x >> i) & 1
            cur_node = self.nodes[pos]

            nxt_pos = cur_node.child[cur_bit]

            if nxt_pos == -1:
                return False
            pos = nxt_pos

        return self.nodes[pos].exist > 0

    def del_num(self, x: int) -> bool:

        if not self.find_num(x):
            return False

        pos = 0

        for i in range(31, -1, -1):

            cur_bit = (x >> i) & 1
            cur_node: BinaryNode = self.nodes[pos]

            nxt_pos = cur_node.child[cur_bit]

            if nxt_pos == -1:
                return True

            nxt_node = self.nodes[nxt_pos]

            nxt_node.cnt -= 1

            if nxt_node.cnt == 0:
                cur_node.child[cur_bit] = -1

            pos = nxt_pos

        self.nodes[pos].exist -= 1

        return True

    def find_xor_max(self, x: int, pos: int, h: int = 32) -> int:

        if h == -1:
            return 0
        cur_node = self.nodes[pos]
        bit_max = 1 ^ ((x >> h) & 1)

        nxt_pos = cur_node.child[bit_max]

        if nxt_pos == -1 or self.nodes[nxt_pos].cnt == 0:
            bit_max = 1 - nxt_pos
            nxt_pos = cur_node.child[bit_max]

        res = self.find_xor_max(x, nxt_pos, h - 1)
        res += bit_max << h

        return res

    def find_max_xor(self, x: int) -> int:

        return self.find_xor_max(x, 0)


class XorSubMatrixSolution:
    def __init__(self, u_arr: List[int], v_arr: List[int]):
        self.m = len(u_arr)
        self.n = len(v_arr)

        self.u: List[int] = u_arr
        self.v: List[int] = v_arr

    def build_sub_u(self) -> (List[int], int):
        res: List[int] = []
        max_xor = 0
        for beg in range(self.m):
            cur_xor = 0
            for i in range(0, self.m - beg):
                cur_xor ^= self.u[beg + i]
                if i % 2 == 0:
                    max_xor = max(max_xor, cur_xor)
                    res.append(cur_xor)

        return res, max_xor

    def build_trie_v(self) -> (BinaryTrie, int):
        trie: BinaryTrie = BinaryTrie()
        max_xor = 0
        for beg in range(self.n):
            cur_xor = 0
            for i in range(0, self.n - beg):
                cur_xor ^= self.v[beg + i]
                if i % 2 == 0:
                    trie.add_num(cur_xor, beg*(beg + i))
                    max_xor = max(cur_xor, max_xor)

        return trie, max_xor

    def solve(self) -> int:

        sub_u, u_max_xor = self.build_sub_u()
        trie_v, v_max_xor = self.build_trie_v()

        max_xor = max(u_max_xor, v_max_xor)

        for xor_e in sub_u:

            partner = trie_v.find_max_xor(xor_e)
            max_xor = max(partner ^ xor_e, max_xor)

        return max_xor

