from typing import List


class CanVisitAllRoomsSolution:
    def __init__(self, rooms: List[List[int]]):

        self.rooms: List[List[int]] = rooms
        self.n = len(rooms)
        self.visited: List[bool] = [False] * self.n

    def solve(self) -> bool:
        self.dfs_solve(0)

        return all(self.visited)

    def dfs_solve(self, u: int, p: int = -1):

        self.visited[u] = True

        for v in self.rooms[u]:
            if v == p or self.visited[v]:
                continue
            self.dfs_solve(v, u)
