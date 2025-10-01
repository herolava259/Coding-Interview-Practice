from typing import List, Tuple
from ..base.InitialTrickyProblem import ConvexHull


class SubGroupSolution:

    def __init__(self,n: int, hs: List[int], ws: List[int]):

        self.n: int = n
        self.hs: List[int] = hs
        self.ws: List[int] = ws


    def solve(self) -> int:

        rectangles: List[Tuple[int, int]] = [(wi, hi) for wi, hi in zip(self.hs, self.ws)]

        rectangles = sorted(rectangles)

        filtered_rectangles: List[Tuple[int, int]] = [rectangles[0]]

        p_w, p_h = rectangles[0]

        for c_w, c_h in rectangles[1:]:

            while filtered_rectangles and p_w <= c_w and p_h <= c_h:
                filtered_rectangles.pop()

                if filtered_rectangles:
                    p_w, p_h = filtered_rectangles[-1]

            filtered_rectangles.append((c_w, c_h))
            p_w, p_h = c_w, c_h

        cost: List[float] = [float('inf')] * (len(filtered_rectangles) + 1)
        cost[0] = 0

        convex_hull = ConvexHull()
        convex_hull.add_increasing_line(filtered_rectangles[1][0], cost[0])

        n = len(filtered_rectangles)

        for i in range(1, n):
            wi, hi =float(filtered_rectangles[i][0]), float(filtered_rectangles[i][1])
            line = convex_hull.search_range_in(hi)
            cost[i] = line.value_of(hi)
            convex_hull.add_increasing_line(wi, cost[i])

        return int(cost[n])


