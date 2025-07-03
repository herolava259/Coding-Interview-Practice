from C2_W3.GeneratingTheoreticalSpectrumProblem import mass_table
from collections import defaultdict

Mass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def CountingPeptidewithGivenMass(m,mass):

    count_table = defaultdict(int)


    minaa = mass[0]
    count_table[0] = 1
    if m < mass[0]:
        return 0

    begin = mass[0]
    n = len(mass)
    print(n)

    for v in range(minaa,m+1,1):
        j = 0
        while j < n and v >= mass[j]:
            count_table[v] += count_table[v-mass[j]]

            j+=1

    return count_table[m]

m = 2025

print(CountingPeptidewithGivenMass(m,Mass))



