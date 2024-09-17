
def xorAndSum(a, b):
    # Write your code here
    res = 0

    len_a = len(a)
    len_b = len(b)
    max_loop = 314159
    pow2 = 1
    modk = 1000000007
    count = 0
    a = a[::-1]
    b = b[::-1]
    for i in range(max_loop):
        if i < len_b and b[i] == '1':
            count += 1

        multiplier = count
        if i < len_a and a[i] == '1':
            multiplier = max_loop + 1 - count

        res += (multiplier * pow2) % modk
        res %= modk

        pow2 = (pow2 * 2) % modk

    for i in range(len_b):
        res += (count * pow2) % modk
        res %= modk

        pow2 = (pow2 * 2) % modk

        if b[i] == '1':
            count -= 1

    return int(res)