from typing import List, DefaultDict as SparseTable
from collections import defaultdict


class CrackingTheSafeSolution:
    def __init__(self, n: int, k: int):
        self.n: int = n
        self.k: int = k

    def solve(self) -> str:

        if self.n==1:
            return ''.join([str(i) for i in range(self.k)])

        def adj_nodes(cur_chain: str, k: int) -> List[str]:

            postfix: str = cur_chain[1:]

            return [postfix + str(digit) for digit in range(k)]

        def near_sequence(cur_chain: str, k: int, n: int) -> str:

            p = n - 1
            max_char = str(k-1)
            while p >= 0 and cur_chain[p] == max_char:
                p -= 1

            if p < 0:
                return cur_chain
            return cur_chain[:p] + str(int(cur_chain[p]) + 1) + '0'*(n-p-1)


        def build_debruijn_graph(k: int, n:int) -> SparseTable[str, List[str]]:

            cur_seq = '0' * n
            last_seq = str(k-1) * n

            graph: SparseTable[str, List[str]] = defaultdict(list)
            graph[cur_seq].extend(adj_nodes(cur_seq, k))
            while cur_seq != last_seq:
                nxt_seq:str = near_sequence(cur_seq, k, n)
                adj_seq:List[str] = adj_nodes(nxt_seq, k)

                graph[nxt_seq].extend(adj_seq)

                cur_seq = nxt_seq

            return graph

        g: SparseTable[str, List[str]] = build_debruijn_graph(self.k, self.n-1)

        def euler_walk(cur_chain: str) -> List[str]:
            cur_u = cur_chain
            path: List[str] = [cur_u]
            while g[cur_u]:
                cur_v = g[cur_u].pop()
                path.append(cur_v)
                cur_u = cur_v

            n_path = len(path)

            for p in range(n_path, 0, -1):

                entry = path[p-1]
                if not g[entry]:
                    continue

                sub_circuit = euler_walk(entry)[1:]
                path = path[:p] + sub_circuit + path[p:]

            return path

        raw_result = euler_walk('0'*(self.n-1))
        crack_chain = raw_result[0]

        for chain in raw_result[1:]:
            crack_chain += chain[-1]

        return crack_chain

n1 = 3
k1 = 2

sln = CrackingTheSafeSolution(n1, k1)

print(sln.solve())