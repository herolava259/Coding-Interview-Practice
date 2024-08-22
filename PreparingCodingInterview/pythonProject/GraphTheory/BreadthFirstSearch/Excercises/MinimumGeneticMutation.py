from typing import List, Deque, DefaultDict, Tuple
from collections import deque, defaultdict

char_gene = {'A': 1, 'C': 2, 'G': 3, 'T': 4}


class MGMSolution:
    def __init__(self, start_gene: str, end_gene: str, bank: List[str]):
        self.start_gene: str = start_gene
        self.end_gene: str = end_gene
        self.bank: List[str] = bank

    def solve(self) -> int:
        choices: str = 'ACGT'
        cur_num_mutate = 0
        visited: DefaultDict[str, bool] = defaultdict(bool)
        cur_gene = self.start_gene

        q: Deque[Tuple[int, str]] = deque()
        visited[cur_gene] = True
        q.append((cur_num_mutate, cur_gene))

        while q:
            cur_num_mutate, cur_gene = q.popleft()

            if cur_gene == self.end_gene:
                return cur_num_mutate
            for i in range(len(cur_gene)):
                for c in choices:
                    new_gene = cur_gene[0:i] + c + cur_gene[i + 1:]
                    if not visited[new_gene] and new_gene in self.bank:
                        visited[new_gene] = True
                        q.append((cur_num_mutate + 1, new_gene))
        return -1
