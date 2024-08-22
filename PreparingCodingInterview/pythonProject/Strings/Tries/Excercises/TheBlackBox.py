from typing import List, DefaultDict
from collections import defaultdict
import heapq


class BinaryNode:
    def __init__(self):
        self.child: List[int] = [-1, -1]
        self.cnt: int = 0
        self.exist: int = 0


class BinaryTrie:
    def __init__(self):
        self.nodes: List[BinaryNode | None] = [None for _ in range(2000)]
        self.height: int = 32
        self.cur: int = 0

    def new_node(self) -> int:

        self.cur += 1
        new_node = self.nodes[self.cur]
        new_node.child = [-1, -1]
        new_node.cnt = 0
        new_node.exist = 0
        return self.cur

    def add_num(self, x: int):

        pos: int = 0

        for i in range(self.height - 1, -1, -1):

            cur_bit = (x >> i) & 1
            cur_node = self.nodes[pos]
            nxt_pos = cur_node.child[cur_bit]

            if nxt_pos == -1:
                nxt_pos = cur_node.child[cur_bit] = self.new_node()
            nxt_node = self.nodes[nxt_pos]

            nxt_node.cnt += 1

            pos = nxt_pos

        self.nodes[pos].exist += 1

    def find_num(self, x: int) -> bool:

        pos = 0

        for i in range(self.height - 1, -1, -1):

            cur_bit = (x >> i) & 1

            cur_node = self.nodes[pos]

            nxt_pos = cur_node.child[cur_bit]

            if nxt_pos == -1:
                return False

            pos = nxt_pos
        return True

    def delete_num(self, x: int) -> bool:

        if not self.find_num(x):
            return False

        pos = 0

        for i in range(self.height - 1, -1, -1):
            cur_bit = (x >> i) & 1

            cur_node: BinaryNode = self.nodes[pos]
            nxt_pos = cur_node.child[cur_bit]

            if nxt_pos == -1:
                return True
            nxt_node = self.nodes[nxt_pos]

            nxt_node.cnt -= 1

            if nxt_node.cnt <= 0:
                cur_node.child[cur_bit] = -1

            pos = nxt_pos

        self.nodes[pos].exist -= 1

        return True


class BlackBoxCommand:
    def __init__(self, cmd_type: str, val: int):
        self.cmd_type: str = cmd_type
        self.val: int = val if val >= 0 else -val

    def is_add(self) -> bool:
        return self.cmd_type == 'add'

    def is_del(self) -> bool:
        return self.cmd_type == 'del'


class TheBlackBoxSolution:

    def __init__(self):
        self.arr: List[int] = [0]
        self.basis: List[List[int]] = [[]]
        self.map_value: DefaultDict[int, int] = defaultdict(int)

    def query(self, x: int) -> int:
        if x < 0:
            self.arr.append(0)
            idx_x = self.map_value[-x]
            prev_idx = idx_x - 1 if idx_x > 0 else 0
            cur_basis = self.basis[prev_idx]

            for e in self.arr[idx_x + 1:]:
                if e > 0:
                    cur_basis = add_to_basis(cur_basis, e)
            self.map_value[0] = len(self.arr) - 1
            self.basis.append(cur_basis)
            return find_xor_max(basis=cur_basis)

        self.arr.append(x)
        self.map_value[x] = len(self.arr) - 1
        cur_basis = self.basis[-1]
        cur_basis = add_to_basis(cur_basis, x)
        self.basis.append(cur_basis)

        return find_xor_max(cur_basis)


class MaxHeap:
    def __init__(self, arr: List[int]):
        self.arr = [-e for e in sorted(arr, reverse=True)]

    def push(self, x: int):
        heapq.heappush(self.arr, -x)

    def pop(self) -> int:
        return -heapq.heappop(self.arr)

    def peek(self) -> int:
        return -self.arr[0] if self.arr else 0

    def to_list(self) -> List[int]:
        res = []

        while self.arr:
            res.append(-heapq.heappop(self.arr))

        return res

    def empty(self) -> bool:
        return len(self.arr) == 0


def generate_basis(arr: List[int]) -> List[int]:
    q: MaxHeap = MaxHeap(arr)

    basis: List[int] = []
    for i in range(64, 0, -1):

        need_nor = []

        if q.empty():
            break
        if (q.peek() >> i) & 1 == 0:
            continue
        best_elem = q.pop()
        basis.append(best_elem)
        while not q.empty() and ((q.peek() >> i) & 1 == 1):
            need_nor.append(q.pop())

        for elem in need_nor:
            new_elem = elem ^ best_elem
            q.push(new_elem)
    idx = 0

    res = q.to_list()
    n = len(res)
    while idx < n and res[idx] == 0:
        idx += 1
    return res[idx:]


def first_bit_one_pos(x):
    i = 63

    while i >= 0 and (x >> i) & 1 == 0:
        i -= 1

    return i


def add_to_basis(basis: List[int], x: int) -> List[int]:
    cur = x
    idx = 0
    n = len(basis)
    for i in range(63, -1, -1):
        bit_i = (cur >> i) & 1

        if bit_i == 0:
            continue

        while idx < n and first_bit_one_pos(basis[idx]) > i:
            idx += 1

        if idx >= n or first_bit_one_pos(basis[idx]) < i:
            break

        cur_basis = basis[idx]

        if cur > cur_basis:
            basis[idx] = cur
            cur, cur_basis = cur_basis, cur
        elif cur == cur_basis:
            cur = 0
            break
        cur = cur_basis ^ cur
        idx += 1
    if cur > 0:
        basis.insert(idx, cur)

    return basis


def find_xor_max(basis: List[int]) -> int:
    res = basis[0]
    for e in basis[1:]:
        if e ^ res > res:
            res = e ^ res
    return res
