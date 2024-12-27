from typing import List

class ArrangeCoinsSolution:
    def __init__(self, n: int):
        self.n: int = n

    def solve(self) -> int:

        low, high = 1, self.n

        while low < high:

            mid = ((low + high) // 2) + ((low+high)%2)

            num_coin = (mid // 2) * (mid+1)

            if mid % 2 == 1:
                num_coin += (mid // 2) + 1
            if num_coin > self.n:
                high = mid - 1
            elif num_coin == self.n:
                return mid
            else:
                low = mid

        return low


for test in [1, 5, 6, 8, 9, 10]:
    print(f'Test case n={test}. Result: {ArrangeCoinsSolution(test).solve()}')
