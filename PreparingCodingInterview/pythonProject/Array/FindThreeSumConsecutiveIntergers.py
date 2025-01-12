from typing import List

class SumOfThreeSolution:
    def __init__(self, num: int):

        self.num: int = num

    def solve(self) -> List[int]:
        if self.num % 3 == 0:
            mid_num = self.num // 3
            return [mid_num-1, mid_num, mid_num+1]
        return []

