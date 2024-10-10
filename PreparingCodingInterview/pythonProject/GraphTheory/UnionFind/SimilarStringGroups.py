from typing import List, Dict


class DSU:
    def __init__(self):
        self.par: Dict[str, str] = dict()

    def add(self, chain: str) -> bool:
        if not self.par.get(chain, None):
            self.par[chain] = chain
            return True
        return False

    def find(self, chain: str) -> str | None:
        if not self.par.get(chain, None):
            return None
        par_chain = chain
        while par_chain != self.par[par_chain]:
            par_chain = self.par[par_chain]
        self.par[chain] = par_chain
        return par_chain

    def union_join(self, chain_a: str, chain_b: str) -> bool:
        par_a, par_b = self.find(chain_a), self.find(chain_b)

        if par_a == par_b or not par_a or not par_b:
            return False

        if par_a > par_b:
            par_a, par_b = par_b, par_a

        self.par[par_b] = par_a

        return True


def get_similar_chain_of(chain: str):
    k = len(chain)

    for i in range(k):
        for j in range(i + 1, k):
            if chain[i] > chain[j]:
                continue
            yield chain[:i] + chain[j] + chain[i + 1:j] + chain[i] + chain[j + 1:]


def is_similar(chain_a: str, chain_b: str):
    num_diff = 0
    diff_a: str = ''
    diff_b: str = ''

    for c_a, c_b in zip(chain_a, chain_b):
        if c_a == c_b:
            continue

        if num_diff == 2:
            return False
        if num_diff == 1 and (diff_a != c_b or c_a != diff_b):
            return False

        num_diff += 1
        diff_a, diff_b = c_a, c_b

    return True


class SimilarStringGroupSolution:
    def __init__(self, strs: List[str]):

        self.chains: List[str] = strs

    def solve(self) -> int:

        dsu: DSU = DSU()
        unique_chains: List[str] = []
        num_group = 0
        for chain in self.chains:
            if dsu.add(chain):
                num_group += 1
                unique_chains.append(chain)

        for i in range(len(unique_chains)):
            for j in range(i + 1, len(unique_chains)):
                if is_similar(unique_chains[i], unique_chains[j]) and dsu.union_join(unique_chains[i], unique_chains[j]):
                    num_group -= 1
        return num_group


strs1 = ["omv","ovm"]
sln = SimilarStringGroupSolution(strs1)

print(sln.solve())
