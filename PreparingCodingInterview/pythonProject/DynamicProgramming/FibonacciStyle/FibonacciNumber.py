
class FibonacciNumberSolution:

    def __init__(self, n: int):
        self.n: int = n

    def solve(self) -> int:

        f0, f1 = 0, 1

        if self.n == 0:
            return f0
        if self.n == 1:
            return f1

        for _ in range(2, self. n + 1):
            f2 = f0 + f1

            f0, f1 = f1, f2

        return f1

n = 3

sln = FibonacciNumberSolution(n)

print(sln.solve())
