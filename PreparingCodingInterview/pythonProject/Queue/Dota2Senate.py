from typing import Deque
from collections import deque


class PredictPartyVictorySolution:
    def __init__(self, senate: str):

        self.senate: str = senate

    def solve(self) -> str:

        q: Deque[str] = deque()

        num_radiant: int = 0
        num_dire: int = 0

        make_lose_dire = 0
        make_lose_radiant = 0

        for c in self.senate:
            if c == 'R':
                num_radiant += 1
            else:
                num_dire += 1
            q.append(c)

        while q and num_dire > 0 and num_radiant > 0:
            c = q.popleft()
            if c == "R":
                if make_lose_radiant > 0:
                    make_lose_radiant -= 1
                    num_radiant -= 1
                else:
                    make_lose_dire += 1
                    q.append(c)
            else:
                if make_lose_dire > 0:
                    make_lose_dire -= 1
                    num_dire -= 1
                else:
                    make_lose_radiant += 1
                    q.append(c)

        if num_dire != 0:
            return 'Dire'
        return 'Radiant'


senate1 = "RDD"

sln = PredictPartyVictorySolution(senate1)

print(sln.solve())
