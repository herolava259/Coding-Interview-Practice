from typing import List, Deque as Stack, Tuple
from collections import deque as stack

class MinHeap:
    def __init__(self, capacity: int = 1000):

        self.capacity = capacity
        self.size = 0
        self._heap: List[Tuple[float, int]] = [(-1.0, -1)]

    def _swap(self, p1: int, p2: int):
        self._heap[p1], self._heap[p2] = self._heap[p2], self._heap[p1]

    def empty(self) -> bool:
        return self.size <= 0

    def _compare(self, p1: int, p2: int) -> bool:
        return self._heap[p1][0] <= self._heap[p2][0]

    def arg_min(self, p1: int, p2: int, p3: int) -> int:

        min_val = min(self._heap[p1][0], self._heap[p2][0], self._heap[p3][0])

        if min_val == self._heap[p1][0]:
            return p1
        if min_val == self._heap[p2][0]:
            return p2

        return p3

    def push(self, time: float, idx: int):

        self._heap.append((time, idx))
        self.size += 1

        cur_p = self.size

        while cur_p > 1:
            par_p = cur_p >> 1

            if self._heap[par_p][0] <= self._heap[cur_p][0]:
                break

            self._swap(par_p, cur_p)
            cur_p = par_p

    def peek(self) -> Tuple[float, int] | None:
        if self.empty():
            return None
        return self._heap[1]

    def pop(self) -> Tuple[float, int] | None:
        if self.empty():
            return None


        self._swap(1, self.size)
        self.size -= 1
        pop_pair = self._heap.pop()
        cur_p = 1

        while (cur_p << 1) <= self.size:
            left_p = cur_p << 1
            right_p = min(self.size, left_p + 1)

            arg_min_p = self.arg_min(cur_p, left_p, right_p)

            if arg_min_p == cur_p:
                break

            self._swap(cur_p, arg_min_p)
            cur_p = arg_min_p


        return pop_pair


class GetCollisionTimesSolution:
    def __init__(self, cars: List[List[int]]):

        self.cars: List[List[int]] = cars

    def solve(self) -> List[float]:

        min_heap: MinHeap = MinHeap()

        n = len(self.cars)

        ans: List[float] = [-1.0] * n
        collided: List[bool] = [False] * n
        collided[-1] = True
        last_fleets: List[int] = list(range(n))
        first_fleets: List[int] = list(range(n))

        def get_first_car_of_fleet(car_idx: int):
            if first_fleets[car_idx] == car_idx or car_idx <= 0:
                return car_idx
            first_fleets[car_idx] = get_first_car_of_fleet(car_idx-1)

            return first_fleets[car_idx]

        def get_last_car_of_fleet(car_idx: int):
            if last_fleets[car_idx] == car_idx or car_idx == n-1:
                return car_idx
            last_fleets[car_idx] = get_last_car_of_fleet(car_idx+1)

            return last_fleets[car_idx]

        def calc_collision_time(idx: int) -> float:
            pos, speed = self.cars[idx]

            last_fleets[idx+1] = get_last_car_of_fleet(idx+1)
            nxt_pos, nxt_speed = self.cars[last_fleets[idx+1]]
            if speed <= nxt_speed:
                return -1.0
            return float(nxt_pos - pos) / float(speed-nxt_speed)

        for i in range(n-1):
            collided_time: float = calc_collision_time(i)

            if collided_time >= 0.0:
                min_heap.push(collided_time, i)

        while not min_heap.empty():
            cd_timing, car_no = min_heap.pop()

            if last_fleets[car_no] != car_no or collided[car_no]:
                continue

            ans[car_no] = cd_timing

            last_fleets[car_no] = get_last_car_of_fleet(car_no+1)
            first_fleets[car_no+1] = get_first_car_of_fleet(car_no)

            collided[car_no] = True
            prev_fleet = get_first_car_of_fleet(car_no)

            if prev_fleet <= 0:
                continue

            re_timing = calc_collision_time(prev_fleet-1)
            if re_timing >= 0.0:
                min_heap.push(re_timing, prev_fleet - 1)

        return ans

    def monotonic_stack_solve(self) -> List[float]:
        inc_st: Stack[int] = stack()
        ans : List[float] = [-1.0] * len(self.cars)

        n = len(self.cars)

        for i in range(n-1, -1, -1):
            timing = -1.0
            cur_pos, cur_speed = self.cars[i]

            while inc_st:
                nxt_i = inc_st[-1]
                collided_time = ans[nxt_i]
                nxt_pos, nxt_speed = self.cars[nxt_i]
                if cur_speed <= nxt_speed:
                    inc_st.pop()
                    continue
                intended_time: float = float(nxt_pos-cur_pos) / float(cur_speed - nxt_speed)

                if collided_time == -1.0 or intended_time <= collided_time:
                    timing = intended_time
                    break
                inc_st.pop()
            ans[i] = timing
            inc_st.append(i)


        return ans


cars1 = [[3,4],[5,4],[6,3],[9,1]]

print(GetCollisionTimesSolution(cars1).monotonic_stack_solve())