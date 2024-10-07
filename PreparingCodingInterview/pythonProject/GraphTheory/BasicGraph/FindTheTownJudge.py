from typing import List
from collections import defaultdict


class FindJudgeSolution:
    def __init__(self, n: int, trust: List[List[int]]):
        self.trust: List[List[int]] = trust
        self.n: int = n

    def solve(self) -> int:

        mark_toward: List[bool] = [False] * (self.n + 1)
        mark_toward[0] = True
        trust_labels = defaultdict(set)

        for u, v in self.trust:
            mark_toward[u] = True
            trust_labels[v].add(u)

        for i in range(1, self.n + 1):
            if not mark_toward[i] and len(trust_labels[i]) == self.n - 1:
                return i
        return -1


n1 = 3
trust1 = [[1, 3], [2, 3]]

sln = FindJudgeSolution(n1, trust1)

print(sln.solve())
