from typing import List
from typing import Optional
import random


class Cell:
    def __init__(self, previous_column: Optional['Column'] = None, next_column: Optional['Column'] = None):
        self.previous_column: Optional['Column'] = previous_column
        self.next_column: Optional['Column'] = next_column


class Column:
    def __init__(self, value: int = 2, cells: List[Cell] | None = None, is_end: bool = False):
        self.value = value
        self.cells: List[Cell] = cells if cells is not None else []
        self.is_end: bool = is_end


max_level = 20


class SkipLists:
    def __init__(self):
        self.head: Column = Column(0)
        self.tail: Column = Column(0, is_end=True)

        for i in range(max_level):
            self.head.cells.append(Cell(None, self.tail))
            self.tail.cells.append(Cell(self.head, None))

    def is_empty(self) -> bool:
        return self.head.cells[0].next_column.is_end

    def lower_bound(self, val: int) -> Column:

        curr_column = self.head
        for level in range(max_level - 1, -1, -1):
            while not curr_column.cells[level].next_column.is_end and curr_column.cells[level].next_column.value <= val:
                curr_column = curr_column.cells[level].next_column

        return curr_column

    def upper_bound(self, value: int) -> Column:
        curr_col = self.head

        for level in range(max_level, -1, -1):
            while not curr_col.cells[level].next_column.is_end and curr_col.cells[level].next_column.value <= value:
                curr_col = curr_col.cells[level].next_column

        return curr_col.cells[0].next_column

    def insert(self, val: int):
        temp: Column = self.lower_bound(val)

        if not temp.is_end and temp.value == val:
            return

        new_column: Column = Column(val)
        new_column.cells.append(Cell())

        while len(new_column.cells) <= max_level and random.random() > 0.5:
            new_column.cells.append(Cell())

        curr_col = self.head

        for level in range(max_level - 1, -1, -1):
            while not curr_col.cells[level].next_column.is_end and curr_col.cells[level].next_column.value <= val:
                curr_col = curr_col.cells[level].next_column

            if level < len(new_column.cells):
                next_col = curr_col.cells[level].next_column
                curr_col.cells[level].next_column = new_column
                next_col.cells[level].previous_column = new_column
                next_col.cells[level].previous_column = curr_col
                next_col.cells[level].next_column = new_column

    def erase(self, val):
        erased_col: Column = self.lower_bound(val)

        if erased_col.is_end or erased_col.value != val:
            return

        curr_col = self.head

        for level in range(max_level - 1, -1, -1):

            while not curr_col.cells[level].next_column.is_end and curr_col.cells[level].next_column.value <= val:
                curr_col = curr_col.cells[level].next_column

            if curr_col.value == erased_col.value:
                prev_col = curr_col.cells[level].previous_column
                next_col = curr_col.cells[level].next_column
                prev_col.cells[level].next_column = next_col
                next_col.cells[level].previous_column = prev_col

        del erased_col
