from typing import List


class NextGreatestLetterSolution:
    def __init__(self, letters: List[str], target: str):
        self.letters: List[str] = letters
        self.target: str = target

    def solve(self) -> str:

        n = len(self.letters)

        low, high = 0, n - 1

        target_num = ord(self.target)
        while low < high:
            mid = (low + high) // 2
            mid_num = ord(self.letters[mid])

            if mid_num <= target_num:
                low = mid + 1
            else:
                high = mid

        return self.letters[low] if ord(self.letters[low]) > target_num else self.letters[0]


letters1 = ["x","x","y","y"]
target1 = "z"
sln = NextGreatestLetterSolution(letters1, target1)

print(sln.solve())
