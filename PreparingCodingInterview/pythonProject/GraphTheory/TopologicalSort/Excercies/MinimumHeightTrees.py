from typing import List, Set, Deque as Queue
from collections import deque as queue


class MinimumHeightTreeSolution:
    def __init__(self, n: int, edges: List[List[int]]):

        self.n: int = n
        self.edges: List[List[int]] = edges

    def solve(self) -> List[int]:

        g: List[List[int]] = [[] for _ in range(self.n)]

        if self.n == 2:
            return list(range(2))

        for u_node, v_node in self.edges:
            g[u_node].append(v_node)
            g[v_node].append(u_node)

        h: List[int] = [0] * self.n
        central_child: List[List[int]] = [[] for _ in range(self.n)]
        secondary_len: List[int] = [0] * self.n

        def dfs_construct(u: int, p: int = -1) -> int:

            for v in g[u]:
                if v == p:
                    continue
                length_v = dfs_construct(v, u)
                if length_v + 1 > h[u]:
                    central_child[u] = [v]
                    secondary_len[u], h[u] = h[u], length_v + 1
                elif length_v + 1 == h[u]:
                    central_child[u].append(v)

            return h[u]

        ans: List[int] = []
        min_h: int = 10**9 + 7
        def dfs_crack(u: int, outer_length: int = 0):

            outer_length = max(outer_length, secondary_len[u])
            if not central_child[u]:
                return
            nonlocal min_h
            sample_child = central_child[u][0]
            h[u] = max(h[sample_child]+1, outer_length)

            if h[u] == min_h:
                ans.append(u)
            elif h[u] < min_h:
                min_h = h[u]
                ans.clear()
                ans.append(u)
            if outer_length == h[u]:
                return

            if len(central_child[u]) > 1:
                return

            dfs_crack(sample_child, outer_length+1)

        root = 0
        dfs_construct(root)
        dfs_crack(root)

        return list(ans)

    def topo_solve(self) -> List[int]:

        deg: List[int] = [0] * self.n
        g: List[Set[int]] = [set() for _ in range(self.n)]
        const_g: List[List[int]] =[[] for _ in range(self.n)]
        for u_node, v_node in self.edges:
            deg[u_node] += 1
            deg[v_node] += 1
            g[u_node].add(v_node)
            g[v_node].add(u_node)

            const_g[u_node].append(v_node)
            const_g[v_node].append(u_node)

        one_queue: Queue[int] = queue()

        for u in range(self.n):
            if deg[u] == 1:
                one_queue.append(u)

        centroid: List[int] = [-1] * self.n
        h: List[int] = [0] * self.n
        secondary_h: List[int] = [0] * self.n
        root = 0
        while one_queue:
            root = u = one_queue.popleft()
            if not g[u]:
                continue
            v = g[u].pop()

            if h[u]+1 > h[v]:
                centroid[v] = u
                secondary_h[v] = h[v]
                h[v] = h[u] + 1
            elif h[u] + 1 == h[v]:
                centroid[v] = -1

            deg[v] -= 1
            g[v].remove(u)
            if deg[v] == 1:
                one_queue.append(v)
        cur_u = root
        outer_h = 0
        min_h = 10**9 + 7
        ans: List[int] = []
        while cur_u != -1:
            cur_v = centroid[cur_u]

            h[cur_u] = max(outer_h, h[cur_u])

            if h[cur_u] < min_h:
                ans = [cur_u]
                min_h = h[cur_u]
            elif h[cur_u] == min_h:
                ans.append(cur_u)

            outer_h = max(secondary_h[cur_u], outer_h) + 1
            if cur_v == -1 or outer_h > min_h:
                break

            cur_u = cur_v
        return ans


n1, edges1 = 6, [[3,0],[3,1],[3,2],[3,4],[5,4]]

sln = MinimumHeightTreeSolution(n1, edges1)


print(sln.solve())

print(sln.topo_solve())

