from typing import List, Set


class NQueensSolution:
    def __init__(self, n: int):

        self.n: int = n

    def solve(self) -> List[List[str]]:

        results: List[List[str]] = []

        def backtrack(solution: List[str], positions: List[int]):

            if len(positions) == self.n:
                results.append(list(solution))
                return
            k = len(positions)

            overlap_pos: Set[int] = set()

            for pos_i, pos_j in enumerate(positions):
                overlap_pos.add(pos_j)
                offset = abs(pos_i - k)
                if pos_j - offset >= 0:
                    overlap_pos.add(pos_j - offset)
                if pos_j + offset < self.n:
                    overlap_pos.add(pos_j + offset)

            for i in range(self.n):

                if i in overlap_pos:
                    continue

                new_row = '.' * i + 'Q' + '.' * (self.n - i - 1)

                positions.append(i)
                solution.append(new_row)
                backtrack(solution, positions)
                positions.pop()
                solution.pop()

        backtrack([], [])

        return results


n1 = 9
sln = NQueensSolution(n1)
print(sln.solve())
