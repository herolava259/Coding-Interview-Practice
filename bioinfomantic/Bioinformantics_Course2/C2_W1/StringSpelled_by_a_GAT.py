def PathToGenome(lis_kmers):
    sequence = lis_kmers[0]
    for pat in lis_kmers[1:]:
        sequence += pat[-1]

    return sequence
