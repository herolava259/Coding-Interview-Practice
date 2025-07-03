

def CountSubPeptidesofLinearPeptide(n):
    count = 1

    for i in range(n):
        count += n-i
    return count

print(CountSubPeptidesofLinearPeptide(21254))