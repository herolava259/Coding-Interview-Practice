from typing import List, Set


class TrieNode:
    def __init__(self):
        self.child: List[TrieNode | None] = [None for _ in range(26)]
        self.cnt: int = 0
        self.exist: int = 0


class PrefixTrie:
    def __init__(self):

        self.root: TrieNode = TrieNode()

    def add_word(self, word: str):

        cur_node = self.root

        for c in word:

            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                nxt_node = cur_node.child[offset] = TrieNode()

            nxt_node.cnt += 1
            cur_node = nxt_node

        cur_node.exist += 1

    def find_word(self, word: str) -> bool:

        cur_node = self.root

        for c in word:

            offset = ord(c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                return False
            cur_node = nxt_node

        return cur_node.exist > 0


directions: List[tuple] = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class WordSearchIISolution(PrefixTrie):
    def __init__(self, words: List[str], board: List[List[str]]):
        super(WordSearchIISolution, self).__init__()
        self.words: List[str] = words
        self.board: List[List[str]] = board
        self.m_row = len(self.board)
        self.n_col = len(self.board[0])
        self.visited: List[List[bool]] = [[False for _ in range(self.n_col)] for _ in range(self.m_row)]
        self.searched_words: Set[str] = set()

    def backtrack(self, prefix_word: str, cur_node: TrieNode, cur_i: int, cur_j: int):
        if cur_node.exist > 0:
            self.searched_words.add(prefix_word)

        for dir_i, dir_j in directions:

            nxt_i, nxt_j = cur_i + dir_i, cur_j + dir_j

            if not (0 <= nxt_i < self.m_row and 0 <= nxt_j < self.n_col):
                continue
            if self.visited[nxt_i][nxt_j]:
                continue
            nxt_c = self.board[nxt_i][nxt_j]
            offset = ord(nxt_c) - ord('a')

            nxt_node = cur_node.child[offset]

            if nxt_node is None:
                continue

            self.visited[nxt_i][nxt_j] = True
            nxt_prefix_word = prefix_word + nxt_c
            self.backtrack(nxt_prefix_word, nxt_node, nxt_i, nxt_j)
            self.visited[nxt_i][nxt_j] = False

    def initialize(self):

        for w in self.words:
            self.add_word(w)

    def solve(self) -> List[str]:

        for i in range(self.m_row):
            for j in range(self.n_col):

                c = self.board[i][j]

                prefix = c

                offset = ord(c) - ord('a')

                cur_node = self.root.child[offset]

                if cur_node is None:
                    continue

                self.visited[i][j] = True
                self.backtrack(prefix, cur_node, i, j)
                self.visited[i][j] = False

        return list(self.searched_words)


board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]

words1 = ["oath","pea","eat","rain"]

sln = WordSearchIISolution(words1, board1)
sln.initialize()
print(sln.solve())
