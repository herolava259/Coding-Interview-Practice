from typing import List
from collections import Counter

modk = 10**9 + 7
def gcd_extended(a: int, b: int) -> int:

    if b >= a:
        b = b % a

    a1, a2, a3 = 1, 0, a
    b1, b2, b3 = 0, 1, b

    while b3 != 0 and b3 != 1:
        q = a3 // b3
        r1 = a1 - q * b1
        r2 = a2 - q * b2
        r3 = a3 - q * b3

        a1, a2, a3 = b1, b2, b3
        b1, b2, b3 = r1, r2, r3

    if b3 == 0:
        return a3
    return b2


def factorial_modk(num: int) -> int:
    result: int = 1

    for i in range(1, num + 1):
        result = (result * i) % modk
    return result

class CountAnagramsSolution:
    def __init__(self, s: str):

        self.s: str = s

    def solve(self) -> int:

        words: List[str] = self.s.split(' ')


        def num_permutation_of(word: str) -> int:
            n_word = len(word)

            result = factorial_modk(n_word)
            freq = Counter(word)
            inverse_modk = lambda c: gcd_extended(modk, c)
            for c in freq.keys():
                if freq[c] == 1:
                    continue
                result = (result * inverse_modk(factorial_modk(freq[c]))) % modk

            return result

        num_anagram = 1

        for w in words:
            num_anagram = (num_anagram * num_permutation_of(w)) % modk

        return num_anagram


s1 = "aa"

print(CountAnagramsSolution(s1).solve())