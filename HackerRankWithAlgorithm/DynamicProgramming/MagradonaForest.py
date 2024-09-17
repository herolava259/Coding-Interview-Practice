

def seq_mandragora(H):

    argmax_idxs = []

    maxs = 0
    n = len(H)
    for idx in range(n-1,-1,-1):
        if H[idx] > maxs:
            maxs = H[idx]
            argmax_idxs.append(idx)
    argmax_idxs = argmax_idxs[::-1]
    bg = -1
    sums = 0
    for i in argmax_idxs:
        sums += (i-bg)*H[i]
        bg = i

    return sums

def mandragora(H):

    H.sort()
    sums = sum(H)

    max_exp = sums
    n = len(H)

    for i in range(n):
        sums -= H[i]
        tmp_exp = sums*(i+2)

        max_exp = max(max_exp, tmp_exp)

    return max_exp

n = 3
H = [3,2,2]

print(mandragora(H))


