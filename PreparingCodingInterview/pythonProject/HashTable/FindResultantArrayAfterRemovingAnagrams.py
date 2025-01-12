from typing import List

class RemovingAnagramsSolution:
    def __init__(self, words: List[str]):
        self.words: List[str] = words

    def solve(self) -> List[str]:

        result: List[str] = []

        to_origin = lambda c: ''.join(sorted(c))

        result.append(self.words[0])
        n = len(self.words)
        for idx in range(1, n):
            anagram_prev, anagram_cur = to_origin(self.words[idx-1]), to_origin(self.words[idx])
            if anagram_prev != anagram_cur:
                result.append(self.words[idx])

        return result


words_test1 = ["abba","baba","bbaa","cd","cd"]

print(RemovingAnagramsSolution(words_test1).solve())
