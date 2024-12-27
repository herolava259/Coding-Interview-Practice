from typing import List


class IsPerfectSquareSolution:
    def __init__(self, num: int):
        self.num: int = num

    def solve(self) -> bool:

        low, high = 1, self.num

        while low < high:

            mid = (low + high) // 2

            square_mid = mid ** 2

            if square_mid == self.num:
                return True
            elif square_mid > self.num:
                high = mid-1
            else:
                low = mid + 1

        if low ** 2 == self.num:
            return True

        return False


for test in [1, 4, 6, 7, 1999, 1024, 14, 16]:
    print(f'Test: num = {test}. Result: {IsPerfectSquareSolution(test).solve()}')