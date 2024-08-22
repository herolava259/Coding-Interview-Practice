from typing import List
from collections import deque

class NKLeagueSolution:

    def __init__(self, n: int, score_board: List[List[int]]):
        self.n: int = n
        self.score_board: List[List[int]] = score_board
        self.g: List[List[int]] = [[] for _ in range(self.n)]
        self.in_degrees: List[int] = [0 for _ in range(self.n)]

    def initialize(self):

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if i == j:
                    continue
                if self.score_board[i][j] == 1:
                    self.g[i].append(j)
                    self.in_degrees[j] += 1
                else:
                    self.g[j].append(i)
                    self.in_degrees[i] += 1

    def solve(self) -> (bool, List[int] | None):
        q : deque = deque()

        for i in range(self.n):
            if self.in_degrees[i] == 0:
                q.append(i)

        counter: List[int] = 0
        orders: List[int] = []
        while q:
            curr_u = q.popleft()
            orders.append(curr_u)
            counter += 1

            for v in self.g[curr_u]:
                self.in_degrees[v] -= 1

                if self.in_degrees[v] <= 0:
                    q.append(v)

        if counter < self.n:
            return False, None
        return True, orders
    