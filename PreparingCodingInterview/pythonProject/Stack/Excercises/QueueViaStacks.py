from MinStack import MinStack


class SpecialQueue:
    def __init__(self):

        self.s_queue: MinStack = MinStack()
        self.s_dequeue: MinStack = MinStack()

    def enqueue(self, val: int):

        self.s_queue.push(val)

    def dequeue(self) -> int | None:
        if self.s_dequeue.is_empty():
            while not self.s_queue.is_empty():
                cur_val = self.s_queue.pop()
                self.s_dequeue.push(cur_val)
        return self.s_dequeue.pop()

    def is_empty(self) -> bool:
        return self.s_queue.is_empty() and self.s_dequeue.is_empty()
