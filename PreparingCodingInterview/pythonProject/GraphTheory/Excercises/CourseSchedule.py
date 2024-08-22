from typing import List


def find_no_to_edge(num_to_edge: List[int], finished: List[bool]) -> int:

    n = len(num_to_edge)
    for idx in range(n):
        if finished[idx]:
            continue
        if num_to_edge[idx] == 0:
            return idx

    return -1


class TopoSortSolution:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.edges = edges
        self.adj_from: List[List[int]] | None = None
        self.adj_to: List[List[int]] | None = None

    def build(self):
        self.adj_from = [[] for _ in range(self.n)]
        self.adj_to = [[] for _ in range(self.n)]

        for edge in self.edges:
            a, b = edge
            self.adj_to[a].append(b)
            self.adj_from[b].append(a)

    def can_sort(self) -> bool:

        finished = [False for _ in range(self.n)]

        num_to_edge = [len(adj) for adj in self.adj_to]

        counter = 0

        while True:
            if counter == self.n:
                break
            node = find_no_to_edge(num_to_edge, finished)
            if node == -1:
                return False
            finished[node] = True
            counter += 1
            for to_node in self.adj_from[node]:
                num_to_edge[to_node] -= 1

        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        topo_sort_sln = TopoSortSolution(numCourses, prerequisites)

        topo_sort_sln.build()

        return topo_sort_sln.can_sort()

sln = Solution()

n1 = 2
p1 = [[1,0]]

print(sln.canFinish(n1, p1))

n2 = 2
p2 = [[1,0],[0,1]]

print(sln.canFinish(n2, p2))
