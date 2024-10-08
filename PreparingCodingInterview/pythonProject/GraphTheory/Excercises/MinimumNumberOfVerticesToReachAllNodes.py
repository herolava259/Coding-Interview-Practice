from typing import List


class FindSmallestSetOfVerticesSolution:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n: int = n
        self.edges: List[List[int]] = edges

    def solve(self) -> List[int]:
        in_deg_vertices: List[int] = [0] * self.n

        for u, v in self.edges:
            in_deg_vertices[v] += 1

        return list(filter(lambda c: in_deg_vertices[c] == 0, range(self.n)))


n1 = 6
edges1 = [[0,1],[0,2],[2,5],[3,4],[4,2]]

sln = FindSmallestSetOfVerticesSolution(n1, edges1)

print(sln.solve())
