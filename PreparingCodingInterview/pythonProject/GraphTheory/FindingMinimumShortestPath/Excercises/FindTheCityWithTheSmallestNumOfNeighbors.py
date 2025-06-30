from typing import List, Tuple
import heapq

class FindTheCitySolution:
    def __init__(self, n: int, edges: List[List[int]], distanceThreshold: int):

        self.n: int = n
        self.edges: List[List[int]] = edges
        self.distance_threshold = distanceThreshold

    def solve(self):
        return self.dijikstra_solve()
    def dijikstra_solve(self):
        def initialize() -> Tuple[List[List[int]], List[List[Tuple[int, int]]]]:
            mtx: List[List[int]] = [[-1]*self.n for _ in range(self.n)]
            g: List[List[Tuple[int, int]]] = [[] for _ in range(self.n)]

            for uid, vid, w in self.edges:
                g[uid].append((vid, w))
                g[vid].append((uid, w))
                mtx[uid][vid] = w
                mtx[vid][uid] = w
            return mtx, g

        matrix, wg = initialize()

        def dijikstra_single(u: int) -> int:

            h: List[Tuple[int, int]] = []

            d: List[int] = [10**9+7] * self.n

            for vid, w in enumerate(matrix[u]):
                h.append((10 ** 9 + 7 if w==-1 else w, vid))

            heapq.heapify(h)
            visited: List[bool] = [False] * self.n
            visited[u] = True
            num_satisfy = 0
            while h:
                total_w, uid = heapq.heappop(h)

                if visited[uid]:
                    continue
                if total_w > self.distance_threshold:
                    break
                num_satisfy += 1
                visited[uid] = True

                ## loose path
                for vid, w in wg[uid]:
                    if total_w + w < d[vid]:
                        d[vid] = total_w + w
                        heapq.heappush(h, (d[vid], vid))
            return num_satisfy

        record = self.n+1
        best_nid = self.n-1
        for nid in reversed(range(self.n)):

            num_reachable = dijikstra_single(nid)

            if num_reachable < record:
                best_nid = nid
                record = num_reachable

        return best_nid

    def floyd_warshall_solve(self) -> int:

        mtx = [[10**9+7]*self.n for _ in range(self.n)]

        for uid, vid, w in self.edges:
            mtx[uid][vid] = w
            mtx[vid][uid] = w

        dp = [list(mtx[u]) for u in range(self.n)]

        for tmp_nid in range(self.n):
            for uid in range(self.n):
                for vid in range(self.n):
                    if dp[uid][tmp_nid] + dp[tmp_nid][vid] < dp[uid][vid]:
                        dp[uid][vid] = dp[uid][tmp_nid] + dp[tmp_nid][vid]

        num_reachable = [self.n+1] * self.n
        for uid in range(self.n):
            for vid in range(self.n):
                if uid == vid:
                    continue
                if dp[uid][vid] <= self.distance_threshold:
                    num_reachable[uid] += 1

        min_reachable = min(num_reachable)

        for uid in range(self.n-1, -1, -1):
            if num_reachable[uid] == min_reachable:
                return uid
        return 0





n1 = 5
edges1 = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold1 = 2
sln = FindTheCitySolution(n1, edges1, distanceThreshold1)
print(sln.dijikstra_solve())
print(sln.floyd_warshall_solve())



