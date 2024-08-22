from collections import deque
from typing import List
from collections import defaultdict


class NKJumpCollectionSolution:
    def __init__(self, value_cycles: List[int]):

        self.n: int = len(value_cycles)
        self.value_cycles: List[int] = value_cycles
        self.out_g: List[set] = [set() for _ in range(self.n)]
        self.in_g: List[set] = [set() for _ in range(self.n)]
        self.in_degrees: List[int] = [0 for _ in range(self.n)]

    def initialize(self):

        map_tb: defaultdict = defaultdict(list)

        for idx, val in enumerate(self.value_cycles):
            map_tb[val].append(idx)

        ordered_values = list(set(self.value_cycles))

        ordered_values.sort()

        n = len(ordered_values)

        for i in range(2, n):
            c = ordered_values[i]
            for j in range(i):
                a = ordered_values[j]
                b = c - a
                idxs_a = map_tb[a]
                idxs_b = map_tb[b]

                if (a == b and len(idxs_a) == 1 ) or not idxs_b:
                    continue
                idxs_in = set(idxs_a + idxs_b)
                idxs_c = map_tb[c]
                for idx_in in idxs_in:
                    for idx_c in idxs_c:
                        self.out_g[idx_in].add(idx_c)
                        self.in_g[idx_c].add(idx_in)
                        self.in_degrees[idx_c] += 1

    def topo_sort(self) -> List[int] | None:

        q: deque = deque()

        for idx, deg in enumerate(self.in_degrees):
            if deg == 0:
                q.append(idx)

        orders: List[int] = []
        counter = 0

        while q:
            u = q.popleft()
            orders.append(u)
            counter += 1

            out_u: set = self.out_g[u]
            for v in out_u:
                self.in_degrees[v] -= 1
                if self.in_degrees[v] == 0:
                    q.append(v)

        if counter < self.n:
            return None

        return orders

    def solve(self) -> List[int] | None:

        self.initialize()
        orders = self.topo_sort()

        if not orders:
            return None

        dp: List[int] = [1 for _ in range(self.n)]
        traces: List[int] = [-1 for _ in range(self.n)]
        max_c = 0
        last_cyc = -1

        # calc max path
        for u in orders:
            max_curr = 0
            prev_v = -1
            for v_in in self.in_g[u]:
                if dp[v_in] >= max_curr:
                    max_curr = dp[v_in]
                    prev_v = v_in

            dp[u] = 1 + max_curr
            traces[u] = prev_v

            if dp[u] >= max_c:
                max_c = dp[u]
                last_cyc = u
        # tracing path
        if last_cyc == -1:
            return None

        curr_cyc = last_cyc
        path = [curr_cyc]
        while traces[curr_cyc] != -1:
            curr_cyc = traces[curr_cyc]
            path.insert(0, curr_cyc)

        return path



