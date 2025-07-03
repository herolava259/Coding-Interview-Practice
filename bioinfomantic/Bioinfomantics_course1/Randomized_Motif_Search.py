from Scoring_Motifs import Count_motif
from Scoring_Motifs import Profile_motif
import numpy as np
import math
from numpy import random


def Consensus(count_motifs):

    n = len(count_motifs["A"])
    goal_str = ""
    for i in range(n):
        char = ""
        max_frq = 0
        for c in "ACGT":
            if count_motifs[c][i] > max_frq:
                char = c
                max_frq = count_motifs[c]

        goal_str += char

    return goal_str


def Score_Motif(Motifs):

    count_table = Count_motif(Motifs)

    consensus = Consensus(count_table)

    sub_freq = 0
    t = len(Motifs)
    k = len(Motifs[0])

    for i in range(k):
        sub_freq += count_table[consensus[i]][i]

    return k*t - sub_freq

def MostProbableMotifs(k,Dna, Profile):
    t = len(Dna)
    n = len(Dna[0])
    motifs = []
    for i in range(t):
        best_k_mers = ""
        max_prob = 0.0
        for j in range(n-k+1):
            k_mers = Dna[i][j:j+k]
            prob = 0.0
            for q,c in enumerate(k_mers):
                prob *= Profile[c][q]
            if prob > max_prob:
                best_k_mers = k_mers
                max_prob = prob

        motifs.append(best_k_mers)

    return motifs




def RandomizedMotifSearch(Dna, k, t):

    n = len(Dna[0])
    rand_init_index = random.randint(n-k, size = t)
    Motifs = []
    for i in range(t):
        j = rand_init_index[i]
        Motifs.append(Dna[i][j:j+k])

    BestMotifs = Motifs
    best_score = Score_Motif(BestMotifs)
    profile = {}
    while True:
        profile = Profile_motif(Motifs)
        Motifs = MostProbableMotifs(k,Dna,profile)
        tmp = Score_Motif(Motifs)
        if tmp < best_score:
            best_score = tmp
            BestMotifs = Motifs
        else:
            return BestMotifs, best_score



def Loop_RM_n_times(Dna,k,t,n):

    best_score = math.inf
    best_motifs = []
    for i in range(n):
        tmp_motifs, tmp_score = RandomizedMotifSearch(Dna,k,t)
        if tmp_score < best_score:
            best_score = tmp_score
            best_motifs = tmp_motifs

    return best_motifs, best_score





