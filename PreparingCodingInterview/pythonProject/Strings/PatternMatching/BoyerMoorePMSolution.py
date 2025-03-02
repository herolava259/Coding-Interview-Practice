from typing import List, DefaultDict
import string
from collections import defaultdict

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)


class BoyerMooreSolution:

    def __init__(self, t: List[str], p: List[str]):

        self.t: List[str] = t
        self.p: List[str] = p
        self.last: DefaultDict[str, int] = defaultdict(lambda: -1)
        self.len_p = len(p)
        self.len_t = len(t)

    def build(self):

        for idx, c in enumerate(self.p):
            self.last[c] = idx

    def solve(self) -> List[int]:

        cur_idx = 0
        idx_matches = []
        while cur_idx < self.len_t - self.len_p:

            idx = self.len_p - 1

            while idx >= 0 and self.p[idx] == self.t[cur_idx + idx]:
                idx -= 1

            if idx < 0:
                idx_matches.append(cur_idx)
                cur_idx += 1
                continue

            not_match = self.t[cur_idx + idx]

            if self.last[not_match] == -1:
                cur_idx = cur_idx + idx + 1
            elif self.last[not_match] > idx:
                cur_idx += 1
            else:
                cur_idx += idx - self.last[not_match]

        return idx_matches
