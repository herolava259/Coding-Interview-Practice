from typing import List
from collections import deque

class ThreeStateSolution:

    def __init__(self, m_row: int, n_col: int, matrix: List[List[str]]):
        self.m_row: int= m_row
        self.n_col: int= n_col
        self.matrix: List[List[str]] = matrix

    def bfs_solve(self) -> int:

        states = {'1', '2', '3'}
        beg_i, beg_j = -1, -1
        for i in range(self.m_row):
            beg_state = ''
            for j in range(self.n_col):
                if self.matrix[i][j] in states:
                    beg_state = self.matrix[i][j]
                    beg_i, beg_j = i, j
                    break
            if beg_state != '':
                break

        if beg_i == -1 or beg_j == -1:
            return -1
        cost_dic = {'1': 0, '2': 0, '3': 0, '.': 1}
        inf = 10**9 + 7
        cost_m = [[inf for _ in range(self.n_col)] for _ in range(self.m_row)]

        dq: deque = deque()

        dq.appendleft((beg_i, beg_j, {self.matrix[beg_i][beg_j]}))
        cost_m[beg_i][beg_j] = 0

        curr_i, curr_j = beg_i, beg_j
        check = False

        while dq:
            curr_i, curr_j, s = dq.popleft()
            cost_path = cost_m[curr_i][curr_j]

            if '1' in s and '2' in s and '3' in s:
                check = True
                break

            if curr_i-1 >= 0 and self.matrix[curr_i-1][curr_j] != '#'\
                    and cost_path + cost_dic[self.matrix[curr_i-1][curr_j]] < cost_m[curr_i-1][curr_j]:
                cost_m[curr_i - 1][curr_j] = cost_path + cost_dic[self.matrix[curr_i-1][curr_j]]
                if self.matrix[curr_i-1][curr_j] == '.':
                    dq.append((curr_i-1, curr_j))
                else:
                    new_s = s | {self.matrix[curr_i-1][curr_j]}
                    dq.appendleft((curr_i - 1, curr_j, new_s))

            if curr_i+1 < self.m_row and self.matrix[curr_i+1][curr_j] != '#'\
                    and cost_path + cost_dic[self.matrix[curr_i+1][curr_j]] < cost_m[curr_i+1][curr_j]:
                cost_m[curr_i + 1][curr_j] = cost_path + cost_dic[self.matrix[curr_i+1][curr_j]]
                if self.matrix[curr_i+1][curr_j] == '.':
                    dq.append((curr_i+1, curr_j, set(s)))
                else:
                    new_s = s | {self.matrix[curr_i-1][curr_j]}
                    dq.appendleft((curr_i + 1, curr_j, new_s))

            if curr_j-1 >= 0 and self.matrix[curr_i][curr_j-1] != '#'\
                    and cost_path + cost_dic[self.matrix[curr_i][curr_j - 1]] < cost_m[curr_i][curr_j - 1]:
                cost_m[curr_i][curr_j - 1] = cost_path + cost_dic[self.matrix[curr_i][curr_j - 1]]
                if self.matrix[curr_i][curr_j - 1] == '.':
                    dq.append((curr_i, curr_j - 1, set(s)))
                else:
                    new_s = s | {self.matrix[curr_i][curr_j - 1]}
                    dq.appendleft((curr_i, curr_j - 1, new_s))

            if curr_j+1 < self.n_col and self.matrix[curr_i][curr_j+1] != '#'\
                    and cost_path + cost_dic[self.matrix[curr_i][curr_j + 1]] < cost_m[curr_i][curr_j + 1]:
                cost_m[curr_i][curr_j + 1] = cost_path + cost_dic[self.matrix[curr_i][curr_j + 1]]
                if self.matrix[curr_i][curr_j + 1] == '.':
                    dq.append((curr_i, curr_j + 1, set(s)))
                else:
                    new_s = s | {self.matrix[curr_i][curr_j + 1]}
                    dq.appendleft((curr_i, curr_j + 1, new_s))

        if not check:
            return -1

        return cost_m[curr_i][curr_j]

raw_mtx_1 = '''11..2
#..22
#.323
.#333'''

raw_rows = raw_mtx_1.split('\n')
mtx_inp_1 = [list(row) for row in raw_rows]
m1 = 4
n1 = 5
sln1 = ThreeStateSolution(m1, n1, mtx_inp_1)

print(sln1.bfs_solve())

raw_mtx_2 = '''1#2#3'''
raw_rows = raw_mtx_2.split('\n')
mtx_inp_2 = [list(row) for row in raw_rows]
m2 = 1
n2 = 5
sln2 = ThreeStateSolution(m2, n2, mtx_inp_2)
print(sln2.bfs_solve())



