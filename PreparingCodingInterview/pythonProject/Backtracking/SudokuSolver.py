from typing import List, Set, Tuple


class SudokuSolverSolution:

    def __init__(self, board: List[List[str]]):

        self.board: List[List[str]] = board

    def solve(self) -> None:

        m_row, n_col, p_box = 9, 9, 9

        rows: List[Set[int]] = [set() for _ in range(9)]
        cols: List[Set[int]] = [set() for _ in range(9)]
        boxes: List[Set[int]] = [set() for _ in range(9)]

        nums = set(idx+1 for idx in range(9))

        def construct()-> List[Tuple[int, int]]:
            result: List[Tuple[int, int]] = []
            for i in range(m_row):
                box_i = i//3
                for j in range(n_col):
                    if self.board[i][j] == '.':
                        result.append((i, j))
                        continue
                    box_j = j // 3
                    num = int(self.board[i][j])
                    boxes[box_i * 3 + box_j].add(num)
                    rows[i].add(num)
                    cols[j].add(num)
            return result

        missing_cells = construct()
        nums = set(idx + 1 for idx in range(9))

        def backtrack(k: int) -> bool:
            if k >= len(missing_cells):
                return True

            row_i, col_j = missing_cells[k]

            box_no = (row_i // 3) * 3 + col_j // 3

            missing_candidates = nums - (rows[row_i] | cols[col_j] | boxes[box_no])


            for cd_num in missing_candidates:

                rows[row_i].add(cd_num)
                cols[col_j].add(cd_num)
                boxes[box_no].add(cd_num)
                self.board[row_i][col_j] = str(cd_num)
                if backtrack(k+1):
                    return True

                rows[row_i].remove(cd_num)
                cols[col_j].remove(cd_num)
                boxes[box_no].remove(cd_num)
                self.board[row_i][col_j] = '.'

            return False

        backtrack(0)


board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

sln = SudokuSolverSolution(board1)

sln.solve()

for b in board1:
    print(b)





