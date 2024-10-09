from typing import List, Dict


class DSUNode:
    def __init__(self, account: str, name: str):
        self.account: str = account
        self.name: str = name


class DisjointSet:
    def __init__(self):
        self.par: Dict[str, DSUNode] = {}

    def find(self, account: str) -> DSUNode | None:
        par_node = self.par.get(account, None)
        if not par_node:
            return None

        par_account = account
        while par_node.account != par_account:
            par_account = par_node.account
            par_node = self.par[par_account]
        self.par[account] = par_node
        return par_node

    def join(self, a: str, b: str, name: str) -> bool:

        par_a = self.find(a)
        par_b = self.find(b)

        if not par_a:
            self.par[a] = par_a = DSUNode(a, name)

        if not par_b:
            self.par[b] = par_b = DSUNode(b, name)

        if par_a == par_b:
            return False
        if par_a.account > par_b.account:
            par_a, par_b = par_b, par_a

        self.par[par_b.account] = par_a

        return True

    def add(self, accounts: List[str]):
        name = accounts[0]
        par_account = accounts[1]

        if not self.par.get(par_account, None):
            self.par[par_account] = DSUNode(par_account, name)

        for account in accounts[2:]:
            self.join(par_account, account, name)

    def flatten_account(self) -> List[List[str]]:

        account_table: Dict[str, List[str]] = {}

        for acc in sorted(self.par.keys()):

            root_account = self.find(acc)
            if root_account.account == acc:
                account_table[acc] = [root_account.name, root_account.account]
            else:
                account_table[root_account.account].append(acc)

        return [list(account_table[acc]) for acc in account_table.keys()]


class AccountsMergeSolution:
    def __init__(self, accounts: List[List[str]]):
        self.accounts: List[List[str]] = accounts

    def solve(self) -> List[List[str]]:
        dsu: DisjointSet = DisjointSet()

        for account_arr in self.accounts:
            dsu.add(account_arr)

        return dsu.flatten_account()


accounts1 = [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
             ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
             ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]

sln = AccountsMergeSolution(accounts1)

print(sln.solve())
