from typing import List, DefaultDict as SparseTable
from collections import defaultdict


class ValidArrangementSolution:

    def __init__(self, pairs: List[List[int]]):
        self.pairs: List[List[int]] = pairs


    def solve(self) -> List[List[int]]:

        g_out: SparseTable[int, List[int]] = defaultdict(list)

        deg: SparseTable[int, int] = defaultdict(int)

        for u, v in self.pairs:
            g_out[u].append(v)

            deg[u] += 1
            deg[v] -= 1

        st = -1

        for v in deg.keys():
            if st == -1:
                st= v
            if deg[v] == 1:
                st = v
                break

        def euler_walk(uid: int) -> List[int]:

            cur_u = uid
            path: List[int] = [uid]
            while g_out[cur_u]:

                cur_v = g_out[cur_u].pop()

                path.append(cur_v)

                cur_u = cur_v

            n_path = len(path)

            for p in range(n_path, -1, -1):

                entry = path[p-1]

                if not g_out[entry]:
                    continue

                sub_circuit = euler_walk(entry)

                path = path[:p] + sub_circuit + path[p:]

            return path
        result = euler_walk(st)
        return [[result[i], result[i+1]] for i in range(len(result)-1)]