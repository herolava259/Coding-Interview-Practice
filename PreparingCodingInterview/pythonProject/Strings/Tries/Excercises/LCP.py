from typing import List


class PrefixNode:
    def __init__(self):
        self.child: List[PrefixNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class PrefixTrie:
    def __init__(self):

        self.root = PrefixNode()

    def add_string(self, chain: str):

        cur_node = self.root

        for c in chain:

            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]
            if nxt_node is None:
                nxt_node = cur_node.child[offset] = PrefixNode()

            nxt_node.cnt += 1

            cur_node = nxt_node
        cur_node.exist += 1

    def find_string(self, chain) -> bool:
        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return False

            cur_node = nxt_node

        return cur_node.exist > 0

    def remove_string(self, chain: str):

        if not self.find_string(chain):
            return False

        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return True
            nxt_node.cnt -= 1

            if nxt_node.cnt == 0:
                cur_node.child[offset] = None
            cur_node = nxt_node

        cur_node.exist -= 1
        return True


class LCPSolution(PrefixTrie):
    def __init__(self, arr: List[str]):
        super(LCPSolution, self).__init__()
        self.arr: List[str] = arr
        self.n: int = len(arr)

    def initialize(self):

        for s in self.arr:
            self.add_string(s)

    def solve(self) -> str:

        cur_node = self.root
        prefix_s = ''

        while cur_node is not None:
            child_node: PrefixNode | None = None
            for i in range(26):
                nxt_node = cur_node.child[i]
                if nxt_node is None:
                    continue
                nxt_c = chr(ord('a') + i)
                if nxt_node.cnt < self.n:
                    return prefix_s
                prefix_s += nxt_c
                child_node = nxt_node
            cur_node = child_node

        return prefix_s


strs1 = ["flower", "flow", "flight"]

sln = LCPSolution(strs1)
sln.initialize()

print(sln.solve())
