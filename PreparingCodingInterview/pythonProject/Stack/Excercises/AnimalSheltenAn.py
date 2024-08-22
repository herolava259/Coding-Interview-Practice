from typing import Optional, List

cat = 1
dog = 2
any_animal = 3


class AnimalNode:
    def __init__(self, animal_type: int, next_node: Optional['AnimalNode'] = None, val: int = 1):
        self.type: int = animal_type
        self.next_node: Optional['AnimalNode'] = next_node
        self.next_same: Optional['AnimalNode'] = None
        self.value = val


class AnimalQueue:
    def __init__(self):
        self.size = 0

        self.heads: List[AnimalNode | None] = [None, None, None]

        self.tails: List[AnimalNode | None] = [None, None, None]

    def is_empty(self) -> bool:
        return self.heads[any_animal] is None

    def enqueue(self, animal_type: 1 | 2):
        new_node = AnimalNode(animal_type, next_node=None, val=self.size)

        if self.tails[animal_type] is not None:
            self.tails[animal_type].next_same = new_node
        self.tails[animal_type] = new_node
        if self.heads[animal_type] is None:
            self.heads[animal_type] = new_node

        if self.tails[any_animal]:
            self.tails[any_animal].next_node = new_node
        self.tails[any_animal] = new_node

        if not self.heads[any_animal]:
            self.heads[any_animal] = new_node
        self.size += 1

    def dequeue(self, animal_type: 1 | 2 | 3) -> int | None:

        popped_node: AnimalNode = self.heads[animal_type]

        if popped_node is None:
            return None

        self.heads[popped_node.type] = popped_node.next_same

        if popped_node.value == self.heads[any_animal].value:
            self.heads[any_animal] = popped_node.next_node
        else:
            prev_node = self.heads[any_animal]

            while prev_node.next_node and prev_node.next_node.value != popped_node.value:
                prev_node = prev_node.next_node

            prev_node.next_node = popped_node.next_node
        self.size -= 1
        return popped_node.value

    def dequeue_any(self) -> int | None:
        return self.dequeue(any_animal)

    def dequeue_cat(self) -> int | None:
        return self.dequeue(cat)

    def dequeue_dog(self) -> int | None:
        return self.dequeue(dog)
