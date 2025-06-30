from typing import List


class DSU:
    def __init__(self, n: int):
        self.clan: List[int] = list(range(n))

    def find_clan(self, u: int) -> int:
        if self.clan[u] == u:
            return u
        self.clan[u] = self.find_clan(self.clan[u])
        return self.clan[u]

    def merge_clan(self, u: int, v: int) -> bool:
        clan_u = self.find_clan(u)
        clan_v = self.find_clan(v)

        if clan_u == clan_v:
            return False
        self.clan[clan_v] = self.clan[clan_u]
        return True

class MakeConnectedSolution:
    def __init__(self, n: int, connections: List[List[int]]):
        self.n: int = n
        self.connections: List[List[int]] = connections

    def solve(self) -> int:

        # count and check all subnetworks, count available cables
        dsu = DSU(self.n)
        num_subnet = self.n
        num_avail_cable = 0

        for u, v in self.connections:
            if not dsu.merge_clan(u, v):
                num_avail_cable += 1
            else:
                num_subnet -= 1

        return -1 if num_subnet-1 > num_avail_cable else num_subnet-1

if __name__ == '__main__':
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2]]
    sln = MakeConnectedSolution(n, connections)
    print(sln.solve())


