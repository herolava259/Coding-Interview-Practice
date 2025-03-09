from typing import List


class MaximumSwapSolution:
    def __init__(self, num: int):
        self.num: int = num

    def solve(self) -> int:

        digits: List[int] = []

        num = self.num

        while num:
            digits.insert(0, num%10)
            num = num // 10

        argmax_rights = list(range(len(digits)))

        arg_max = len(digits) - 1

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < digits[arg_max]:
                argmax_rights[i]= arg_max
            elif digits[i] > digits[arg_max]:
                arg_max = i
        result = 0
        check = True
        for i in range(len(digits)):
            arg_max_i = argmax_rights[i]
            if check and i != arg_max_i:
                digits[i], digits[arg_max_i] = digits[arg_max_i], digits[i]
                check = False

            result *= 10
            result += digits[i]

        return result

num1 = 2736

sln = MaximumSwapSolution(num1)

print(sln.solve())





