def multiMod(a, b, mod):
    if b == 0:
        return 0
    if b == 1:
        return a % mod
    res = b % 2
    return (2 * multiMod(a, b // 2, mod) + (res * a) % mod) % mod


def summingPieces(arr):
    modk = 10 ** 9 + 7
    s = 0
    sums = 0
    fi = 0
    tmp = 0
    t = 0
    pow2 = 1
    for item in arr:
        pow2 = (pow2 * 2) % modk
        tmp = multiMod(pow2, item, modk)
        fi = ((fi + t) % modk + tmp - item) % modk
        s = (sums + fi) % modk
        sums = (sums + s) % modk
        t = (t + tmp // 2) % modk

    return s


print(summingPieces([1, 2, 3, 4, 5, 6, 7, 8, 9]))
