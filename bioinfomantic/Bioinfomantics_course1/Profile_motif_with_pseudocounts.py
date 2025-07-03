
from Scoring_Motifs import Count_motif
def Profile_with_pseudocounts(Motifs):

    t = len(Motifs)
    n = len(Motifs[0])

    count_matrix = Count_motif(Motifs)

    for i in range(n):
        for c in "ACGT":
            count_matrix[c][i] = (count_matrix[c][i]+1)/(t+4)

    return count_matrix






