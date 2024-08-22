from typing import List, Optional


class LRUNode:
    def __init__(self, key: int, val: int, prev_node: Optional['LRUNode'] = None,
                 next_node: Optional['LRUNode'] = None):
        self.key: int = key
        self.val: int = val
        self.prev_node: Optional['LRUNode'] = prev_node
        self.next_node: Optional['LRUNode'] = next_node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.map_node: List[LRUNode | None] = [None for _ in range(10001)]
        self.head: LRUNode = LRUNode(-1, -1)
        self.tail: LRUNode | None = self.head
        self.size: int = 0

    def get(self, key: int) -> int:

        key %= 10001

        if not self.map_node[key]:
            return -1

        if self.tail != self.map_node[key]:
            cutting_node = self.cutting_node(key)
            self.tail.next_node = cutting_node
            cutting_node.prev_node = self.tail
            self.tail = cutting_node

        return self.map_node[key].val

    def cutting_node(self, key: int) -> LRUNode:
        cur_node = self.map_node[key]

        cur_node.prev_node.next_node = cur_node.next_node
        if cur_node.next_node:
            cur_node.next_node.prev_node = cur_node.prev_node
        cur_node.prev_node = None
        cur_node.next_node = None
        return cur_node

    def put(self, key: int, val: int) -> None:

        if self.get(key) != -1:
            self.map_node[key].val = val
            return

        self.refresh_cache()

        new_node = LRUNode(key, val, self.tail)
        self.tail.next_node = new_node
        self.tail = new_node

        self.map_node[key] = new_node
        self.size += 1

    def refresh_cache(self):
        while self.size >= self.capacity:
            num_remove = self.remove_lru_node()
            self.size -= num_remove

    def remove_lru_node(self) -> int:

        removed_node = self.head.next_node
        nxt_node = removed_node.next_node

        if nxt_node:
            nxt_node.prev_node = self.head

        self.head.next_node = nxt_node
        if self.head.next_node is None:
            self.tail = self.head

        self.map_node[removed_node.key] = None
        del removed_node
        return 1


cache = LRUCache(2)

cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
print(cache.get(1))
print(cache.get(2))
