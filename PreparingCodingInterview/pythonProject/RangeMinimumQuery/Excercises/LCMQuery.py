from typing import List


def prime_sieve(n: int):
    is_prime = [True for _ in range(n + 2)]

    primes = []
    # sqrt_n = math.ceil(math.sqrt(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 2):
        if i * i < n + 2 and is_prime[i]:
            for j in range(i * i, n + 2, i):
                is_prime[i] = False
    for i in range(n + 2):
        if is_prime[i]:
            primes.append(i)
    return primes


mod_k = 10 ** 9 + 7


class LCMDSSolution:
    def __init__(self, arr: List[int]):

        self.primes = prime_sieve(60)
        self.arr: List[int] = arr
        self.n = len(arr)
        len_prime = len(self.primes)
        self.dp: List[List[List[int]]] = [[[0] * len_prime for _ in range(self.n + 1)] for _ in range(self.n)]

    def build(self):
        len_prime = len(self.primes)
        for i in range(self.n):
            for idx, prime in enumerate(self.primes):
                e = self.arr[i]
                num_prime = 0
                while e > 0 and e % prime == 0:
                    num_prime += 1
                    e = e // prime
                self.dp[i][1][idx] = num_prime

        for j in range(2, self.n + 1):
            for i in range(self.n):
                if i + j - 1 >= self.n:
                    self.dp[i][j] = [list(p_num) for p_num in self.dp[i][j - 1]]
                    continue
                for idx in range(len_prime):
                    self.dp[i][j][idx] = max(self.dp[i][j - 1][idx], self.dp[i + j - 1][1][idx])

    def query(self, i: int, len_arr: int) -> int:
        lcm = 1
        expo = self.dp[i][len_arr]
        for idx, p in enumerate(self.primes):
            lcm = (lcm * (p ** expo[idx])) % mod_k
        return lcm

    def compare(self, query_1: tuple, query_2: tuple) -> bool:

        st1, len1 = query_1
        st2, len2 = query_2
        rat: float = 1.0

        expo_1 = self.dp[st1][len1]
        expo_2 = self.dp[st1][len2]
        for idx, p in enumerate(self.primes):
            rat *= (p ** (expo_1[idx] - expo_2[idx]))
        return rat <= 1.0


class LCMQueryResolverSolution:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.lcm_sln = LCMDSSolution(arr)
        self.dp: List[int] | None = None

    def resolve(self):
        if self.dp is None:
            return

        self.lcm_sln.build()
        self.dp = [-1 for _ in range(self.n + 1)]

        for len_a in range(1, self.n + 1):
            arg_min_idx = 0
            for i in range(0, self.n - len_a + 1):
                if not self.lcm_sln.compare((arg_min_idx, len_a), (i, len_a)):
                    arg_min_idx = i

            self.dp[len_a] = self.lcm_sln.query(arg_min_idx, len_a)

        del self.lcm_sln

    def query(self, x: int):
        return self.dp[x]
