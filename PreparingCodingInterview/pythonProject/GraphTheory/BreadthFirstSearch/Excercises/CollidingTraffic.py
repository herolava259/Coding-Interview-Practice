from typing import List
from collections import deque


def get_speed(speed, direction) -> tuple:
    if direction == 0:
        return 0, speed
    elif direction == 90:
        return speed, 0
    elif direction == 180:
        return 0, -speed
    elif direction == 270:
        return -speed, 0
    else:
        return 0, speed


class BoatObject:
    def __init__(self, x: float, y: float, direction: int, speed: float):
        self.x: float = x
        self.y: float = y
        self.direction: int = direction
        self.speed: float = speed
        self.speed_x, self.speed_y = get_speed(speed, direction)

    def position_at(self, time: int) -> tuple:
        return self.x + self.speed_x * time, self.y + self.speed_y * time


def square_distance_between(b1: BoatObject, b2: BoatObject, time: int) -> float:
    p1_x, p1_y = b1.position_at(time)
    p2_x, p2_y = b2.position_at(time)

    return (p1_x - p2_x) ** 2 + (p1_y - p2_y) ** 2


class CollidingTrafficSolution:
    def __init__(self, n: int, r: float, boats: List[BoatObject]):
        self.n = n
        self.r = r
        self.boats: List[BoatObject] = boats

    def bfs_solve(self) -> int:

        dq: deque = deque()

        r_square = self.r ** 2

        time = 0

        idx1, idx2 = 0, 1

        dq.append((idx1, idx2, 0))

        n = len(self.boats)
        mark_times = [[-1 for _ in range(n)] for _ in range(n)]
        mark_times[idx1][idx2] = 0
        curr_d_sq: List[List[float]] = [[100_000_007.0 for _ in range(n)] for _ in range(n)]
        dist_sq = -1.0
        while dq:

            idx1, idx2, time = dq.popleft()
            dist_sq = square_distance_between(self.boats[idx1], self.boats[idx2], time)

            if dist_sq <= r_square:
                break

            if idx1 + 1 < n and idx1 + 1 < idx2 and time == mark_times[idx1 + 1][idx2] + 1:
                dq.appendleft((idx1 + 1, idx2, time))
                mark_times[idx1 + 1][idx2] = time
            if idx2 + 1 < n and time == mark_times[idx1][idx2 + 1] + 1:
                dq.appendleft((idx1, idx2 + 1, time))
                mark_times[idx1][idx2 + 1] = time

            if dist_sq < curr_d_sq[idx1][idx2]:
                dq.append((idx1, idx2, time + 1))
                curr_d_sq[idx1][idx2] = dist_sq
                mark_times[idx1][idx2] = time + 1

        if dist_sq < r_square:
            return time - 1 if time > 0 else time
        elif dist_sq == r_square:
            return time

        return -1


class CollidingTrafficAdapter:
    def __init__(self, raw_inp: str):

        self.raw_inp = raw_inp

        self.num_test = 0
        self.test_cases: List[(int, int, List[BoatObject])] = []

    def build(self):

        raw_rows = self.raw_inp.split('\n')

        self.num_test = int(raw_rows[0])

        n = len(raw_rows)

        idx = 1

        while idx < n:
            e_row = raw_rows[idx].split(' ')

            num_boat, r_warn = int(e_row[0]), int(e_row[1])

            boats: List[BoatObject] = []
            for i in range(1, num_boat + 1):
                e_row = raw_rows[idx + i].split(' ')
                x, y, d, s = float(e_row[0]), float(e_row[1]), int(e_row[2]), float(e_row[3])
                boats.append(BoatObject(x, y, d, s))

            self.test_cases.append((num_boat, r_warn, boats))

            idx += 1 + num_boat

    def to_solution(self, fn):

        solution = []

        for test_case in self.test_cases:
            solution.append(fn(test_case[0], test_case[1], test_case[2]))

        return solution


raw_inp = '''2
2 5
0 0 90 1
10 10 180 1
2 10
0 0 0 0
8 8 270 1'''


def build_solution(n: int, r: float, boats: List[BoatObject]):
    return CollidingTrafficSolution(n, r, boats)


adp = CollidingTrafficAdapter(raw_inp)

adp.build()

solutions: List[CollidingTrafficSolution] = adp.to_solution(build_solution)

print(solutions[0].bfs_solve())

print(solutions[1].bfs_solve())
