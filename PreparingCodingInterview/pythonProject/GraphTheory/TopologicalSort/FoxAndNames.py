from typing import List
from collections import deque

class TopologicalSortSolution:

    def __init__(self, n: int, g: List[List[int]]):

        self.n = n
        self.g: List[List[int]] = g
        self.in_degrees: List[int] = [0 for _ in range(self.n + 1)]
        self.orders: List[int] = []

    def initialize(self):

        for u in range(self.n):
            for v in self.g[u]:
                self.in_degrees[v] += 1

    def get_zero_in_degree_nodes(self) -> List[int]:
        res: List[int] = []

        for v in range(self.n):
            if self.in_degrees[v] == 0:
                res.append(v)
        return res

    def solve(self) -> List[int] | None:
        q: deque = deque(self.get_zero_in_degree_nodes())

        counter = 0
        while len(q) > 0:
            u = q.popleft()
            self.orders.append(u)
            counter += 1
            for v in self.g[u]:
                self.in_degrees[v] -= 1
                if self.in_degrees[v] <= 0:
                    q.append(v)

        return self.orders if counter == self.n else None


class FoxAndNamesSolution:

    def __init__(self,n: int, names: List[str]):

        self.n: int = n
        self.names: List[str] = names
        self.topo_sln: TopologicalSortSolution | None = None

    def build(self) -> bool:

        g_set: List[set[int]] = [set() for _ in range(26)]

        for i in range(self.n - 1):
            first_name = self.names[i]
            second_name = self.names[i+1]
            j = 0
            min_len = min(len(first_name), len(second_name))
            while j < min_len and first_name[j] == second_name[j]:
                j += 1
            if j < min_len:
                g_set[ord(first_name[j]) - ord('a')].add(ord(second_name[j]) - ord('a'))

        g: List[List[int]] = [list(set_v) for set_v in g_set]
        self.topo_sln = TopologicalSortSolution(26, g)
        self.topo_sln.initialize()
        return True

    def solve(self) -> str:

        if not self.build():
            return 'Impossible'

        orders = self.topo_sln.solve()

        if orders is None:
            return 'Impossible'

        res = ''
        num_a = ord('a')
        for n_c in orders:
            res += chr(num_a + n_c)

        return res



n1 = 3
names1 = '''rivest
shamir
adleman'''.split('\n')

sln = FoxAndNamesSolution(n1, names1)

#print(sln.solve())

n2 = 10
names2 = '''petr
egor
endagorion
feferivan
ilovetanyaromanova
kostka
dmitriyh
maratsnowbear
bredorjaguarturnik
cgyforever'''.split('\n')

sln2 = FoxAndNamesSolution(n2, names2)
#print(sln2.solve())

n3 = 7
names3 = '''car
care
careful
carefully
becarefuldontforgetsomething
otherwiseyouwillbehacked
goodluck'''.split('\n')

sln3 = FoxAndNamesSolution(n3, names3)
print(sln3.solve())