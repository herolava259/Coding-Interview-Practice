from Scoring_Motifs import Count_motif
from Scoring_Motifs import Profile_motif
from collections import Counter
from collections import defaultdict
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
            freq = count_motifs[c][i]
            if freq > max_frq:
                char = c
                max_frq = count_motifs[c][i]

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
            prob = 1.0
            for q,c in enumerate(k_mers):
                prob *= Profile[c][q]
            if prob > max_prob:
                best_k_mers = k_mers
                max_prob = prob

        motifs.append(best_k_mers)

    return motifs


def RandomizedMotifSearch(Dna, k, t):

    n = len(Dna[0])
    rand_init_index = random.randint(n-k+1, size = t)
    #print(rand_init_index)
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
        print(tmp)

        if tmp < best_score:
            best_score = tmp
            BestMotifs = Motifs
        else:
            return BestMotifs, best_score





def MostProbMotifs_with_Temperature(k,Dna,Profile,init_array,temp = 0.0):
    t = len(Dna)
    n = len(Dna[0])
    for i,c in enumerate("ACGT"):
        for j in range(k):
            Profile[c][j] += temp *init_array[i][j]
    motifs = []
    for i in range(t):
        best_k_mers = ""
        max_prob = 0.0
        for j in range(n-k+1):
            k_mers = Dna[i][j:j+k]
            prob = 1.0
            for q,c in enumerate(k_mers):
                prob *= Profile[c][q]
            if prob > max_prob:
                best_k_mers = k_mers
                max_prob = prob

        motifs.append(best_k_mers)
    return motifs




def SimulatedAnnealingRMS(Dna,k,t):
    n = len(Dna[0])
    rand_init_index = random.randint(n-k+1, size = t)
    init_arr = random.uniform(low = 0.0, high = 1.0, size = (4,k))

    #print(rand_init_index)
    Motifs = []
    for i in range(t):
        j = rand_init_index[i]
        Motifs.append(Dna[i][j:j+k])

    BestMotifs = Motifs
    best_score = Score_Motif(BestMotifs)
    profile = {}
    go_on = 1
    while True:

        ischeck = True
        profile = Profile_motif(Motifs)
        Motifs = MostProbMotifs_with_Temperature(k,Dna,profile,init_arr,temp = 0.2)
        tmp = Score_Motif(Motifs)
        #print(tmp)
        if(tmp >= best_score):
            go_on -=1
            if go_on < 0:
                ischeck = False
        if ischeck:
            best_score = tmp
            BestMotifs = Motifs
        else:
            return BestMotifs, best_score



def Loop_RMS_n_times(Dna,k,t,n,search_fn = RandomizedMotifSearch):

    best_score = math.inf
    best_motifs = []
    results = defaultdict(int)
    for i in range(n):
        #print("Iter ",i)
        tmp_motifs, tmp_score = search_fn(Dna,k,t)
        if tmp_score < best_score:
            best_score = tmp_score
            best_motifs = tmp_motifs

    return best_motifs, best_score





