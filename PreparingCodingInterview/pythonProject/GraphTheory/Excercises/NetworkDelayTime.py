from collections import defaultdict
import heapq
from typing import List



# Solution : dijkstra algorithm
class DijikstraSolution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        graph = defaultdict(list)
        for i, j, w in times:
            graph[i].append((j, w))
        heap = [(0, K)]
        array = [0] + [float("inf")] * N
        while heap:
            time, ele = heapq.heappop(heap)
            if time < array[ele]:
                array[ele] = time
                for j, w in graph[ele]:
                    heapq.heappush(heap, (time+w,j))

        if max(array) < float("inf"):
            return max(array)
        else:
            return -1


class BellmanFordSolution:
    def __init__(self, times):
        self.times = times

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        array = [0] + [float("inf")] * N
        array[K] = 0
        for node in range(1, N):
            for u, v, w in times:
                if array[u] + w < array[v]:
                    array[v] = array[u] + w

        if max(array) < float("inf"):
            return max(array)
        else:
            return -1


class FloydWarshallSolution:
    @staticmethod
    def network_delay_times(times: List[List[int]], N: int, K: int) -> float | int:

        dist : List[List[float | int]] = [[float("inf") for i in range(N)] for j in range(N)]

        for i in range(N):
            dist[i][i] = 0

        for u, v, w in times:
            dist[u-1][v-1] = w

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        if max(dist[K-1]) < float('inf'):
            return max(dist[K-1])
        else:
            return -1


