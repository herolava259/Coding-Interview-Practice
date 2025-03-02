from typing import List, Annotated, Optional

class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def less_than(self, other: Optional['Point']) -> bool:
        return self.x < other.x

def interpolate(p: Point, q: Point, x: int) -> int:

    if p.y == q.y:
        return p.y

    diff = p.y - q.y

    y = min(p.y, q.y)

    l = x - p.x
    r = q.x - x

    if l == 0:
        return p.y
    if r == 0:
        return q.y

    if diff < 0:
        y -= (l * diff) // (l+r)
    else:
        y += (r * diff) // (l+r)

    return y

class GoldMiningSolution:
    def __init__(self, n: int, m: int, k: int, event_i: List[int],
                 event_j: List[int], event_di: List[int], event_dj: List[int]):

        self.n: int = n
        self.m: int = m
        self.k: int = k

        self.event_i: List[int] = event_i
        self.event_j: List[int] = event_j

        self.event_di: List[int] = event_di
        self.event_dj: List[int] = event_dj


    def solve(self) -> int:

        hull: List[Point] = []

        def inc_const(delta: int):
            for i in range(len(hull)):
                hull[i].y += delta

        def expand(delta: int):

            l, r = 0, 0

            for i in range(len(hull)):
                if hull[i].y > hull[l].y:
                    l = r = i
                elif hull[i].y == hull[l].y:
                    r = i

            if l == r:
                hull.insert(l + 1, hull[l])
                r += 1

            for i in range(l+1):
                hull[i].x += delta

            for i in range(r, len(hull)):
                hull[i].x += delta

        def evaluate(x: int):
            for i in range(len(hull)-1):
                if hull[i].x <= x <= hull[i+1].x:
                    return interpolate(hull[i], hull[i + 1], x)


        def merge_hull(v: int):
            exist: int = -1

            for i in range(len(hull)):
                if hull[i].x == v:
                    exist = i
                    break

            if exist == -1:
                hull.append(Point(v, evaluate(v)))
                hull.sort(key=lambda c: c.x)

            for i in range(len(hull)):
                hull[i].y -= abs(hull[i].x - v)


        def solve_with_dimension(length: int, pos: List[int], limit: List[int]) -> int:

            hull.clear()

            n: int = len(pos)

            hull.append(Point(0, length - pos[0]))

            if pos[0] != 0:
                hull.append(Point(pos[0], length))

            if pos[0] != length:
                hull.append(Point(length, length - abs(pos[0] - length)))

            for i in range(1, n):
                expand(limit[i-1])
                merge_hull(pos[i])
                inc_const(length)

            ans: int = 0
            last: int = 0

            for x in range(length+1):
                while last < len(hull) and hull[last].x <= x:
                    last += 1
                if last == len(hull):
                    last -= 1

                ans = max(ans, interpolate(hull[last - 1], hull[last], x))

            return ans

        return (solve_with_dimension(self.n, self.event_i, self.event_di)
                + solve_with_dimension(self.m, self.event_j, self.event_dj))




