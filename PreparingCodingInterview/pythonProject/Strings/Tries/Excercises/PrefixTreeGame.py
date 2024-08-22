from typing import List
from queue import Queue


class PrefixNode:
    def __init__(self):
        self.child: List[PrefixNode | None] = [None for _ in range(26)]
        self.exist: int = 0
        self.cnt: int = 0


class PrefixTree:
    def __init__(self):
        self.cur: int = 0
        self.root = PrefixNode()

    def new_node(self) -> PrefixNode:
        self.cur += 1

        return PrefixNode()

    def add_string(self, s: str):

        cur_node = self.root

        for c in s:

            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                cur_node.child[offset] = nxt_node = self.new_node()
            nxt_node.cnt += 1
            cur_node = nxt_node
        cur_node.exist += 1

    def find_string(self, s: str) -> bool:
        cur_node = self.root

        for c in s:
            offset = ord(c) - ord('a')
            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return False

            cur_node = nxt_node

        return True

    def delete_string(self, s: str) -> bool:

        if not self.find_string(s):
            return False
        cur_node = self.root

        for c in s:
            offset = ord(c) - ord('a')
            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return True
            nxt_node.cnt -= 1
            if nxt_node.cnt <= 0:
                cur_node.child[offset] = None
            cur_node = nxt_node
        cur_node.exist -= 1
        return True


class PrefixTreeGameSolution(PrefixTree):
    def __init__(self, good_strings: List[str], l: int):
        super(PrefixTreeGameSolution, self).__init__()
        self.good_strings: List[str] = good_strings
        self.l: int = l

    def build(self):
        for s in self.good_strings:
            self.add_string(s)

    def find_new_good_string(self) -> str | None:

        cur_node = self.root

        good_str = ''

        q: Queue = Queue()

        q.put((good_str, 0, cur_node))

        while not q.empty():

            good_str, len_s, cur_node = q.get()

            if cur_node is None:
                return good_str
            if len_s + 1 > self.l or cur_node.exist > 0:
                continue
            for i in range(26):
                nxt_node = cur_node.child[i]
                nxt_str = good_str + chr(i + ord('a'))
                q.put((nxt_str, nxt_node))

            return None

    def solve(self) -> str:

        k = 0

        while k < 1000000:
            k += 1

            new_string = self.find_new_good_string()

            if new_string is None:
                break

            self.add_string(new_string)

        return 'Alice' if k % 2 == 1 else 'Bob'
