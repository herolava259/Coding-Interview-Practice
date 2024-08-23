from typing import List

class MaxVowelsSolution:
    def __init__(self, s: str, k: int):
        self.s: str = s
        self.k: int = k

    def solve(self) -> int:
        vowels = 'aeiou'

        cur_num_vowels = 0

        for i in range(0, self.k):
            if self.s[i] in vowels:
                cur_num_vowels += 1
        max_num_vowels = cur_num_vowels

        for i in range(1, len(self.s) - self.k +1):
            if self.s[i-1] in vowels:
                cur_num_vowels -= 1
            if self.s[i+self.k-1] in vowels:
                cur_num_vowels += 1

            if cur_num_vowels > max_num_vowels:
                max_num_vowels = cur_num_vowels

        return max_num_vowels

s1 = 'abciiidef'
k1 = 3

sln = MaxVowelsSolution(s1, k1)

print(sln.solve())