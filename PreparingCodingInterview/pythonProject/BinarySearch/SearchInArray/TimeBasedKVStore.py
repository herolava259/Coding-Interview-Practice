from typing import List, DefaultDict, Tuple
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.table: DefaultDict[str, List[Tuple[int, str]]] = defaultdict(lambda: [(-1, '')])

    def set(self, key: str, value: str, timestamp: int) -> None:
        seq: List[Tuple[int, str]] = self.table[key]

        low, high = 0, len(seq) - 1
        while low < high:
            mid = ((low + high) // 2) + (low+high) % 2
            ts, _ = seq[mid]

            if ts <= timestamp:
                low = mid
            else:
                high = mid-1
        seq.insert(low+1, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        seq = self.table[key]

        low, high = 0, len(seq)-1

        while low < high:
            mid = ((low+high) // 2) + (low+high) % 2

            ts, _ = seq[mid]

            if ts > timestamp:
                high = mid-1
            else:
                low = mid

        return seq[low][1]


ds: TimeMap | None = TimeMap()
print('null')
actions: List[Tuple[str, any]] = [('set', ('foo', 'bar', 1)), ('get', ('foo', 1)), ('get', ('foo', 3)), ('set', ('foo', 'bar2', 4)), ('get', ('foo', 4)),
                                  ('get', ('foo', 5))]


for cmd, arg in actions:
    if cmd == 'set':
        ds.set(*arg)
        print('null')
    elif cmd == 'get':
        print(ds.get(*arg))


# ds.set('foo', 'bar', 1)
#
# print(ds.get('foo', 1))
# print(ds.get('foo', 3))




