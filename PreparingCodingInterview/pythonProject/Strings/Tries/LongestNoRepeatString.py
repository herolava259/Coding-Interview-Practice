from typing import List
from collections import defaultdict


class LongestNoRepeatStringSolution:
    def __init__(self, s: str):
        self.s: str = s

    def solve(self) -> int:
        max_len = 1

        last_idx: defaultdict = defaultdict(lambda: -1)

        prev_len = 1
        last_idx[self.s[0]] = 0
        n = len(self.s)
        for i in range(1, n):

            c = self.s[i]

            if c == self.s[i - 1]:
                prev_len = 1
                last_idx[c] = i
                continue

            if last_idx[c] < i - prev_len:
                prev_len += 1
                max_len = max(prev_len, max_len)
                last_idx[c] = i
                continue

            prev_len = i - last_idx[c]
            max_len = max(prev_len, max_len)
            last_idx[c] = i

        return max_len


s1 = 'AAAAAAAA' #'ABCCDFHHIKJLPP'

sln = LongestNoRepeatStringSolution(s1)

print(sln.solve())
