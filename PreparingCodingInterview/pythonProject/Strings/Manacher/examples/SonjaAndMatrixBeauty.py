from typing import List, Tuple

# problem: https://judge.yosupo.jp/problem/enumerate_palindromes
class SonjaAndMatrixBeautySolver:
    def __init__(self, n_row: int, m_col: int, mtx: List[List[str]], max_n: int = 10_000):

        self.n_row = n_row
        self.m_col = m_col
        self.mtx = mtx
        self.max_n = max_n


    def solve(self) -> List[Tuple[int, int, int, int]]:

        def row_equal(r1: List[int], r2: List[int]):

            return all(c1 == c2 for c1, c2 in zip(r1, r2))

        def is_palindrome_shuffle(ct: List[int]) -> bool:
            has_odd = False
            for item in ct:
                if item % 2 == 0:
                    continue
                if not has_odd:
                    has_odd = True
                else:
                    return False
            return True

        def calc_d_odd(counters: List[List[int]])-> List[Tuple[int, int]]:

            ok: List[bool] = [False] + [is_palindrome_shuffle(c) for c in counters]

            result: List[Tuple[int, int]] = []

            l, r = 1, 0
            d_odd = [0] * (self.n_row + 1)

            left_boundary = lambda idx: idx - d_odd[idx] - 1
            right_boundary = lambda idx: idx + d_odd[idx] + 1

            condition_extend = lambda idx : left_boundary(idx) > 0 and right_boundary(idx) <= self.max_n and \
                                                ok[left_boundary(idx)] and \
                                                ok[right_boundary(idx)] and \
                                                row_equal(counters[left_boundary(idx)], counters[right_boundary(idx)])

            for ii in range(1, self.n_row+1):
                d_odd[ii] = 0 if ii > r else min(r-ii, d_odd[l + r - ii])

                if ok[ii]:
                    while condition_extend(ii):
                        d_odd[ii] += 1
                    result.append((ii, d_odd[ii]+1))

                # update

                if ii + d_odd[ii] > r:
                    l, r = ii - d_odd[ii], ii + d_odd[ii]

            return result

        def calc_d_even(counters: List[List[int]]) -> List[Tuple[int, int]]:
            ok: List[bool] = [False] + [is_palindrome_shuffle(c) for c in counters]

            result: List[Tuple[int, int]] = []

            l, r = 1, 0
            d_even = [0] * (self.n_row + 1)

            left_boundary = lambda idx: idx - d_even[idx]
            right_boundary = lambda idx: idx + d_even[idx] + 1

            extend_condition = lambda idx: left_boundary(idx) > 0 and right_boundary(idx) <= self.max_n and \
                                            ok[left_boundary(idx)] and ok[right_boundary(idx)] and \
                                            row_equal(counters[left_boundary(idx)], counters[right_boundary(idx)])
            for ii in range(1, self.n_row+1):
                ij = ii + 1

                d_even[ii] = 0 if ij > r else min(r-ij+1, d_even[l + r - ij])

                while extend_condition(ii):
                    d_even[ii] += 1

                result.append((ii, d_even[ii]))

                if ii + d_even[ii] > r:
                    r, l = ii + d_even[ii], ij - d_even[ij]

            return result

        def transform_to_two_corner_repr(center_radius_forms: List[Tuple[int, int]],
                                         x_coord: Tuple[int, int]) \
                -> List[Tuple[int, int, int, int]]:
            x_f, x_e = x_coord
            result: List[Tuple[int, int, int, int]] = []

            for c, r in center_radius_forms:
                for half_size in range(r):
                    result.append((c - half_size, x_f, c + half_size, x_e))
            return result

        res: List[Tuple[int, int, int, int]] = []
        for x_first in range(1, self.m_col+1):
            counter: List[List[int]] = [[0] * 26 for _ in range(self.n_row+1)]
            for x_last in range(x_first, self.m_col+1):
                for y in range(1, self.n_row+1):
                    counter[y][ord(self.mtx[y][x_last]) - ord('a')] += 1

                odd_cr = calc_d_odd(counter)
                even_cr = calc_d_even(counter)

                res.extend(transform_to_two_corner_repr(odd_cr, x_coord=(x_first, x_last)))
                res.extend(transform_to_two_corner_repr(even_cr, x_coord=(x_first, x_last)))

        return res