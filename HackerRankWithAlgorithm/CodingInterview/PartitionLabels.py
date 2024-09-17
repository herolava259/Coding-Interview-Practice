from collections import defaultdict
from typing import List


class PartitionLabelsSolution:
    def __init__(self, s: str):
        self.s: str = s

    def solve(self) -> List[int]:

        min_idxs = defaultdict(lambda: 501)
        max_idxs = defaultdict(int)

        for idx, c in enumerate(self.s):
            min_idxs[c] = min(idx, min_idxs[c])
            max_idxs[c] = max(idx, max_idxs[c])
        first = min_idxs[self.s[0]]
        end = max_idxs[self.s[0]]
        res: List[int] = []
        for idx, c in enumerate(self.s):
            if idx > end:
                res.append(end - first + 1)
                first = min_idxs[c]
                end = max_idxs[c]
                continue
            min_idx, max_idx = min_idxs[c], max_idxs[c]
            end = max(end, max_idx)

        res.append(end - first + 1)

        return res

    @staticmethod
    def partitionLabels(s: str) -> List[int]:
        pass


inp = 'eccbbbbdec'

print(PartitionLabelsSolution(inp).solve())
