from typing import List, Optional


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class QuadTree:
    def __init__(self, grid: List[List[int]]):
        self.grid: List[List[int]] = grid
        self.m: int = len(grid)
        self.n: int = len(grid[0])

    def construct(self) -> Node | None:
        return self.decompose_and_merge(0, self.m, 0, self.n)

    def decompose_and_merge(self, beg_row: int, end_row: int, beg_col: int, end_col: int) -> Node | None:

        if beg_col == end_col and beg_row == end_row:
            return None

        if (end_row - beg_row) == 1 and (end_col - beg_col) == 1:
            return Node(self.grid[beg_row][beg_col], True, None, None, None, None)

        mid_row = (end_row + beg_row - 1) // 2
        mid_col = (end_col + beg_col - 1) // 2

        top_left = self.decompose_and_merge(beg_row, mid_row + 1, beg_col, mid_col + 1)
        top_right = self.decompose_and_merge(beg_row, mid_row + 1, mid_col + 1, end_col)
        bottom_left = self.decompose_and_merge(mid_row + 1, end_row, beg_col, mid_col + 1)
        bottom_right = self.decompose_and_merge(mid_row + 1, end_row, mid_col + 1, end_col)

        if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf \
                and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
            return Node(top_left.val, True, None, None, None, None)

        return Node(1, False, top_left, top_right, bottom_left, bottom_right)


grid1 = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]

sln = QuadTree(grid1)

root = sln.construct()

res: List[List[int]] = []


def retrieve_info(cur_node: Node | None):
    if cur_node is None:
        return

    res.append([1 if cur_node.isLeaf else 0, cur_node.val])
    retrieve_info(cur_node.topLeft)
    retrieve_info(cur_node.topRight)
    retrieve_info(cur_node.bottomLeft)
    retrieve_info(cur_node.bottomRight)


retrieve_info(root)
print(res)
