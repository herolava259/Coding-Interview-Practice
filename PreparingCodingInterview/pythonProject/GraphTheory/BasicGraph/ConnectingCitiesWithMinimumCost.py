import heapq
import collections
from typing import List


class PrimSolution:

    def minimumCost(self, N: int, connections: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        for a, b, w in connections:
            graph[a].append((b, w))
            graph[b].append((a, w))
        visited, cost = set(), 0

        minHeap = [(0, 1)]
        while minHeap:
            minCost, city = heapq.heappop(minHeap)

            if city not in visited:

                cost += minCost
                visited.add(city)
                for nxt, c in graph[city]:
                    if nxt not in visited:
                        heapq.heappush(minHeap, (c, nxt))

        return -1 if len(visited) < N else cost


class KruskalSolution:

    @staticmethod
    def minimum_cost(N: int, connections: List[List[int]]) -> int:

        def find(node, par):
            if par[node] == node:
                return node

            par[node] = find(par(node), par)
            return par[node]

        def union(a, b, par, rank1, a_rep, b_rep):
            if rank1[a] == rank1[b]:
                par[a_rep] = b_rep
                rank1[a] += 1
            elif rank1[a] > rank1[b]:
                par[a_rep] = b_rep
            else:
                par[b_rep] = a_rep

        parent = [x for x in range(N + 1)]
        rank = [1 for i in range(N + 1)]
        res, i, e, result = 0, 0, 0, []
        graph = sorted(connections, key=lambda x: x[2])

        while i < len(graph) and e < N - 1:
            u, v, w = graph[i]
            u_root, v_root = find(u, parent), find(v, parent)
            if u_root != v_root:
                result.append([u, v])
                res += w
                e += 1
                union(u, v, parent, rank, u_root, v_root)
            i += 1
        if len(result) == N - 1:
            return res
        else:
            return -1
