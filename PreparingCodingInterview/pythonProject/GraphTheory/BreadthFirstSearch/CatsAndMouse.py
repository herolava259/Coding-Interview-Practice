from typing import List, Optional
from queue import Queue


class Position:
    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y

    def overlapped_with(self, other: Optional['Position']) -> bool:
        return self.pos_x == other.pos_x and other.pos_y == self.pos_y

    def closer_with(self, other: Optional['Position']):

        if self.pos_x > other.pos_x:
            yield Position(self.pos_x - 1, self.pos_y)
        elif self.pos_x < other.pos_x:
            yield Position(self.pos_x + 1, self.pos_y)

        if self.pos_y > other.pos_y:
            yield Position(self.pos_x, self.pos_y - 1)
        elif self.pos_y < other.pos_y:
            yield Position(self.pos_x, self.pos_y + 1)

    def move(self, offset_x: int, offset_y: int) -> Optional['Position']:
        return Position(self.pos_x + offset_x, self.pos_y + offset_y)


moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class UnitOfWork:

    def __init__(self, mouse_pos: Position, cats_pos: List[Position], size_row: int, size_col: int):
        self.mouse_pos: Position = mouse_pos
        self.cats_pos: List[Position] = cats_pos
        self.size_row: int = size_row
        self.size_col: int = size_col

    def cats_catch_up_mouse(self) -> bool:
        for cat_pos in self.cats_pos:
            if self.mouse_pos.overlapped_with(cat_pos):
                return True

        return False

    def mouse_escape_from_cats(self) -> bool:

        return self.mouse_pos.pos_y >= self.size_col or self.mouse_pos.pos_x >= self.size_row \
               or self.mouse_pos.pos_x < 0 or self.mouse_pos.pos_y < 0

    def choose_cat_pos(self, cat_id: int, num_cat: int) -> List[List[Position]]:

        if cat_id == num_cat:
            return [[]]

        perm_cd_pos = self.choose_cat_pos(cat_id + 1, num_cat)
        res: List[List[Position]] = []

        for cd_pos in self.cats_pos[cat_id].closer_with(self.mouse_pos):
            for perm in perm_cd_pos:
                res.append([cd_pos, *perm])

        return res

    def forward(self, visited: List[List[bool]]):

        new_cat_pos_cd = self.choose_cat_pos(0, len(self.cats_pos))

        for move in moves:

            new_mouse_pos = self.mouse_pos.move(move[0], move[1])
            if visited[new_mouse_pos.pos_x][new_mouse_pos.pos_y]:
                continue
            visited[new_mouse_pos.pos_x][new_mouse_pos.pos_y] = True
            for new_cats_pos in new_cat_pos_cd:
                yield UnitOfWork(new_mouse_pos, new_cats_pos, self.size_row, self.size_col)


class CatsAndMouseSolution:

    def __init__(self, size_row: int, size_col: int, mouse_pos: Position, cats_pos: List[Position]):

        self.size_row: int = size_row
        self.size_col: int = size_col
        self.mouse_pos: Position = mouse_pos
        self.cats_pos: List[Position] = cats_pos

    def bfs_solve(self) -> bool:

        visited: List[List[bool]] = [[False for _ in range(self.size_col)] for _ in range(self.size_row)]

        visited[self.mouse_pos.pos_x][self.mouse_pos.pos_y] = True

        q: Queue = Queue()

        q.put(UnitOfWork(self.mouse_pos, self.cats_pos, self.size_row, self.size_col))

        while not q.empty():

            uow: UnitOfWork = q.get()

            if uow.cats_catch_up_mouse():
                continue

            if uow.mouse_escape_from_cats():
                return True

            for new_uow in uow.forward(visited):
                q.put(new_uow)

        return False
