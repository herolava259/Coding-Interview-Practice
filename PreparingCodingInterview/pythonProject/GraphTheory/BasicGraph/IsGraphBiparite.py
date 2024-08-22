import collections
from typing import List


class IsBipartiteSolution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        adj_table = collections.defaultdict(list)

        for idx, val in enumerate(graph):
            adj_table[idx] = val
        vis = [-1 for i in range(n)]
        for i in range(n):
            if not vis[i] and adj_table[i]:
                queue = [i]
                vis[i] = 0
                while queue:
                    x = queue.pop(0)
                    for i in adj_table[x]:
                        if vis[i] == -1:
                            vis[i] = 1 - vis[x]
                            queue.append(i)
                        else:
                            if vis[i] == vis[x]:
                                return False

        return True