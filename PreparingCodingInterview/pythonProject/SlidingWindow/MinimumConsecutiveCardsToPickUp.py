from typing import List, DefaultDict
from collections import defaultdict


class MinimumCardPickupSolution:
    def __init__(self, cards: List[int]):
        self.cards: List[int] = cards

    def hash_solve(self) -> int:

        idx_tb: DefaultDict[int, List] = defaultdict(list)
        min_dist = len(self.cards) + 1
        for idx, card in enumerate(self.cards):
            if len(idx_tb[card]) >= 0 and idx - idx_tb[card][-1] + 1 < min_dist:
                min_dist = idx - idx_tb[card][-1] + 1
            idx_tb[card].append(idx)

        return min_dist if min_dist <= len(self.cards) else -1

    def opt_hash_solve(self) -> int:
        idx_tb: DefaultDict[int, int] = defaultdict(lambda : -1)
        min_dist = len(self.cards) + 1
        for idx, card in enumerate(self.cards):
            if idx_tb[card] >= 0 and idx - idx_tb[card] + 1 < min_dist:
                min_dist = idx - idx_tb[card] + 1
            idx_tb[card]= idx

        return min_dist if min_dist <= len(self.cards) else -1
    def naive_solve(self) -> int:

        num_card = len(self.cards)
        min_dist = num_card + 1

        for idx in range(num_card):
            nxt_p = idx + 1
            while nxt_p < num_card and self.cards[nxt_p] != self.cards[idx]:
                nxt_p += 1
            if nxt_p < num_card and (nxt_p - idx + 1) <min_dist:
                min_dist = nxt_p - idx + 1
        return min_dist if min_dist <= num_card else -1

    def sliding_window_solve(self) -> int:
        num_card = len(self.cards)
        min_wd_size = num_card

        for idx in range(num_card):

            cur_window_size = min(min_wd_size, num_card - idx) - 1
            for i in range(1, cur_window_size):
                if self.cards[idx] == self.cards[idx + i]:
                    min_wd_size = i+1
                    break

        return min_wd_size



cards_test1 = [3,4,2,3,4,7]
cards_test2 = [1,0,5,3]

cards_test3 = [0,0]

sln = MinimumCardPickupSolution(cards_test3)

print(sln.opt_hash_solve())