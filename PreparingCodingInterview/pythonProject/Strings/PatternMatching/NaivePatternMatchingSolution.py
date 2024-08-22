from typing import List


class NaivePatternMatchingSolution:

    def __init__(self, t: List[str], p: str):
        self.t = t
        self.p = p
        self.len_p = len(p)
        self.len_t = len(t)

    def match(self, idx: int) -> bool:

        for idx_p in range(self.len_p):
            idx_t = idx + idx_p
            if idx_t >= self.len_t:
                return False
            if self.t[idx_t] != self.p[idx_p]:
                return False

        return True

    def enhance_match(self, idx) -> bool:
        for idx_p in range(self.len_p, -1, -1):
            idx_t = idx + idx_p
            if idx_t >= self.len_t:
                return False
            if self.t[idx_t] != self.p[idx_p]:
                return False

        return True
    
    def solve_naive(self) -> List[int]:

        res = []
        for idx in range(self.len_t - self.len_p):

            if self.match(idx):
                res.append(idx)
        return res


