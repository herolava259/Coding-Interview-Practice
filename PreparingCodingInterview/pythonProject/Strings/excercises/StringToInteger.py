from typing import List


class MyAtoiSolution:
    def __init__(self, s: str):
        self.s = s

    def solve(self) -> int:

        cleaned_digits: List[int] = []

        max_range = (1<<31) -1
        min_range = -(1<<31)

        ignore_characters = " "
        sign_characters = "-+"

        negative = False
        has_sign = False


        for c in self.s:
            if not has_sign and c in ignore_characters:
                continue
            if c in sign_characters and not has_sign:
                negative =  c == "-"
                has_sign = True
                continue

            if not c.isdigit():
                break
            has_sign= True
            cleaned_digits.append(int(c))

        result = 0
        for idx, digit in enumerate(reversed(cleaned_digits)):
            result += digit * (10**idx)

            if negative and -result < min_range:
                return min_range
            if not negative and result > max_range:
                return max_range

        return -result if negative else result

s1 = "   +0 123"

print(MyAtoiSolution(s1).solve())
