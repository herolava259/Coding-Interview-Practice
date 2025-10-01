from typing import List, Optional, Tuple, Deque
from collections import deque

"""
Given N of lines has function y = a{i} * x + b{i} and magnitude number Q of queries
condition 0 <= i < N
Each query include some values of x

What minimum of y respect with x in N given lines 
"""



class Line:
    a: float
    b: float
    def __init__(self, a: float, b: float, coeff_y: 0|1 = 0):
        self.a: float = a
        self.b: float = b
        self.tan_alpha = self.a if coeff_y else float('inf')
        self.coeff_y = coeff_y

    def value_of(self, x: float) -> float:
        return self.a * x + self.b if self.coeff_y else float('inf')

    def intersect_with(self, other: Optional['Line']) -> Tuple[float, float]:

        if self.a == other.a or self.coeff_y == other.coeff_y == 0:
            return float('inf'), float('inf')

        x = (other.b - self.b) / (self.a - other.a)

        return x, self.value_of(x)

class Passage(Line):
    def __init__(self, a: float, b: float, lower_bound: Tuple[float, float] = (float('-inf'),float('-inf')), upper_bound: Tuple[float, float] = (float('inf'),float('inf'))):
        super().__init__(a, b)
        self.lower_bound: Tuple[float, float] = lower_bound
        self.upper_bound: Tuple[float, float] = upper_bound


class ConvexHull:
    def __init__(self):
        self.n = 0
        self.passages: List[Passage] = []
        self.ranges: List[Tuple[float, Passage]] = []

    def build(self, lines: List[Line]):
        self.passages = build_convex_hull_from(lines)
        self.n = len(self.passages)
        for p in self.passages:
            self.ranges.append((p.lower_bound[0], p))

    def add_increasing_line(self, a: float | int, b: int | float):

        st = self.passages
        a, b = float(a), float(b)
        p_line, pp_line = st.pop(), st.pop()
        self.ranges.pop()

        if p_line.a == a:
            p_line.b = min(p_line.b, b)
            intersect = p_line.intersect_with(pp_line)
            pp_line.upper_bound = intersect
            p_line.lower_bound = intersect
            self.ranges.append((intersect[0], p_line))
            self.passages.append(pp_line)
            self.passages.append(p_line)
            return

        def retain_line_b(line_a: Passage, line_b: Passage, line_c: Passage) -> bool:
            x_ca, _ = line_c.intersect_with(line_a)
            x_cb, _ = line_c.intersect_with(line_b)
            return x_cb < x_ca

        new_line = Passage(a, b)

        if retain_line_b(pp_line, p_line, new_line):
            intersect = new_line.intersect_with(p_line)
            p_line.upper_bound = intersect
            new_line.lower_bound = intersect
            self.passages.extend([pp_line, p_line, new_line])
            self.ranges.extend([(p_line.lower_bound[0], p_line), (new_line.lower_bound[0], new_line)])
            self.n+=1
            return

        intersect = new_line.intersect_with(pp_line)
        pp_line.upper_bound = intersect
        new_line.upper_bound = intersect
        self.passages.extend([pp_line, new_line])
        self.ranges.append((new_line.lower_bound[0], new_line))


    def search_range_in(self, x: float) -> Passage:

        low, high = 0, len(self.passages) - 1

        while low < high:
            mid = ((low + high) >> 1) + ((low+high) & 1)

            lower_x, p = self.ranges[mid]
            if lower_x > x:
                high = mid -1
            else:
                low = mid
        return self.passages[low]



def build_convex_hull_from(lines: List[Line]) -> List[Passage]:

    lines = [line for line in lines if line.coeff_y]

    lines.sort(key=lambda c: c.a)

    if not lines:
        return []

    def distinct_by_a(line_arr: List[Line]) -> List[Line]:
        uniques: List[Line] = []

        cur_line = line_arr[0]

        for line in line_arr[0:]:
            if line.a != cur_line.a:
                uniques.append(cur_line)
                continue
            if line.b < cur_line.b:
                cur_line = line
        uniques.append(cur_line)
        return uniques

    unique_lines = distinct_by_a(lines)

    if len(unique_lines) <= 1:
        return [Passage(unique_lines[0].a, unique_lines[0].b)]

    st: Deque[Line] = deque()

    st.append(unique_lines[0])
    st.append(unique_lines[1])

    for line in unique_lines[2:]:
        p_line, pp_line = st.pop(), st.pop()

        x32, _ = line.intersect_with(p_line)
        x31, _ = line.intersect_with(pp_line)
        st.append(pp_line)
        if x32 < x31:
            st.append(p_line)
        st.append(line)


    convex_hull: List[Passage] = [Passage(line.a, line.b) for line in st]
    n = len(convex_hull)
    for i in range(1, n):
        prev_p, cur_p = convex_hull[i-1], convex_hull[i]

        intersect = prev_p.intersect_with(cur_p)
        prev_p.upper_bound = intersect
        cur_p.lower_bound = intersect
    return convex_hull



class QueryInNLinesSolution:
    def __init__(self, lines: List[Line]):

        self.lines: List[Line] = lines

    def naive_retrieve(self, x: float) -> float:

        return min([line.value_of(x) for line in self.lines])

    def bs_retrieve(self, x: float) -> float:

        convex_hull = ConvexHull()
        convex_hull.build(self.lines)

        p = convex_hull.search_range_in(x)
        return p.value_of(x)
