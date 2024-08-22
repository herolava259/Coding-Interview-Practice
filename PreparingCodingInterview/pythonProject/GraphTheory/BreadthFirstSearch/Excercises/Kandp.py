from typing import List, Optional
from collections import defaultdict

knight_move_rules = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

pawn_move_rules = [(-1, 0)]


class Piece:
    def __init__(self, pos_x: int, pos_y: int, moves: List[tuple]):

        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.moves: List[tuple] = moves

    def move(self):
        for move in self.moves:
            yield Piece(self.pos_x + move[0], self.pos_y + move[1], self.moves)

    def overlapped_with(self, other_piece: Optional['Piece']) -> bool:
        if other_piece is None:
            return True
        return self.pos_x == other_piece.pos_x and self.pos_y == other_piece.pos_y

    def norm_one_with(self, other: Optional['Piece']) -> int:
        if other is None:
            return -1

        return abs_diff(self.pos_x, other.pos_x) + abs_diff(self.pos_y, other.pos_y)

    def move_closer_with(self, other: Optional['Piece']):

        origin_dis = self.norm_one_with(other)

        if origin_dis == -1:
            return None

        for move in self.moves:
            new_x, new_y = self.pos_x + move[0], self.pos_y + move[1]

            new_dis = abs_diff(new_x, other.pos_x) + abs_diff(new_y, other.pos_y)

            if new_dis <= origin_dis:
                yield Piece(new_x, new_y, self.moves)

    def pos_str(self) -> str:
        return f'{self.pos_x}-{self.pos_y}'


class ItemQ:
    def __init__(self, pawn: Piece, knight: Piece, weight: int):
        self.pawn: Piece = pawn
        self.knight: Piece = knight
        self.weight: int = weight

    def get(self) -> (Piece, Piece, int):

        return self.pawn, self.knight, self.weight


class TwoQueue:
    def __init__(self):

        self.q_first: List[ItemQ] = []
        self.q_last: List[ItemQ] = []
        self.curr_move = 0

    def enqueue(self, item: ItemQ):

        if item.weight > self.curr_move:
            self.q_last.append(item)
        else:
            self.q_first.append(item)

    def up_move(self):
        self.q_first, self.q_last = self.q_last, self.q_first
        self.curr_move += 1

    def dequeue(self) -> ItemQ:
        if not self.q_first:
            self.up_move()
        return self.q_first.pop(0)

    def empty(self) -> bool:
        return len(self.q_first) == 0 and len(self.q_last) == 0


def abs_diff(a: int, b: int):
    return a - b if a >= b else b - a


class KandpSolution:
    def __init__(self, pawn_pos: tuple, knight_pos: tuple):
        self.pawn_x: int = pawn_pos[0]
        self.pawn_y: int = pawn_pos[0]

        self.knight_x: int = knight_pos[0]
        self.knight_y: int = knight_pos[1]

    def solve(self) -> (bool, int):

        curr_pawn: Piece = Piece(self.pawn_x, self.pawn_y, pawn_move_rules)
        curr_knight: Piece = Piece(self.knight_x, self.knight_y, knight_move_rules)

        visited: defaultdict = defaultdict(bool)

        limit_pos = 100_000_000

        limit_move = 100_000_00
        q: TwoQueue = TwoQueue()

        visited[f'{curr_knight.pos_x}-{curr_knight.pos_y}'] = True
        q.enqueue(ItemQ(curr_pawn, curr_knight, 0))

        while not q.empty():

            curr_pawn, curr_knight, num_move = q.dequeue().get()

            if curr_knight.overlapped_with(curr_pawn):
                return True, num_move

            if num_move > limit_move:
                continue

            new_pawn: Piece = next(curr_pawn.move())

            for new_knight in curr_knight.move():

                if visited[new_knight.pos_str()]:
                    continue
                visited[new_knight.pos_str()] = True

                new_dis_cur = new_knight.norm_one_with(curr_pawn)
                new_dis_new = new_knight.norm_one_with(new_pawn)

                if new_dis_cur < limit_pos:
                    q.enqueue(ItemQ(new_pawn, new_knight, num_move + 1))

                if new_dis_new < limit_pos:
                    q.enqueue(ItemQ(new_pawn, new_knight, num_move + 2))

        return False, -1
