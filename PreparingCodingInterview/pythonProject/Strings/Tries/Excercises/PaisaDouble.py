from typing import List


class TrieNode:
    def __init__(self):
        self.child: List[TrieNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class PrefixTrie:
    def __init__(self):

        self.root: TrieNode = TrieNode()

    def add_string(self, chain: str):

        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                nxt_node = cur_node.child[offset] = TrieNode()

            nxt_node.cnt += 1
            cur_node = nxt_node

        cur_node.exist += 1

    def find_string(self, chain: str) -> bool:

        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return False

            cur_node = nxt_node

        return cur_node.exist > 0

    def remove_string(self, chain: str) -> bool:

        if not self.find_string(chain):
            return False

        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return False
            nxt_node.cnt -= 1

            if nxt_node.cnt == 0:
                cur_node.child[offset] = None

            cur_node = nxt_node
        cur_node.exist -= 1
        return True


class Result:
    def __init__(self, pos: int, res: bool):
        self.pos: int = pos
        self.res: str = 'Yes' if res else 'No'

    def to_string(self):
        return f'X = {self.pos}: {self.res}'


class PaisaDoubleSolution(PrefixTrie):

    def __init__(self, p_arr: List[str], k: int, exist_chars: List[int], s: str):

        super(PaisaDoubleSolution, self).__init__()

        self.p_arr: List[str] = p_arr
        self.k: int = k
        self.exist_chars = exist_chars
        self.s: str = s
        self.avail = set()

        for i in range(len(exist_chars)):
            if exist_chars[i] == 1:
                self.avail.add(i)

    def initialize(self):

        for p in self.p_arr:
            self.add_string(p)

    def count_less(self) -> (int, TrieNode):

        cur_node = self.root
        num_less_equal = 0

        for c in self.s[:-1]:

            offset = ord(c) - ord('a')
            nxt_node = cur_node.child[offset]

            for i in range(offset):
                child_node = cur_node.child[i]
                if child_node is not None:
                    num_less_equal += child_node.cnt

            if nxt_node is None:
                break
            cur_node = nxt_node
        return num_less_equal, cur_node.child[ord(self.s[-1]) - ord('a')]

    def solve(self) -> List[Result]:

        res: List[Result | None] = [None for _ in range(self.k + 1)]

        num_less, cur_node = self.count_less()

        for i in range(num_less):
            res[i] = Result(i, False)

        res[num_less] = Result(num_less, True)

        cur_exist = cur_node.exist

        for i in range(num_less + 1, num_less + cur_exist + 1):
            res[i] = Result(i, False)
        num_less += cur_exist
        remain_less = self.k - num_less

        for i in range(remain_less):
            exist = self.find_less(cur_node, i)
            res[i + num_less] = Result(i + num_less, exist)

        return res

    def find_less(self, cur_node: TrieNode, num_less: int = 0) -> bool:

        if cur_node.cnt < num_less:
            return False

        cur = 0
        i = 0
        while i < 26 and cur < num_less:
            child_node = cur_node.child[i]

            if child_node is not None:
                cur += child_node.cnt

            i += 1

        if i >= 26:
            return False

        while i < 25 and i not in self.avail:
            i += 1
            child_node = cur_node.child[i]

            if child_node is not None:
                return False

        if i not in self.avail:
            return False
        new_num_less = num_less + cur_node.child[i].cnt - cur

        if new_num_less == 0:
            return True

        return self.find_less(cur_node.child[i], new_num_less)
