from typing import List

map_alphabet = {'a': 0, 'b': 1, 'c': 2}


class RabinKarpSolution:

    def __init__(self, t: List[str], p: List[str]):

        self.p: List[str] = p
        self.t: List[str] = t

    def solve(self) -> List[int]:

        num_p = 0
        len_p, len_t = len(self.p), len(self.t)
        expo = len(map_alphabet.keys())
        offset = 1
        first_t = 0
        for c_p, c_t in zip(self.p[::-1], self.t[:len_p][::-1]):
            num_p += offset * map_alphabet[c_p]
            first_t += offset * map_alphabet[c_t]
            offset *= expo

        nums_t: List[int] = [first_t]

        curr_num_t = first_t

        for idx, c_t in enumerate(self.t[len_p:]):
            curr_num_t -= offset * map_alphabet[self.t[idx - len_p]]
            curr_num_t *= expo
            curr_num_t += map_alphabet[c_t]
            nums_t.append(curr_num_t)

        return [idx for idx in range(len_t - len_p) if nums_t[idx] == nums_t]
