from typing import List


class GenericUnionFindSolution:

    def __init__(self, x):
        self.x = x

    def find_circle_num(self, M: List[List[int]]):

        def find(node, par):
            if par[node] == self.x:
                return node
            par[node] = find(par[node], par)
            return par[node]

        def union(a, b, par, rank1):
            a_rep, b_rep = find(a, par), find(b, par)

            if rank1[a] == rank1[b]:
                par[a_rep] = b_rep
                rank1[a] += 1
            elif rank1[a] > rank1[b]:
                par[a_rep] = b_rep
            else:
                par[b_rep] = a_rep

        s, V = set(), len(M)
        parent = [x for x in range(V)]
        rank = [1 for i in range(V)]

        for i in range(V):
            s.add(find(i, parent))

        return len(s)
