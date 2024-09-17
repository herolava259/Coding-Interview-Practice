
def birthday(s, d, m):
    # Write your code here
    length = len(s)
    counter = 0
    sums = sum(s[:m])
    if sums == d:
        counter += 1

    for i in range(m ,length):
        sums -= s[i -m]
        sums += s[i]
        if sums == d:
            counter +=1
    return counter

s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d= 18
m= 7

print(birthday(s, d, m))