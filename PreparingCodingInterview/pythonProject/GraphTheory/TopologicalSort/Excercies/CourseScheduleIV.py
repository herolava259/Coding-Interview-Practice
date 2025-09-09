from typing import List, Set


class CheckIfPrerequisiteSolution:
    def __init__(self, num_courses: int, prerequisites: List[List[int]],
                    queries: List[List[int]]):
        self.n = num_courses
        self.edges: List[List[int]] = prerequisites
        self.queries: List[List[int]] = queries

    def solve_by_dfs(self) -> List[bool]:
        visited: List[bool] = [False] * self.n
        descendant: List[Set[int]] = [set() for _ in range(self.n)]
        topo_order: List[int] = []

        def generate_graph() -> List[List[int]]:
            graph: List[List[int]] = [[] for _ in range(self.n)]

            for uid, vid in self.edges:
                graph[uid].append(vid)

            return graph

        g: List[List[int]] = generate_graph()


        def dfs_topo(uid: int):
            visited[uid] = True

            for vid in g[uid]:
                if visited[vid]:
                    continue
                dfs_topo(vid)

            topo_order.append(uid)

        def dfs_tracing(uid: int):

            visited[uid] = True

            for vid in g[uid]:
                descendant[uid].add(vid)
                if not visited[vid]:
                    dfs_tracing(vid)

                descendant[uid] |= descendant[vid]

        for u in range(self.n):
            if not visited[u]:
                dfs_topo(u)
        visited = [False] * self.n

        for u in topo_order:
            if not visited[u]:
                dfs_tracing(u)

        return [v in descendant[u] for u,v in self.queries]


numCourses = 7
prerequisites = [[2,3],[2,1],[2,0],[3,4],[3,6],[5,1],[5,0],[1,4],[1,0],[4,0],[0,6]]
queries = [[3,0]]

print(CheckIfPrerequisiteSolution(numCourses, prerequisites, queries).solve_by_dfs())


    