from MinStack import MinStack


class SortStack:
    def __init__(self):

        self.s: MinStack = MinStack()

    def is_empty(self) -> bool:
        return self.s.is_empty()

    def push(self, val: int):

        tmp_s: MinStack = MinStack()
        while not self.s.is_empty() and val > self.s.peek():
            tmp_s.push(self.s.pop())

        self.s.push(val)

        while not tmp_s.is_empty():
            self.s.push(tmp_s.pop())

    def pop(self) -> int | None:
        return self.s.pop()

    def peek(self, idx: int) -> int | None:
        return self.s.peek(idx)
