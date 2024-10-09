from typing import List


class DisjointSet:
    def __init__(self, ):

        self.par: List[int] = [i for i in range(26)]

    def find(self, var_sign: int) -> int:

        if var_sign == self.par[var_sign]:
            return var_sign

        self.par[var_sign] = self.find(self.par[var_sign])

        return self.par[var_sign]

    def union_join(self, var_a: str, var_b: str) -> bool:

        root_a = self.find(ord(var_a) - 97)
        root_b = self.find(ord(var_b) - 97)

        if root_a == root_b:
            return False

        self.par[root_b] = root_a

        return True


class EquationPossibleSolution:
    def __init__(self, equations: List[str]):

        self.equations: List[str] = equations

    def solve(self) -> bool:

        dsu = DisjointSet()
        not_eqs: List[str] = []
        for eq in self.equations:
            if eq[1:3] == '!=':
                not_eqs.append(eq)
                continue

            dsu.union_join(eq[0], eq[3])

        for eq in not_eqs:
            var_a, var_b = eq[0], eq[3]

            par_a, par_b = dsu.find(ord(var_a) - 97), dsu.find(ord(var_b) - 97)

            if par_a == par_b:
                return False

        return True


equations1 = ["b==a","a==b"]
sln = EquationPossibleSolution(equations1)

print(sln.solve())
