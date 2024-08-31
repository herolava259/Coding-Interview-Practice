from typing import List, Tuple
from collections import Counter


class TwoStringAreCloseSolution:
    def __init__(self, word1: str, word2: str):
        self.word1: str = word1
        self.word2: str = word2

    def solve(self) -> bool:
        if len(self.word1) != len(self.word2):
            return False

        freq1: Counter = Counter(self.word1)
        freq2: Counter = Counter(self.word2)

        sort_freq1: List[Tuple[str, int]] = list(freq1.items())
        sort_freq2: List[Tuple[str, int]] = list(freq2.items())

        sort_freq1.sort(key=lambda c: c[1])
        sort_freq2.sort(key=lambda c: c[1])

        if len(sort_freq1) != len(sort_freq2):
            return False

        n = len(freq1)

        for i in range(n):
            c1, c2 = sort_freq1[i][0], sort_freq2[i][0]
            f1, f2 = sort_freq1[i][1], sort_freq2[i][1]
            if c1 == c2 and f1 == f2:
                continue

            if f1 != f2:
                return False

            # c1 != c2
            # apply operation 2

            j = i + 1

            while j < n and sort_freq1[j][0] != c2:
                j += 1

            if j == n:
                return False

            sort_freq1[i] = (c2, f1)
            sort_freq1[j] = (c1, sort_freq1[j][1])

        return True


word1 = "cabbba"
word2 = "abbccc"

sln = TwoStringAreCloseSolution(word1, word2)

print(sln.solve())
