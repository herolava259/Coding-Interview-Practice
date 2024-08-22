from typing import List


class TrieNode:
    def __init__(self):
        self.child: List[TrieNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

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

    def delete_string(self, chain: str) -> bool:

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


class WorkBreakSolution(PrefixTrie):

    def __init__(self, s: str, word_dict: List[str]):
        super(WorkBreakSolution, self).__init__()
        self.s: str = s
        self.word_dict: List[str] = word_dict

    def build(self):

        for word in self.word_dict:
            self.add_string(word)

    def solve(self) -> bool:

        prefix_nodes: List[TrieNode | None] = [None for _ in range(21)]
        is_done: bool = True

        len_s = len(self.s)
        completed = [False for _ in range(len_s + 1)]
        prefix_nodes[0] = self.root

        for idx, c in enumerate(self.s):
            offset = ord(c) - ord('a')
            new_done = False

            for i in range(2, 0, -1):
                if prefix_nodes[i] is None:
                    continue

                cur_node = prefix_nodes[i]
                nxt_node = cur_node.child[offset]

                if nxt_node is not None and nxt_node.exist > 0 and (idx < i + 1 or completed[idx - i - 1]):
                    new_done = True

                prefix_nodes[i + 1] = nxt_node

            if c == 't':
                pass
            if is_done:
                prefix_nodes[1] = prefix_nodes[0].child[offset]

                if prefix_nodes[1] and prefix_nodes[1].exist > 0 and (idx < 1 or completed[idx - 1]):
                    new_done = True
            else:
                prefix_nodes[1] = None
            completed[idx] = is_done = new_done

        return is_done

s1 = 'leetcode'
wordDict1 = ["leet","code"]

s2 = 'applepenapple'
wordDict2 = ["apple","pen"]

s3 = 'catsandog'
wordDict3 = ["cats","dog","sand","and","cat"]

s4 = 'ab'
wordDict4 = ['a', 'b']

sln = WorkBreakSolution(s4, wordDict4)



sln.build()

print(sln.solve())