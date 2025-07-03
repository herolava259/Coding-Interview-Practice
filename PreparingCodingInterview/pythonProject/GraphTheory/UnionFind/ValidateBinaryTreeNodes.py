from typing import List


class DSU:
    def __init__(self, size: int):
        self.par: List[int] = list(range(size))

    def find_root(self, u):
        if u == self.par[u]:
            return u
        self.par[u] = self.find_root(self.par[u])

        return self.par[u]

    def join(self, u, v) -> bool:
        if v == -1:
            return True
        par_u, par_v = self.find_root(u), self.find_root(v)

        if par_u == par_v:
            return False
        self.par[par_v] = par_u
        return True
    def not_root(self, u) -> bool:
        return u != self.par[u]



class ValidateBinaryTreeNodesSolution:
    def __init__(self, n: int, left_child: List[int], right_child: List[int]):

        self.n: int = n
        self.left_child: List[int] = left_child
        self.right_child: List[int] = right_child

    def solve(self) -> bool:
        dsu = DSU(self.n)
        for par, child in enumerate(zip(self.left_child, self.right_child)):
            left_c, right_c = child
            if left_c != -1 and (dsu.not_root(left_c) or not dsu.join(par, left_c)):
                return False

            if right_c != -1 and (dsu.not_root(right_c) or not dsu.join(par, right_c)):
                return False

        root = dsu.find_root(0)

        for u in range(1, self.n):
            if root != dsu.find_root(u):
                return False
        return True

n = 3
leftChild = [1,-1,-1]
rightChild = [-1,-1,1]

print(ValidateBinaryTreeNodesSolution(n, leftChild, rightChild).solve())
