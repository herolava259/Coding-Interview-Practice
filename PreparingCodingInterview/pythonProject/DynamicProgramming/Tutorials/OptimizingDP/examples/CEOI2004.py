from typing import List




class CEOISolution:
    def __init__(self, n: int, weights: List[int], distances: List[int]):

        self.n: int = n
        self.weights: List[int] = weights
        self.dists: List[int] = distances

    def solve(self) -> int:

        def accumulate_of(arr: List[int]) -> List[int]:
            result = [0] * len(arr)
            result[0] = arr[0]

            for i in range(1, len(arr)):
                result[i] = result[i-1] + arr[i]

            return result

        sum_ws : List[int] = accumulate_of(self.weights)
        sum_ds: List[int] = accumulate_of(self.dists)

        sum_wds: List[int] = accumulate_of([w * sum_d for w, sum_d in zip(self.weights, sum_ds)])

        def cost(l: int, r: int) -> int:
            if r < l:
                l, r = r, l
            l-=1
            r-=1
            return sum_wds[l] - sum_wds[r] - sum_ds[r] * (sum_ws[l] - sum_ws[r])

        def evaluate(i: int, j: int) -> int:
            return cost(1, i) + cost(i+1, j) + cost(j+1, self.n+1)

        best: List[int] = [self.n] * self.n

        def calc(l: int, r: int, f: int, t: int):

            if f > r:
                return
            mid: int = (l + r) >> 1
            best[mid] = f

            for i in range(f+1, t+1):
                if evaluate(mid, best[mid]) > evaluate(mid, i):
                    best[mid] = i

            calc(l, mid-1, f, best[mid])
            calc(mid+1, r, best[mid], t)

        calc(1, self.n, 1, self.n)
        return min(evaluate(i, best[i]) for i in range(1, self.n+1))

