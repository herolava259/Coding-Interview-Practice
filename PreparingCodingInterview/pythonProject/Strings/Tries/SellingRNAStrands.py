from typing import List


class PrefixNode:
    def __init__(self):
        self.left: int = 0
        self.right: int = 0
        self.child: List[PrefixNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class PrefixTrie:

    def __init__(self, arr: List[str]):

        self.root: PrefixNode = PrefixNode()
        self.arr: List[str] = arr
        self.n = len(arr)

    def add_chain(self, chain: str, idx: int):

        cur_node = self.root

        for c in chain:
            offset: int = ord(c) - ord('a')
            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                nxt_node = PrefixNode()
                cur_node.child[offset] = nxt_node
                nxt_node.left = idx

            nxt_node.right = idx
            nxt_node.cnt += 1
            cur_node = nxt_node

        cur_node.exist += 1

    def build(self):
        for idx, x in enumerate(self.arr):
            self.add_chain(x, idx)

    def find_chain(self, x: str) -> PrefixNode | None:

        cur_node = self.root

        for c in x:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return None
            cur_node = nxt_node

        return cur_node


class SuffixNode:
    def __init__(self):
        self.suffix_of: List[int] = []
        self.childs: List[SuffixNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class SuffixTrie:

    def __init__(self, arr: List[str]):
        self.arr: List[str] = arr
        self.root: SuffixNode = SuffixNode()
        self.n = len(arr)

    def add_chain(self, x: str, idx: int):

        cur_node = self.root

        for c in x:
            offset = ord(c) - ord('a')
            nxt_node = cur_node.childs[offset]

            if nxt_node is None:
                nxt_node = SuffixNode()
                cur_node.childs[offset] = nxt_node

            nxt_node.suffix_of.append(idx)
            nxt_node.cnt += 1

        cur_node.exist += 1

    def build(self):
        for idx, c in enumerate(self.arr):
            self.add_chain(c, idx)

    def find_chain(self, x: str) -> SuffixNode | None:

        cur_node = self.root

        for c in x:

            offset = ord(c) - ord('a')

            nxt_node: SuffixNode = cur_node.childs[offset]

            if nxt_node is None:
                return None

            cur_node: SuffixNode = nxt_node

        return cur_node


class SellingRNAStrandSolution:
    def __init__(self, arr: List[str]):
        self.arr = arr
        self.sorted_arr = sorted(arr)
        self.prefix_trie = PrefixTrie(self.sorted_arr)
        self.suffix_trie = SuffixTrie([invert_s for invert_s in self.sorted_arr])

    def build(self):
        self.prefix_trie.build()
        self.suffix_trie.build()

    def query(self, p: str, q: str) -> int:
        prefix_node = self.prefix_trie.find_chain(p)
        suffix_node = self.suffix_trie.find_chain(q)

        if prefix_node is None or suffix_node is None:
            return -1

        first, last = prefix_node.left, prefix_node.right

        first_idx = find_upper_bound(first, suffix_node.suffix_of)
        last_idx = find_lower_bound(last, suffix_node.suffix_of)

        if first_idx == -1 or last_idx == -1 or first_idx > last_idx:
            return -1

        return last_idx - first_idx + 1


def find_upper_bound(x, sorted_arr: List[int]) -> int:
    n = len(sorted_arr)
    first = 0
    last = n - 1

    if x > sorted_arr[-1]:
        return -1

    while first < last:
        mid = (first + last) // 2
        if sorted_arr[mid] >= x:
            first = mid
        else:
            first = mid + 1

    return first


def find_lower_bound(x, sorted_arr: List[int]) -> int:
    n = len(sorted_arr)
    first = 0
    last = n - 1

    if x < sorted_arr[0]:
        return -1

    while first < last:
        mid = (first + last) // 2
        if sorted_arr[mid] >= x:
            last = mid
        else:
            first = mid

    return first
