from typing import List


class PrefixNode:
    def __init__(self):
        self.child: List[PrefixNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class PrefixTrie:

    def __init__(self):

        self.root: PrefixNode = PrefixNode()

    def add_chain(self, chain: str):

        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')
            nxt_node = cur_node.child[offset]

            if not nxt_node:
                nxt_node = cur_node.child[offset] = PrefixNode()

            nxt_node.cnt += 1

            cur_node = nxt_node

        cur_node.exist += 1

    def find_chain(self, chain: str) -> bool:

        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if not nxt_node or nxt_node.cnt == 0:
                return False
            cur_node = nxt_node

        return cur_node.exist > 0

    def remove_chain(self, chain: str) -> bool:

        if not self.find_chain(chain):
            return False

        cur_node = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if not nxt_node:
                return True
            nxt_node.cnt -= 1
            if nxt_node.cnt <= 0:
                cur_node.child[offset] = None
            cur_node = nxt_node

        cur_node.exist -= 1

        return True


class SearchSuggestionsSystemSolution(PrefixTrie):

    def __init__(self, products: List[str], search_word: str):
        super(SearchSuggestionsSystemSolution, self).__init__()

        self.products: List[str] = products
        self.search_word: str = search_word

    def initialize(self):
        for p_name in self.products:
            self.add_chain(p_name)

    def find_chains_of_prefix(self, root_node: PrefixNode, num_of_retrieve: int = 3, prefix: str = '') -> List[str]:

        # init ds of result: List[str]
        res: List[str] = []

        # add some chain with end of this node
        cur_retrieve = min(num_of_retrieve, root_node.exist)
        res.extend([prefix] * cur_retrieve)
        num_of_retrieve -= cur_retrieve

        for i in range(26):
            if num_of_retrieve <= 0:
                break
            nxt_c = chr(ord('a') + i)
            nxt_node = root_node.child[i]
            if not nxt_node:
                continue

            cur_retrieve = min(nxt_node.cnt, num_of_retrieve)
            num_of_retrieve -= cur_retrieve
            res.extend(self.find_chains_of_prefix(nxt_node, cur_retrieve, prefix + nxt_c))
        return res

    def solve(self) -> List[List[str]]:
        self.initialize()

        prefix = ''
        res: List[List[str]] = []
        cur_node = self.root

        for i in range(len(self.search_word)):
            c = self.search_word[i]
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if not nxt_node or nxt_node.cnt <= 0:
                res.extend([[] for _ in range(len(self.search_word) - i)])
                break
            prefix += c
            res[i] = self.find_chains_of_prefix(nxt_node, 3, prefix)
            cur_node = nxt_node

        return res


product1: List[str] = ["havana"]

searchWord1 = "havana"

sln = SearchSuggestionsSystemSolution(product1, searchWord1)

print(sln.solve())

