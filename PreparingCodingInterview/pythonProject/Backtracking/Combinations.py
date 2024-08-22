from typing import List


class CombinationsSolution:
    def __init__(self, n: int, k: int):
        self.n: int = n
        self.k: int = k
        self.visited: List[bool] = [False for _ in range(self.n + 1)]
        self.results: List[List[int]] = []

    def solve(self) -> List[List[int]]:
        if self.k == 0:
            return []
        self.backtrack(1, 1)

        return self.results

    def backtrack(self, k: int, beg: int):
        if k == self.k + 1:
            result = []

            for i in range(1, self.n+1):
                if self.visited[i]:
                    result.append(i)
            self.results.append(result)
            return

        for i in range(beg, self.n+1):

            if not self.visited[i]:
                self.visited[i] = True
                self.backtrack(k+1, i+1)
                self.visited[i] = False
