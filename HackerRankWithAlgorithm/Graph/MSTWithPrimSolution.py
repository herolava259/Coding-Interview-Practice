from collections import defaultdict
from typing import List
import heapq
from DisjoinSet import Edge

max_value = 100000000


class PrimSolution:

    @staticmethod
    def solve(graph: List[List[tuple]], num_vertex: int) -> (int, List[Edge]):

        priority_queue, s = [], 0

        heapq.heappush(priority_queue, (s, s, 0))

        dis_arr = [max_value for _ in range(num_vertex)]
        visited = [False for _ in range(num_vertex)]

        mst, total_weight = [], 0
        while priority_queue:

            u, v, dis = heapq.heappop(priority_queue)

            curr_dis = dis_arr[u]

            if curr_dis != dis and u != 0 and v != 0:
                continue
            total_weight += dis
            visited[v] = True
            if u != 0 or v != 0:
                mst.push(Edge(u, v, dis))

            for (v, c) in graph[u]:
                if dis_arr[v] > c and not visited[v]:
                    dis_arr[v] = c
                    heapq.heappush(priority_queue, (u, v, dis_arr[v]), key=lambda x: x[1])

        return total_weight, mst
