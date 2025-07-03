from math import log2


def Count_motif(matrix_motif):
    count_matric = {}
    n = len(matrix_motif)
    num_col = len(matrix_motif[0])

    for c in "ACGT":
        init_lis = [0] * num_col
        count_matric[c] = init_lis

    for motif in matrix_motif:
        for j in range(num_col):
            for c in "ACGT":
                if c == motif[j]:
                    count_matric[c][j] += 1
                    break

    return count_matric



def Profile_motif(matrix_motif):
    profile_matric = Count_motif(matrix_motif)
    num_col = len(matrix_motif[0])
    n = float(len(matrix_motif))
    #print(profile_matric)
    for i in range(num_col):
        profile_matric["A"][i] +=1
        profile_matric["A"][i] /=(n+4)

        profile_matric["C"][i] += 1
        profile_matric["C"][i] /= (n+4)

        profile_matric["G"][i] += 1
        profile_matric["G"][i] /= (n+4)

        profile_matric["T"][i] += 1
        profile_matric["T"][i] /= (n+4)

    return profile_matric



def Entropy_motif(matrix_motif):
    n = len(matrix_motif)
    num_col = len(matrix_motif[0])
    profile_matric = Profile_motif(matrix_motif)
    entropy_lis = []
    # print(profile_matric)
    for i in range(num_col):
        a = profile_matric["A"][i]
        a = a if a != 0 else 1

        t = profile_matric["T"][i]
        t = t if t != 0 else 1

        g = profile_matric["G"][i]
        g = g if g != 0 else 1

        c = profile_matric["C"][i]
        c = c if c != 0 else 1

        tmp = a * log2(a) + t * log2(t) + g * log2(g) + c * log2(c)
        entropy_lis.append(-tmp)

    return entropy_lis


test_case = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC"
]
#print(sum(Entropy_motif(test_case)))