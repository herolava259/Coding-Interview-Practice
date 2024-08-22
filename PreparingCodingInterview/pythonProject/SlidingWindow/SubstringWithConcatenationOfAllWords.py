from typing import List, DefaultDict
from collections import defaultdict


class WordInConcatenationSolution:

    def __init__(self, s: str, words: List[str]):
        self.s: str = s
        self.words: List[str] = words
        self.n = len(words)
        self.len_s = len(s)

    def solve(self) -> List[int]:

        word_freq: DefaultDict = defaultdict(int)

        for w in self.words:
            word_freq[w] += 1

        k = len(self.words[0])
        concat_idxs = []
        for i in range(k):
            concat_idxs.extend(self.find_sub_str(i, k, word_freq))

        return concat_idxs

    def find_sub_str(self, beg: int, k: int, word_freq: defaultdict) -> List[int]:

        if ((self.len_s - beg) // k) < self.n:
            return []

        map_freq = defaultdict(int)

        i = beg
        res = []

        f = beg
        limit = self.len_s - k
        while i < limit:

            if i == 8:
                pass

            w = self.s[i:i + k]

            if word_freq[w] == 0:
                map_freq = defaultdict(int)
                i += k
                f = i
                continue

            if map_freq[w] + 1 > word_freq[w]:
                j = f
                cur_w = self.s[j: j + k]
                while j < i and cur_w != w:
                    map_freq[cur_w] -= 1
                    j += k
                    cur_w = self.s[j: j + k]
                f = j + k
            else:
                map_freq[w] += 1

            if (i - f) // k + 1 == self.n:
                res.append(f)
            i += k
        return res


s1 = "wordgoodgoodgoodbestword"
words1 = ["word","good","best","good"]

sln = WordInConcatenationSolution(s1, words1)

print(sln.solve())
