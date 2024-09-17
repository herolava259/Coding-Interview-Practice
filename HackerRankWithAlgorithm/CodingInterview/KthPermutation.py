

factorials = [1]

def factorial(n):
    if n <= 0:
        return factorials[0]
    factorials.append(n*factorial(n-1))

    return factorials[n]

def kthPermutation(k,n):

    factorial(n)
    permutations = []
    checks = [True]*(n+1)
    checks[0] = False
    for i in range(1, n+1):
        mod_i = k//factorials[n-i] + 1
        k = k % factorials[n-i]
        counter = 0
        for idx, flag in enumerate(checks):
            if flag:
                counter += 1
            if counter == mod_i:
                checks[idx] = False
                permutations.append(idx)
                break

    return permutations

print(kthPermutation(18,4))



