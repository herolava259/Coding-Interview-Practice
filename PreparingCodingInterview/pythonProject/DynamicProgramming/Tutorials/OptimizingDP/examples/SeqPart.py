from typing import List

class SeqPartSolution:
    def __init__(self, g: int, l: int, nums: List[int]):
        self.g: int = g
        self.l: int = l
        self.nums: List[int] = nums

    def naive_solve(self) -> int:

        dp: List[List[int]] = [[0] * (self.l+1) for _ in range(self.g+1)]

        def cost(i: int, j: int) -> int:
            return sum(self.nums[t] for t in range(i, j+1)) * (j-i+1)

        for gr in range(1, self.g+1):
            for j in range(1, self.l+1):
                dp[gr][j] = min(dp[gr-1][k] + cost(k, j-1) for k in range(j))

        return dp[-1][-1]


    def boundary_solve(self) -> int:

        def aggregate_total(arr:List[int])-> List[int]:

            results: List[int] = [0] * len(arr)

            results[0] = arr[0]
            for i in range(1, len(arr)):
                results[i] = results[i-1] + arr[i]

            return results


        sums: List[int] = aggregate_total(self.nums)

        def cost(i, j) -> int:
            if i > j or i <= 0:
                return 0
            return (sums[j] - sums[i-1]) * (j-i+1)

        dp: List[List[int]] = [[0] * (self.l+1) for _ in range(self.g)]
        p: List[List[int]] = [[0] * (self.l+1) for _ in range(self.g)]

        def calc(g: int, l: int, r: int, bound_l: int, bound_r: int):

            if l > r:
                return

            mid = (l+r) >> 1

            dp[g][mid] = 10**9 +7

            for i in range(bound_l, bound_r+1):

                new_cost = dp[g-1][i] + cost(i+1, mid)

                if dp[g][mid] > new_cost:
                    dp[g][mid] = new_cost
                    p[g][mid] = i

            calc(g, l, mid-1, bound_l, p[g][mid])
            calc(g, mid+1, r, p[g][mid], bound_r)

        for i in range(1, self.l+1):
            dp[1][i] = cost(1, i)

        for i in range(2, self.g+1):
            calc(g, 1, self.l, 1, self.l)
        

