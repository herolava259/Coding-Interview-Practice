from typing import List

"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", 
"popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
 

Constraints:

1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
"""


class SmallestInfiniteSet:

    def __init__(self):
        self.inf_heap: List[int] = [0] * 1001
        self.size = 0

        for i in range(1, 1001):
            self._heap_push(i)

    def _heap_push(self, num: int) -> None:
        self.size += 1
        self.inf_heap[self.size] = num

        cur_p = self.size

        while cur_p > 1:
            par_p = cur_p // 2

            if self.inf_heap[cur_p] >= self.inf_heap[par_p]:
                break
            self.inf_heap[cur_p], self.inf_heap[par_p] = self.inf_heap[par_p], self.inf_heap[cur_p]

            cur_p = par_p

    def _heap_pop(self, begin_idx: int = 1) -> int | None:

        if self.size <= 0:
            return None

        min_elem = self.inf_heap[begin_idx]

        self._swap(begin_idx, self.size)

        cur_p = begin_idx

        self.size -= 1

        while (cur_p << 1) + 1 <= self.size:

            left_p, right_p = (cur_p << 1), (cur_p << 1) + 1

            cur_min = min(self.inf_heap[cur_p], self.inf_heap[left_p], self.inf_heap[right_p])

            if cur_min == self.inf_heap[cur_p]:
                break
            elif cur_min == self.inf_heap[left_p]:
                self._swap(left_p, cur_p)
                cur_p = left_p
            elif cur_min == self.inf_heap[right_p]:
                self._swap(right_p, cur_p)
                cur_p = right_p

        if (cur_p << 1) <= self.size and self.inf_heap[cur_p << 1] < self.inf_heap[cur_p]:
            self._swap(cur_p << 1, cur_p)

        return min_elem

    def _swap(self, idx1: int, idx2: int) -> None:
        self.inf_heap[idx1], self.inf_heap[idx2] = self.inf_heap[idx2], self.inf_heap[idx1]

    def _empty(self) -> bool:
        return self.size <= 0

    def find_elem(self, val: int, idx: int = 1) -> int | None:

        if idx > self.size:
            return None

        if val == self.inf_heap[idx]:
            return idx

        # finding_idx = self.find_elem(val, idx << 1)
        # if finding_idx:
        #     return finding_idx

        return self.find_elem(val, idx << 1) or self.find_elem(val, (idx << 1) + 1)

    def popSmallest(self) -> int:
        return self._heap_pop()

    def addBack(self, num: int) -> None:

        cur_p = self.find_elem(num)
        if cur_p:
            return

        self._heap_push(num)


ds = SmallestInfiniteSet()

ds.addBack(2)
print(ds.popSmallest())
print(ds.popSmallest())
print(ds.popSmallest())
ds.addBack(1)
print(ds.popSmallest())
print(ds.popSmallest())
print(ds.popSmallest())
