from typing import List, DefaultDict, Deque, Tuple
from collections import defaultdict, deque


class TrieNode:
    def __init__(self):
        self.child: List[TrieNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, chain: str):
        cur_node: TrieNode = self.root

        for c in chain:
            offset = ord(c) - ord('a')
            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                nxt_node = cur_node.child[offset] = TrieNode()
            nxt_node.cnt += 1
            cur_node = nxt_node

        cur_node.exist += 1

    def find_word(self, chain: str) -> bool:

        cur_node: TrieNode = self.root

        for c in chain:
            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return False
            cur_node = nxt_node

        return cur_node.exist > 0


class WordLadderSolution:

    def __init__(self, begin_word: str, end_word: str, word_list: List[str]):

        self.begin_word: str = begin_word
        self.end_word: str = end_word
        self.word_list: List[str] = word_list

    def build_neighbors_tb(self) -> (DefaultDict[str, List[str]], PrefixTrie):
        neigbors: DefaultDict[str, List[str]] = defaultdict(list)
        # build neighbor table
        trie = PrefixTrie()

        for w in self.word_list:
            trie.add_word(w)

        char_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        len_word = len(self.word_list[0])
        for w in self.word_list:

            for i in range(len_word):
                for c in char_alphabet:
                    if w[i] == c:
                        continue
                    new_w = w[:i] + c + w[i + 1:]
                    if trie.find_word(new_w):
                        neigbors[w].append(new_w)

        return neigbors, trie

    def solve(self) -> int:

        neigbors, trie = self.build_neighbors_tb()

        visited: DefaultDict[str, bool] = defaultdict(bool)

        q: Deque[Tuple[int, str]] = deque()

        len_word = len(self.begin_word)
        char_alphabet = 'abcdefghijklmnopqrstuvwxyz'

        if self.begin_word == self.end_word:
            return 0

        for i in range(len_word):

            for c in char_alphabet:
                if c == self.begin_word[i]:
                    continue

                new_w = self.begin_word[:i] + c + self.begin_word[i + 1:]

                if trie.find_word(new_w):
                    visited[new_w] = True
                    q.append((2, new_w))
        visited[self.begin_word] = True
        while q:
            num_step, cur_w = q.popleft()
            if cur_w == self.end_word:
                return num_step
            for nxt_w in neigbors[cur_w]:
                if visited[nxt_w]:
                    continue
                visited[nxt_w] = True
                q.append((num_step + 1, nxt_w))

        return 0


begin_word1 = "hit"
end_word1 = "cog"
word_list1 = ["hot","dot","dog","lot","log","cog"]

sln = WordLadderSolution(begin_word1, end_word1, word_list1)

print(sln.solve())