from typing import List


class NumOfWeakCharacterSolution:
    def __init__(self, properties: List[List[int]]):
        self.properties: List[List[int]] = properties

    def solve(self) -> int:

        sorted_arr: List[List[int]] = sorted(self.properties, key=lambda c: (c[0], c[1]), reverse=True)

        buckets: List[List[int]] = []

        pres_atk = sorted_arr[0][0]

        buckets.append([sorted_arr[0][1]])

        for cur_atk, cur_def in sorted_arr[1:]:

            if cur_atk == pres_atk:
                buckets[-1].append(cur_def)
            else:
                pres_atk = cur_atk
                buckets.append([cur_def])

        max_def = buckets[0][0]
        num_weak = 0
        for buck in buckets[1:]:

            i = len(buck) - 1

            while i >= 0 and buck[i] < max_def:
                i -= 1

            num_weak += len(buck) - (i+1)

            if i >= 0:
                max_def = buck[0]

        return num_weak


properties1 = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]

sln = NumOfWeakCharacterSolution(properties1)

print(sln.solve())
