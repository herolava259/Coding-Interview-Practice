from typing import List


class PartitionSolution:
    def __init__(self, s: str):

        self.s: str = s

    def solve(self) -> List[List[str]]:

        results: List[List[str]] = []

        def backtrack(len_sq: List[int], k: int) -> List[List[str]]:
            if k == 0:
                prev_l: int = 0
                palindromes: List[str] = []
                for l in len_sq:
                    cd_s = self.s[prev_l:prev_l + l]
                    if not is_palindrome(cd_s):
                        return
                    palindromes.append(cd_s)
                    prev_l += l
                results.append(palindromes)

            for i in range(1, k + 1):
                len_sq.append(i)
                backtrack(len_sq, k - i)
                len_sq.pop()

        backtrack([], len(self.s))

        return results


def is_palindrome(s: str) -> bool:
    first_p, last_p = 0, len(s) - 1

    while first_p < last_p:
        if s[first_p] != s[last_p]:
            return False
        first_p += 1
        last_p -= 1

    return True


s1 = 'a'
sln = PartitionSolution(s1)

print(sln.solve())
