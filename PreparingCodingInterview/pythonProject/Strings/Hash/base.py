from typing import List


class RollingHashSolver:
    def __init__(self, max_n: int, mod: int, base: int):
        self.max_n = max_n
        self.pow = [0] * max_n
        self.hash_t = [0] * max_n
        self.mod = mod
        self.base = base

    def _get_hash_t(self, i: int, j: int) -> int:

        return (self.hash_t[j] - self.hash_t[i-1] * self.pow[j-i+1] + self.mod**2) % self.mod

    def initialize(self):

        self.pow[0] = 1

        for i in range(1, self.max_n):
            self.pow[i] = (self.pow[i-1] * self.base) % self.mod

    def find(self, txt: str, pattern: str)-> List[int]:

        m, n = len(txt), len(pattern)

        txt = ' ' + txt
        pattern = ' ' + pattern

        for i in range(1, m+1):
            self.hash_t[i] = (self.hash_t[i-1] * self.base + ord(txt[i]) - ord('a') + 1) % self.mod

        hash_p = 0
        for i in range(1, n+1):
            hash_p = (hash_p* self.base + ord(pattern[i]) - ord('a') + 1) % self.mod

        return [i for i in range(1, m-n+2) if hash_p == self._get_hash_t(i, i+ n - 1)]


