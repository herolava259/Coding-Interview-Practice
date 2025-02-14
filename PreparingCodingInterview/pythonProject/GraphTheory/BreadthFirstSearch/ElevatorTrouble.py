from typing import List
from queue import Queue


class ElevatorTrouble:
    def __init__(self, f: int, s: int, g: int, u: int, d: int):
        self.f: int = f
        self.s: int = s
        self.g: int = g
        self.u: int = u
        self.d: int = d

    def bfs_solve(self) -> (int, List[str]):

        q: Queue = Queue(maxsize=100)

        prev: List[int] = [0 for _ in range(self.f + 1)]
        visited: List[int] = [0 for _ in range(self.f + 1)]
        q.put(self.s)
        path: List[str] = []
        visited[self.s] = True
        curr_level = self.s
        while not q.empty():
            curr_level = q.get()

            if curr_level == self.g:
                break
            level_down = curr_level - self.d
            level_up = curr_level + self.u

            if level_down >= 1 and not visited[level_down]:
                q.put(level_down)
                visited[level_down] = True
                prev[level_down] = curr_level
            if level_up <= self.f and not visited[level_up]:
                q.put(level_up)
                visited[level_up] = True
                prev[level_up] = curr_level

        while curr_level != self.s:
            prev_level = prev[curr_level]

            if prev_level > curr_level:
                path.insert(0, "Down")
            else:
                path.insert(0, "Up")
            curr_level = prev_level

        return len(path), path


f1, s1, g1, u1, d1 = 10, 1, 10, 2, 1

sln1 = ElevatorTrouble(f1, s1, g1, u1, d1)

print(sln1.bfs_solve()[0])
print(sln1.bfs_solve()[1])
