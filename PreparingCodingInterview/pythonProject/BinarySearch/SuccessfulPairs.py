from typing import List


class SuccessfulPairsSolution:

    def __init__(self, spells: List[int], potions: List[int], success: int):
        self.spells: List[int] = spells
        self.potions: List[int] = potions
        self.success: int = success

    def solve(self) -> List[int]:

        sorted_potions: List[int] = sorted(self.potions, reverse=True)

        results: List[int] = [0] * len(self.spells)

        sorted_spells = sorted(enumerate(self.spells), key=lambda c: c[1])

        first_p = 0

        for idx, s in sorted_spells:
            first_p = max(0, first_p)
            last_p = len(sorted_potions)-1
            while first_p < last_p:
                mid_p = (first_p + last_p) // 2

                mid_potion = sorted_potions[mid_p]
                if mid_potion * s >= self.success:
                    first_p = mid_p + 1
                else:
                    last_p = mid_p - 1

            if sorted_potions[first_p] * s < self.success:
                first_p -= 1
            results[idx] = first_p + 1

        return results


spells1 = [3,1,2]
potions1 = [8,5,8]
success1 = 16

sln = SuccessfulPairsSolution(spells1, potions1, success1)

print(sln.solve())
