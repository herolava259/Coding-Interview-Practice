from numpy import random
from Scoring_Motifs import Profile_motif
from Bio_w4 import Randomized_Motif_Search
def Probabilities_k_mer(k_mer, Profile):
    prob = 1.0

    for i,c in enumerate(k_mer):
        prob *= Profile[c][i]

    return prob

def Profile_randomly_generated_k_mer(k,Seqi,Profile):
    n = len(Seqi)
    probs = []
    for i in range(n-k+1):
        probs.append(Probabilities_k_mer(Seqi[i:i+k],Profile))


    sum_probs = sum(probs)
    for i in range(len(probs)):
        probs[i] /= sum_probs
    index_k_mer = random.choice(n-k+1,p = probs)
    return Seqi[index_k_mer:index_k_mer+k]


def GibbsSampler(Dna, k, t, N):
    n = len(Dna[0])
    index_init_motifs = random.randint(low = 0, high = n-k+1, size = t)
    Motifs = []
    BestMotifs = []

    for i,index in enumerate(index_init_motifs):
        Motifs.append(Dna[i][index: index+k])

    BestMotifs = Motifs
    score_best_motifs = Randomized_Motif_Search.Score_Motif(BestMotifs)

    for j in range(N):
        i = random.randint(low = 0, high = t, size = 1)[0]
        motifs_copy = Motifs.copy()
        motifs_copy = motifs_copy[0:i] + motifs_copy[i+1:] if i<t-1 else motifs_copy[0:i]
        profile_exi = Profile_motif(motifs_copy)

        replace_k_mer = Profile_randomly_generated_k_mer(k,Dna[i],profile_exi)
        motifs_copy.insert(i, replace_k_mer)
        Motifs = motifs_copy

        tmp_score = Randomized_Motif_Search.Score_Motif(Motifs)
        if  tmp_score < score_best_motifs:
            score_best_motifs = tmp_score
            BestMotifs = Motifs

    return BestMotifs, score_best_motifs


