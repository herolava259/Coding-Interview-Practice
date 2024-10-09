from typing import List


class DisjointSet:
    def __init__(self):

        self.par: List[int] = [i for i in range(26)]

    def find(self, num: int) -> int:
        par_num = num
        while par_num != self.par[par_num]:
            par_num = self.par[par_num]

        self.par[num] = par_num

        return par_num

    def union_join(self, u: int, v: int) -> bool:

        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False

        if par_u > par_v:
            par_u, par_v = par_v, par_u

        self.par[par_v] = par_u
        return True


class SmallestEquivalentStringSolution:
    def __init__(self, s1: str, s2: str, baseStr: str):
        self.s1: str = s1
        self.s2: str = s2
        self.base_str: str = baseStr

    def solve(self) -> str:

        dsu = DisjointSet()
        for c1, c2 in zip(self.s1, self.s2):
            dsu.union_join(ord(c1) - 97, ord(c2) - 97)
        result = ''
        for c in self.base_str:
            result += chr(97 + dsu.find(ord(c) - 97))

        return result


s1 = "getscode"
s2 = "programs"
baseStr = "sourcecode"
sln = SmallestEquivalentStringSolution(s1, s2, baseStr)

print(sln.solve())
