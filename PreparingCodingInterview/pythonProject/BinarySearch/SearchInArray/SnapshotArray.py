from typing import List, Tuple

class SnapshotArray:

    def __init__(self, length: int):
        self.length: int = length
        self.table: List[List[Tuple[int, int]]] = [[] for _ in range(length+1)]
        self.buffer: List[Tuple[int, int]] = []
        self.cur_snapshot = 0

    def set(self, index: int, val: int) -> None:
        self.buffer.append((index, val))

    def snap(self) -> int:
        def push_and_clear():
            for index, val in self.buffer:
                self.table[index].append((self.cur_snapshot, val))
            self.buffer.clear()

        push_and_clear()

        self.cur_snapshot += 1
        return self.cur_snapshot-1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id >= self.cur_snapshot:
            return 0
        def find(arr: List[Tuple[int, int]], idx: int)-> int:
            if not arr:
                return 0
            low, high = 0, len(arr)-1

            while low < high:
                mid = ((low + high) // 2) + ((low+high)%2)

                cd_idx, _ = arr[mid]
                if cd_idx > idx:
                    high = mid - 1
                else:
                    low = mid

            return arr[low][1] if arr[low][0] <= idx else 0

        return find(self.table[index], snap_id)

actions = ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
args = [[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
ds: SnapshotArray | None = None
for cmd, arg in zip(actions, args):

    if arg == [0,1]:
        pass
    if cmd == 'SnapshotArray':
        ds = SnapshotArray(*tuple(arg))
        print('null')
    elif cmd == 'set':
        ds.set(*tuple(arg))
        print('null')
    elif cmd == 'snap':
        print(ds.snap())
    else:
        print(ds.get(*tuple(arg)))


