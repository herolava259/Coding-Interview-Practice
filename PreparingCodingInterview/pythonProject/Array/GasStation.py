from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        first, nxt = 0, 1
        n = len(gas)

        while first < n and gas[first] < cost[first]:
            first += 1
        if first == n:
            return -1
        nxt = (first + 1) % n
        remain_gas = gas[first] - cost[first]
        while first != nxt:
            remain_gas += gas[nxt] - cost[nxt]
            while first != nxt and remain_gas < 0:
                first = (first - 1) % n
                remain_gas += gas[first] - cost[first]

            if remain_gas < 0 and first == nxt:
                return -1
            nxt = (nxt + 1) % n

        nxt = (nxt - 1) % n

        remain_gas += gas[nxt] - cost[nxt]

        if remain_gas < 0:
            return -1

        return first

gas1 = [1,2,3,4,5]
cost1 = [3,4,5,1,2]

sln = Solution()

print(sln.canCompleteCircuit(gas1, cost1))