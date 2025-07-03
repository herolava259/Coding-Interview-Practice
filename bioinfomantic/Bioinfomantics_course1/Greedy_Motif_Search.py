from Profile_most_Probable_k_mer import Most_probable_k_mer
from Scoring_Motifs import Profile_motif
from Scoring_Motifs import Count_motif
import math
from convert_list_to_string import list_to_string
def ScoreMotif(Motifs):

    k = len(Motifs[0])
    t = len(Motifs)
    sum_consensus = 0
    count_matrix = Count_motif(Motifs)

    for i in range(k):
        tmp = 0
        for c in "ACGT":
            tmp = max(tmp,count_matrix[c][i])

        sum_consensus += tmp

    return k*t - sum_consensus


#print(Count_motif(["AAAA"]))
def GreedyMotifSearch(Dnas, k, t, Profile_alg):
    score_best_motif = math.inf
    n = len(Dnas[0])
    best_motifs = []

    first_dna = Dnas[0]

    other_dnas = Dnas[1:]

    for i in range(n-k+1):
        tmp_motifs = []
        first_motif = first_dna[i:i+k]
        tmp_motifs.append(first_motif)

        for j in range(1,t):
            profile_motifs = Profile_alg(tmp_motifs)

            motif_j = Most_probable_k_mer(Dnas[j],k,profile_motifs)

            tmp_motifs.append(motif_j)

        tmp_score = ScoreMotif(tmp_motifs)
        if tmp_score < score_best_motif:
            best_motifs = tmp_motifs
            score_best_motif = tmp_score

    return best_motifs


def convert_data(in_put):

    lis_space = in_put.split("\n")

    param_int = lis_space[0].split()
    k, t = int(param_int[0]), int(param_int[1])

    Dnas = lis_space[1:]
    return k, t, Dnas
"""
raw_input = "3 5\nGGCGTTCAGGCA\nAAGAATCAGTCA\nCAAGGAGTTCGC\nCACGTCAATCAC\nCAATAATATTCG"
filename = "C://Users\Admin\Desktop\dataset_159_5.txt"

with open(filename, "r") as file:
    raw_input = file.read()

k, t, Dnas = convert_data(raw_input)

lis_output = GreedyMotifSearch(Dnas,k,t, Profile_motif)
print(lis_output)

str_output = list_to_string(lis_output)

print(str_output)
"""