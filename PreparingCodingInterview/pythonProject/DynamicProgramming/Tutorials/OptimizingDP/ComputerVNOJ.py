from typing import List, Tuple



class ComputerSolution:
    def __init__(self, x_laptop: int, y_pc: int, a_price: int, b_price: int, n_dpt: int):

        self.x_laptop: int = x_laptop
        self.y_pc: int = y_pc

        self.a_price: int = a_price
        self.b_price: int = b_price

        self.n_dpt: int = n_dpt

    def solve(self) -> int:

        def init_f(x_dim: int = self.x_laptop, y_dim: int = self.y_pc) -> List[List[Tuple[int, int]]]:
            return [[(0, 0) for _ in range(y_dim)] for _ in range(x_dim)]

        def new_state(s: Tuple[int, int], a: int, v: int) -> Tuple[int, int]:

            new_dpt, new_val = s
            new_val += a
            if new_val >= v:
                new_dpt += 1
                new_val = 0

            return new_dpt, new_val
        def maximize(pair_a: Tuple[int, int], pair_b: Tuple[int, int]) -> Tuple[int, int]:
            if pair_a[0] > pair_b[0]:
                return pair_a
            elif pair_a[0] == pair_b[0]:
                return pair_a if pair_a[1] >= pair_b[1] else pair_b
            else:
                return pair_b

        def dp(value: int, x_dim: int = self.x_laptop, y_dim: int = self.y_pc)-> bool:
            x_dim += 1
            y_dim += 1

            f: List[List[Tuple[int, int]]] = init_f(x_dim, y_dim)

            for i in range(x_dim):
                for j in range(y_dim):
                    if f[i][j][0] == self.n_dpt:
                        return True

                    if i < x_dim:
                        f[i+1][j] = maximize(f[i+1][j], new_state(f[i][j], self.a_price, value))

                    if j < y_dim:
                        f[i][j+1] = maximize(f[i][j+1], new_state(f[i][j], self.b_price, value))
            return False


        low, high = 0, (self.a_price * self.x_laptop + self.b_price * self.y_pc) // self.n_dpt
        while low < high:
            mid = (low + high) >> 1

            if dp(mid):
                low = mid
            else:
                high = mid - 1
        return low
