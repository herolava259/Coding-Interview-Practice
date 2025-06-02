from typing import List, Tuple, Optional, Literal


class BitArray:
    @staticmethod
    def convert_to_array(x: int) -> Tuple[bool, List[bool]]:
        bit_arr: List[bool] = [False] * 32
        negative = False
        if x < 0:
            negative = True
            if x == -(1<<31):
                return True, [False] * 31 + [True]
            x = -x

        for i in range(32):
            if (x&(1<<i)) != 0:
                bit_arr[i] = True

        return negative, bit_arr

    @staticmethod
    def init_32_bit_signed_integer(negative: bool) -> Optional['BitArray']:
        return BitArray(negative=negative)

    def __init__(self, x: int = None, negative: bool|None = None, bit_arr: List[bool] | None = None):

        if negative is not None and bit_arr is not None:
            self.negative: bool = negative
            self.bit_arr: List[bool] = bit_arr
            return
        elif negative is not None:
            self.negative: bool = negative
            self.bit_arr: List[bool] = [False] * 32
            return

        negative, bit_arr = BitArray.convert_to_array(x)
        self.negative: bool = negative
        self.bit_arr: List[bool] = bit_arr

    def left_shift(self, offset: int) -> Optional["BitArray"]:

        offset = max(0, offset)
        if offset >= 32:
            return BitArray(negative = self.negative)

        if offset == 0:
            return self

        shifted_bit_arr = [False] * offset + self.bit_arr[:32-offset]

        return BitArray(bit_arr=shifted_bit_arr, negative=self.negative)

    def compare_absolute_value(self, another: Optional['BitArray']) -> Literal[-1, 0, 1]:

        cur_bits, another_bits = self.bit_arr, another.bit_arr
        for cur_bit, another_bit in reversed(list(zip(cur_bits, another_bits))):
            if cur_bit == another_bit:
                continue
            if cur_bit:
                return 1
            else:
                return -1
        return 0


    def diff_sign_for(self, another: Optional['BitArray']) -> bool:
        return self.negative != another.negative

    def add_absolute(self, another: Optional['BitArray']) -> Optional['BitArray']:


        residual = False

        result_arr: List[bool] = [False]*32

        for i in range(32):
            result_arr[i] = self.bit_arr[i] ^ another.bit_arr[i] ^ residual
            residual = (self.bit_arr[i] and another.bit_arr[i]) or (self.bit_arr[i] and residual) or (another.bit_arr[i] and residual)

        return BitArray(negative=self.negative, bit_arr=result_arr)
    def index_first_index_bit_one(self) -> int:
        cur_p = 31
        while cur_p >= 0 and not self.bit_arr[cur_p]:
            cur_p -= 1
        return max(cur_p, 0)
    def add_bit(self, idx: int, bit: bool):
        if not bit:
            return
        if idx >= 31:
            self.bit_arr = [True] * 31
        self.bit_arr[idx] = bit

    @staticmethod
    def overflow_bit(idx: int, bit: bool) -> bool:
        return bit and idx >= 32

    def to_int_32_bit(self) -> int:
        result = 0

        if self.negative:
            for idx, bit in enumerate(self.bit_arr):
                result -= (1 << idx) if bit else 0
        else:
            for idx, bit in enumerate(self.bit_arr):
                result += (1 << idx) if bit else 0
        return result

    def __repr__(self):
        return f"Sign: {'-' if self.negative else '+'}\n Value: " + "".join('1'if bit else '0' for bit in self.bit_arr )

class DivideTwoIntegersSolution:
    def __init__(self, dividend: int, divisor: int):
        self.dividend: int = dividend
        self.divisor: int = divisor

    def solve(self) -> int:

        if self.dividend == 0:
            return 0
        if self.dividend == self.divisor:
            return 1
        if self.dividend == -(1 << 31) and self.divisor == -1:
            return (1 << 31) - 1
        if self.divisor == -1:
            return -self.dividend
        if self.divisor == 1:
            return self.dividend


        terms_bit_arr: List[BitArray] = []
        divisor_bit_arr = BitArray(x = self.divisor)
        dividend_bit_arr = BitArray(x = self.dividend)

        if divisor_bit_arr.compare_absolute_value(dividend_bit_arr) > 0:
            return 0

        diff_sign = dividend_bit_arr.diff_sign_for(divisor_bit_arr)

        prime_bit_arr = BitArray(negative = dividend_bit_arr.negative, bit_arr=divisor_bit_arr.bit_arr)

        begin_idx = prime_bit_arr.index_first_index_bit_one()

        for shifted_last_idx in range(begin_idx, 32):
            offset = shifted_last_idx - begin_idx
            cd_bit_arr = prime_bit_arr.left_shift(offset)
            if cd_bit_arr.compare_absolute_value(dividend_bit_arr) > 0:
                break
            terms_bit_arr.append(cd_bit_arr)

        accum_sum = BitArray(negative=dividend_bit_arr.negative, bit_arr=[False]*32)
        result_bit_arr = BitArray(negative=diff_sign)

        for idx, bit_arr in reversed(list(enumerate(terms_bit_arr))):
            cd_sum: BitArray = accum_sum.add_absolute(bit_arr)
            if cd_sum.compare_absolute_value(dividend_bit_arr) > 0:
                continue
            accum_sum = cd_sum
            result_bit_arr.add_bit(idx, True)

        return result_bit_arr.to_int_32_bit()

dividend1 = -2147483648
divisor1 = 3

print(DivideTwoIntegersSolution(dividend1, divisor1).solve())