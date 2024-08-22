from typing import List


class KnuthMorrisPrattSolution:
    def __init__(self, t: List[str], p: List[str]):
        self.t: List[str] = t
        self.p: List[str] = p

    def compute_prefix_p(self) -> List[int]:

        pi = [0]

        len_p = len(self.p)
        k = 0
        for q in range(1, len_p):
            while k > 0 and self.p[k + 1] != self.p[q]:
                k = pi[k]
            if self.p[k + 1] == self.p[q]:
                k += 1
                pi.append(k)
            else:
                pi.append(-1)

        return pi

    def solve(self) -> List[int]:

        pi = self.compute_prefix_p()

        q = 0

        len_t = len(self.t)
        len_p = len(self.p)

        res = []

        for i in range(len_t):

            while q > 0 and self.p[q + 1] != self.t[i]:
                q = pi[q]

            if self.p[q + 1] == self.t[i]:
                q += 1
            if q == len_p - 1:
                res.append(i)
                q = pi[q]

        return res
