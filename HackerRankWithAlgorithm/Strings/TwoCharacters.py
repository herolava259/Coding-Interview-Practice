from collections import Counter
from collections import defaultdict


def alternate(s):
    # Write your code here

    index_chars = defaultdict(list)

    char_keys = list(Counter(s).keys())

    for index, c in enumerate(s):
        index_chars[c].append(index)

    n = len(index_chars)
    max_len = 0

    for i in range(n):
        for j in range(i + 1, n):
            c1 = char_keys[i]
            c2 = char_keys[j]
            less_len = min(len(index_chars[c1]), len(index_chars[c2]))
            gr_len = max(len(index_chars[c1]), len(index_chars[c2]))

            if gr_len - less_len < 2:

                if index_chars[c1][0] > index_chars[c2][0]:
                    k = 1
                    while k < less_len and index_chars[c1][k] > index_chars[c2][k] > index_chars[c1][k - 1]:
                        k += 1

                    if k == less_len and len(index_chars[c2]) > len(index_chars[c1]):
                        max_len = max(max_len, gr_len + less_len)
                        print(f"key: {c1}, values:{index_chars[c1]}")
                        print(f"key: {c2}, values:{index_chars[c2]}")
                        print("\n")

                else:
                    k = 1
                    while k < less_len and index_chars[c2][k] > index_chars[c1][k] > index_chars[c2][k - 1]:
                        k += 1
                    if k == less_len and len(index_chars[c1]) >= len(index_chars[c2]):
                        max_len = max(max_len, gr_len + less_len)
                        print(f"key: {c1}, values:{index_chars[c1]}")
                        print(f"key: {c2}, values:{index_chars[c2]}")
                        print("\n")

    return max_len


s = "txnbvnzdvasknhlmcpkbxdvofimsvqbvkswlkrchohwuplfujvlwpxtlcixpajjpaskrnjneelqdbxtiyeianqjqaikbukpicrwpnjvfpzolcredzmfaznnzd "

print(alternate(s))
