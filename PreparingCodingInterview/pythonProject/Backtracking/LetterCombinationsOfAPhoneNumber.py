from typing import List, Dict

keyboard: Dict[int, str] = {1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}


class LetterCombinationSolution:
    def __init__(self, digits: str):
        self.digits: str = digits
        self.n = len(digits)
        self.results: List[str] = []

    def solve(self) -> List[str]:
        self.backtrack(0, '')

        return self.results

    def backtrack(self, k: int = 0, chain: str = ''):
        if k == self.n:
            self.results.append(chain)
            return

        for c in keyboard[int(self.digits[k])]:
            self.backtrack(k + 1, chain + c)
