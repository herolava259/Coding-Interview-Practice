from typing import List
from queue import Queue


class NaughtyCowsSolution:

    def __init__(self, n: int, g: List[List[int]]):
        self.n: int = n
        self.g: List[List[int]] = g
        self.marks: List[bool] = [False for _ in range(self.n + 1)]

    def bfs_marks(self, u: int) -> List[int]:

        q: Queue = Queue()

        q.put(u)
        self.marks[u] = True
        cows: List[int] = [u]
        while not q.empty():
            cur_cow = q.get()

            for near_cow in self.g[cur_cow]:
                if self.marks[near_cow]:
                    continue
                self.marks[near_cow] = True
                cows.append(near_cow)
                q.put(near_cow)

        return cows

    def solve(self) -> List[int]:

        self.bfs_marks(1)
        naughty_cows: List[int] = []
        for u in range(2, self.n + 1):
            if not self.marks[u]:
                naughty_cows.extend(self.bfs_marks(u))

        return naughty_cows
