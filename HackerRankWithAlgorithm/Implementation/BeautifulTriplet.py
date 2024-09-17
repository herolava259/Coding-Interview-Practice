def naive_beautiful_triplets(d, arr):
    # Write your code here
    count = 0
    arr.sort()
    n = len(arr)
    d_double = 2 * d

    for j, half_sum in enumerate(arr[1:-1]):
        sum_double = 2 * half_sum
        for i in range(j):
            for k in range(j + 1, n):
                if sum_double == arr[i] + arr[k] \
                        and (arr[k] - arr[i]) == d_double:
                    count += 1

    return count

def opt_beautiful_triplets(d, arr):
    # Write your code here
    count = 0
    arr.sort()
    n = len(arr)
    d_double = 2 * d
    max_elem = arr[-1]
    bucket = [0 for i in range(max_elem + 1)]

    for i in range(n - 1):
        for j in range(i + 2, n):
            tmp = arr[i] + arr[j]
            tmp_subtract = arr[j] - arr[i]
            if tmp % 2 == 0 and tmp_subtract == d_double:
                bucket[tmp // 2] += 1

    for item in arr[1:-1]:
        count += bucket[item]

    return count

def on_beatiful_triplets(d, arr):
    count = 0
    arr.sort()
    n = len(arr)
