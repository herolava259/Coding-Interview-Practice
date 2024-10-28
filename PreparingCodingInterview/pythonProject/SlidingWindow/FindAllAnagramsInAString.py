from collections import Counter
from typing import Dict, List


def check_same_distribution(d1: Dict[str, int], d2: Dict[str, int]):
    keys = set(d1.keys()).union(d2.keys())

    for k in keys:
        if d1.get(k, 0) != d2.get(k, 0):
            return False

    return True


class FindingAnagramsSolution:

    def __init__(self, s: str, p: str):
        self.s: str = s
        self.p: str = p

    def solve(self) -> List[int]:
        len_p = len(self.p)
        len_s = len(self.s)

        freq_p = dict(Counter(self.p))

        freq_win = dict(Counter(self.s[:len_p]))
        results: List[int] = []
        if check_same_distribution(freq_p, freq_win):
            results.append(0)

        for i in range(1, len_s - len_p+1):
            freq_win[self.s[i - 1]] -= 1
            freq_win[self.s[i + len_p - 1]] = freq_win.get(self.s[i + len_p - 1], 0) + 1

            if check_same_distribution(freq_win, freq_p):
                results.append(i)

        return results


s1 = "abab"
p1 = "ab"

sln = FindingAnagramsSolution(s1, p1)

print(sln.solve())
