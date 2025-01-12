from typing import List, Dict, Optional


class HuffmanNode:
    def __init__(self, bit_code: bool, freq: int, cnt: str = '$', is_leaf=False,
                 left_node: Optional['HuffmanNode'] = None,
                 right_node: Optional['HuffmanNode'] = None):
        self.bit_code: bool = bit_code
        self.is_leaf: bool = is_leaf
        self.cnt: str = cnt
        self.freq: int = freq
        self.left_node: Optional['HuffmanNode'] = left_node
        self.right_node: Optional['HuffmanNode'] = right_node


class MinHeap:
    def __init__(self, capacity: int = 10000):
        self.arr: List[Optional[HuffmanNode]] = [None for _ in range(capacity)]
        self.size: int = 0
        self.capacity: int = capacity

    def heap_push(self, e: HuffmanNode):
        if e is None:
            return
        if self.size >= self.capacity:
            self.arr = self.arr + [None for _ in range(self.capacity)]

        self.arr[self.size] = e
        self.size += 1

        self.heapify_to_top()

    def heap_pop(self) -> HuffmanNode | None:
        if self.size == 0:
            return None
        cur_node = self.arr[0]
        self.arr[self.size - 1], self.arr[0] = self.arr[0], self.arr[self.size - 1]

        self.size -= 1
        self.heapify_to_bottom()
        return cur_node

    def heapify_to_top(self):

        idx = self.size - 1
        while idx > 0:
            par_idx = idx // 2
            if self.arr[par_idx].freq > self.arr[idx].freq:
                self.arr[idx].freq, self.arr[par_idx].freq = self.arr[par_idx].freq, self.arr[idx].freq
            else:
                break
            idx = par_idx

    def heapify_to_bottom(self):

        idx = 0

        while idx * 2 < self.size:

            left_idx = idx * 2
            right_idx = idx * 2 + 1
            min_val = min(self.arr[idx].freq, self.arr[left_idx].freq, self.arr[right_idx].freq)

            if min_val == self.arr[idx].freq:
                break
            elif min_val == self.arr[left_idx].freq:
                self.arr[idx].freq, self.arr[left_idx].freq = self.arr[left_idx].freq, self.arr[idx].freq
                idx = left_idx
            elif min_val == self.arr[right_idx].freq:
                self.arr[idx].freq, self.arr[right_idx].freq = self.arr[right_idx].freq, self.arr[idx].freq
                idx = right_idx

    def __len__(self):
        return self.size

    def empty(self) -> bool:
        return self.size == 0


class HuffmanTree:
    def __init__(self, freq_table: Dict[str, int]):
        self.freq_table: Dict[str, int] = freq_table
        self.root: Optional[HuffmanNode] = None
        self.map_word: Dict[str, str] = dict()

    def build(self):
        heap: MinHeap = MinHeap()
        for k in self.freq_table.keys():
            new_node = HuffmanNode(True, self.freq_table[k], cnt=k, is_leaf=True)

            heap.heap_push(new_node)

        while len(heap) > 1:
            e1, e2 = heap.heap_pop(), heap.heap_pop()

            e1.bit_code, e2.bit_code = False, True

            new_node = HuffmanNode(True, freq=e1.freq + e2.freq, left_node=e1, right_node=e2)

            heap.heap_push(new_node)

        self.root = heap.heap_pop()

        self.dfs_build('', self.root.left_node)
        self.dfs_build('', self.root.right_node)

    def dfs_build(self, bit_arr: str, u: HuffmanNode):
        new_bit_arr = bit_arr
        if u.bit_code:
            new_bit_arr += '1'
        else:
            new_bit_arr += '0'
        if u.is_leaf:
            self.map_word[u.cnt] = bit_arr
            return
        self.dfs_build(new_bit_arr, u.left_node)
        self.dfs_build(new_bit_arr, u.right_node)

    def encode(self, p: str) -> str:

        encoded_text: str = ''
        for c in p:
            encoded_text += self.map_word[c]

        return encoded_text

    def decode(self, e_p: str) -> str:

        decoded_text: str = ''

        cur_node = self.root

        for c in e_p:

            if c == '1':
                cur_node = cur_node.right_node
            elif c == '0':
                cur_node = cur_node.left_node

            if cur_node.is_leaf:
                decoded_text += cur_node.cnt
                cur_node = self.root

        return decoded_text
