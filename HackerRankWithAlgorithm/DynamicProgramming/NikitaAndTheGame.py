




def arraySplitting(arr):

    n = len(arr)

    sums = sum(arr)

    def solve( part_sum, first, last):

        if first == last:
            return 0

        if part_sum % 2 == 1:
            return 0

        if part_sum == 0:
            return last-first

        half_sum = part_sum // 2

        s = 0
        idx = first - 1
        for id in range(first, last):
            s += arr[id]
            idx += 1
            if s == half_sum:
                break
        if s != half_sum:
            return 0

        return max(solve(half_sum, first, idx), solve(half_sum, idx + 1, last)) + 1
    return solve(sums, 0, n -1)

arr = [2,2,2,3,3]

print(arraySplitting(arr))