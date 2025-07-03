from Bio_w4 import Randomized_Motif_Search
from convert_list_to_string import list_to_string
from Scoring_Motifs import Count_motif

file_name = "C://Users\Admin\Desktop\dataset_161_5.txt"
in_put = "8 5 CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA".split()

with open(file_name, "r") as file:
    in_put = file.read().split()

k, t = int(in_put[0]), int(in_put[1])
Dna = in_put[2:]
output, score = Randomized_Motif_Search.Loop_RMS_n_times(Dna, k, t,100,search_fn=Randomized_Motif_Search.SimulatedAnnealingRMS)

cur_output = []
file_name2 = "C://Users\Admin\Desktop\Test.txt"
with open(file_name2, "r") as file:
    cur_output = file.read().split()



print("Best Score",Randomized_Motif_Search.Score_Motif(cur_output))

# print(Randomized_Motif_Search.Consensus(Count_motif(output)))
output = list_to_string(output)
print(output)
print(score)
