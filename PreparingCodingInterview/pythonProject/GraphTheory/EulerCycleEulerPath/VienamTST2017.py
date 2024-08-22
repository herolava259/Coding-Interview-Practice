from typing import List


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Edge:
    def __init__(self, x: int, y: int, u: int, v: int, ids: int, fake: bool = False):
        self.source = Point(x, y)
        self.target = Point(u, v)

        self.id = ids
        self.fake = fake


max_size = 1002


class Graph:

    def __init__(self):
        super.__init__(self)
        self.edges: int = 0
        self.graph: List[List[List[Edge]]] = []
        for i in range(max_size * 2):
            self.graph.append([[] for _ in range(max_size * 2)])

    def __len__(self):
        return len(self.graph)

    def __getitem__(self, item):
        return self.graph[item]

    def add_edge(self, x: int, y: int, u: int, v: int, fake: bool = False):
        self.graph[x][y].append(Edge(x, y, u, v, self.edges, fake))
        self.edges += 1

    def add_fake_edges(self):
        for i in range(max_size * 2):
            for j in range(max_size * 2):
                if len(self.graph[i][j]) % 2 == 1:
                    self.add_edge(i, j, 0, 0, True)

    def add_line(self, x1: int, y1: int, x2: int, y2: int):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        if x1 == x2:
            for i in range(y1, y2, 1):
                self.add_edge(max_size + x1, max_size + i, max_size + x2, max_size + i + 1)
        else:
            for i in range(x1, x2, 1):
                self.add_edge(max_size + i, max_size + y1, max_size + i + 1, max_size + y2)


class TST2017Solution:
    def __init__(self, n: int, lines: List[tuple]):
        self.n = n
        self.g = Graph()

        for line in lines:
            x, y, u, v = line
            self.g.add_line(x, y, u, v)

        self.g.add_fake_edges()

        self.avail = [True for _ in range(self.g.edges)]
        self.ans: List[List[Point]] = []

    def euler_walk(self, u: Point) -> List[Edge]:

        ans: List[Edge] = []
        curr: Point = u
        while len(self.g[curr.x][curr.y]) != 0:
            e: Edge = self.g[u.x][u.y].pop()

            if not self.avail[e.id]:
                continue
            self.avail[e.id] = False
            ans.append(e)
            curr = e.target

        it: int = len(ans) - 1

        for i in range(it, -1, -1):
            sub_cycle = self.euler_walk(ans[i].source)
            ans = ans[:i + 1] + sub_cycle + ans[i + 1:]

        return ans

    def solve(self) -> List[List[Point]]:

        for i in range(max_size * 2):
            for j in range(max_size * 2):
                if len(self.g[i][j]) == 0:
                    continue

                cycle: List[Edge] = self.euler_walk(Point(i, j))

                stroke: List[Point] = []

                for edge in cycle:
                    if edge.fake:
                        if len(stroke) != 0:
                            self.ans.append(stroke)
                            stroke.clear()
                    else:
                        if len(stroke) == 0:
                            stroke.append(edge.source)

                        stroke.append(edge.target)

                if len(stroke) != 0:
                    self.ans.append(stroke)

        return self.ans
