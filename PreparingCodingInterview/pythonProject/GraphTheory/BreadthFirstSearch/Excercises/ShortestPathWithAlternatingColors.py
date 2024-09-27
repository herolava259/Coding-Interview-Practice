from typing import List, Deque, Tuple
from collections import deque


class ShortestPathWithAlternatingColors:
    def __init__(self, n: int, red_edges: List[List[int]]
                 , blue_edges: List[List[int]]):
        self.n: int = n
        self.red_edges: List[List[int]] = red_edges
        self.blue_edges: List[List[int]] = blue_edges

    def solve(self) -> List[int]:

        shortest_paths: List[int] = [-1] * self.n

        red_g: List[List[int]] = build_directed_graph_from_edge(self.red_edges, self.n)
        blue_g: List[List[int]] = build_directed_graph_from_edge(self.blue_edges, self.n)

        visited_red: List[bool] = [False] * self.n
        visited_blue: List[bool] = [False] * self.n

        q: Deque[Tuple[int, int, bool]] = deque()

        if red_g[0]:
            q.append((0, 0, False))
        if blue_g[0]:
            q.append((0, 0, True))

        visited_red[0] = True
        visited_blue[0] = True
        shortest_paths[0] = 0

        while q:
            u, num_path, prev_color = q.popleft()
            visited = visited_red
            g = red_g

            # case: red edge come to u
            if prev_color:
                visited = visited_blue
                g = blue_g

            for v in g[u]:
                if visited[v]:
                    continue

                if shortest_paths[v] == -1:
                    shortest_paths[v] = num_path + 1
                elif shortest_paths[v] > num_path + 1:
                    shortest_paths[v] = num_path + 1

                visited[v] = True
                q.append((v, num_path + 1, not prev_color))

        return shortest_paths


def build_directed_graph_from_edge(edges: List[List[int]], n: int):
    g: List[List[int]] = [[] for _ in range(n)]

    for u, v in edges:
        g[u].append(v)

    return g


n1 = 3
redEdges1 = [[0,1]]
blueEdges1 = [[2,1]]
sln = ShortestPathWithAlternatingColors(n1, redEdges1, blueEdges1)

print(sln.solve())
