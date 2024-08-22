from typing import List, Optional


class BigDecimal:
    def __init__(self, init_num: int):

        self.digits: List[int] = []

        curr_num = init_num

        if curr_num == 0:
            self.digits = [0]
            return

        while curr_num > 0:
            last_digit = curr_num % 10

            self.digits.insert(0, last_digit)

            curr_num = curr_num // 10

    def add_digit(self, digit: int, is_head: bool = False) -> bool:

        if digit < 0 or digit > 9:
            return False

        if is_head:
            self.digits.insert(0, digit)
        else:
            self.digits.append(digit)
        return True

    def clone(self) -> Optional['BigDecimal']:

        clone_digits = list(self.digits)

        copy_d = BigDecimal(0)

        copy_d.digits = clone_digits

        return copy_d

    def decimal_str(self) -> str:
        res = ''

        for dig in self.digits:
            res = str(dig) + res
        return res


class UnitOfWork:
    def __init__(self, target: int, candidate: BigDecimal, residual: int):
        self.target: int = target
        self.candidate: BigDecimal = candidate
        self.residual = residual

    def reach(self) -> bool:
        return self.residual % self.target == 0

    def transfer(self) -> Optional['UnitOfWork']:
        new_d = self.candidate.clone()
        new_d.add_digit(0)
        yield UnitOfWork(self.target, new_d, (self.residual * 10) % self.target)

        new_d = self.candidate.clone()
        new_d.add_digit(1)
        yield UnitOfWork(self.target, new_d, (self.residual * 10 + 1) % self.target)


class OneAndZeroSolution:
    def __init__(self, n: int):
        self.n: int = n

    def initialize(self) -> List[(BigDecimal, int)]:

        pow10 = 1
        num_dig = 1
        while pow10 < self.n:
            pow10 *= 10
            num_dig += 1

        res: List[int] = [pow10]
        len_res = 1
        for i in range(num_dig - 2, -1, -1):

            pow10 = 10 ** i
            for j in range(len_res):
                res.append(res[j] + pow10)

            len_res = len_res << 1
        return [(BigDecimal(num), num) for num in res]

    def bfs_solve(self) -> str:

        big_decimals = self.initialize()

        q: List[UnitOfWork] = []

        for dec, num in big_decimals:
            q.append(UnitOfWork(self.n, dec, num % self.n))

        uow: UnitOfWork | None = None

        while q:
            uow = q.pop(0)

            if uow.reach():
                break

            for nxt_uow in uow.transfer():
                q.append(nxt_uow)

        if uow is None or not uow.reach():
            return 'IMPPOSSIBLE'

        return uow.candidate.decimal_str()
