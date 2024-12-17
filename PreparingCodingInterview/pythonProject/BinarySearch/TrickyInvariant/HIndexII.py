from typing import List


class HIndexIISolution:
    def __init__(self, citations: List[int]):
        self.citations: List[int] = citations
    def solve(self) -> int:

        low, high = 0, len(self.citations)

        n = len(self.citations)

        while low < high:
            # observed value of num of h-index
            mid = low + high
            cd_index = (mid >> 1) + (mid & 1)

            min_citation = self.citations[n - cd_index]

            if min_citation < cd_index:
                high = cd_index - 1
            else:
                low = cd_index

        return low

citations1 = [1,2,100]

sln = HIndexIISolution(citations1)

print(sln.solve())
