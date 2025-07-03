from collections import defaultdict

def DeBruijnGraph(k_mers):

    debruijn_adj = defaultdict(list)

    for kmer in k_mers:
        debruijn_adj[kmer[:-1]].append(kmer[1:])

    return debruijn_adj

