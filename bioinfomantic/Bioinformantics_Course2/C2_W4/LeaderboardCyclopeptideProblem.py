from collections import Counter

mass_of_aa = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
aminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

def Expand(LeaderBoard, mass_of_aa = mass_of_aa):

    new_board = []
    for pep in LeaderBoard:
        for aa in mass_of_aa:
            new_pep = pep.copy()
            new_pep.append(aa)
            new_board.append(new_pep)

    return new_board
# print(Expand([[]]))
def LinearSubPeptides(Peptide):

    lis_subpeptides = [[]]
    n = len(Peptide)
    for i in range(n):
        subpeptide = [Peptide[i]]
        lis_subpeptides.append(subpeptide.copy())
        for j in range(i+1,n,1):
            subpeptide.append(Peptide[j])
            lis_subpeptides.append(subpeptide.copy())

    return lis_subpeptides

def CycloSubPeptides(Peptide):
    lis_subpeptides = [[]]
    n = len(Peptide)

    for i in range(n):
        for j in range(1,n,1):
            k = i+j
            subpeptide = []
            if k > n:
                subpeptide.extend(Peptide[i:n].copy())
                subpeptide.extend(Peptide[0:k-n].copy())
            else:
                subpeptide.extend((Peptide[i:k]))

            lis_subpeptides.append(subpeptide)
    lis_subpeptides.append(Peptide.copy())
    return lis_subpeptides

pep = [1,2,3,4]

# print(CycloSubPeptides(pep))



Peptide = [71,113]

# print(LinearSubPeptides(Peptide))


def Mass(Peptide):
    mass = 0
    for aa in Peptide:
        mass += aa

    return mass


def MassofSubPeptides(Peptide):

    spectrum = []
    subpeptides = LinearSubPeptides(Peptide)
    for subpep in subpeptides:
        spectrum.append(Mass(subpep))
    spectrum.sort()
    return spectrum

def MassofSubPeptides_ver2(Peptide):
    spectrum = []
    subpeptides = CycloSubPeptides(Peptide)
    for subpep in subpeptides:
        spectrum.append(Mass(subpep))
    spectrum.sort()
    return spectrum

def ScoreCyclePeptide(Peptide,Spectrum):
    theorectical_spectrum = MassofSubPeptides_ver2(Peptide)
    theo_table = Counter(theorectical_spectrum)
    expri_table = Counter(Spectrum)
    elements_exp = list(expri_table.elements())
    score = 0
    for pep in theo_table:
        if pep in elements_exp:
            if theo_table[pep] >= expri_table[pep]:
                score += expri_table[pep]
            else:
                score += theo_table[pep]

    return score

def ScoreLinearPeptide(Peptide,Spectrum):

    theoretical_spectrum = MassofSubPeptides(Peptide)
    theo_table = Counter(theoretical_spectrum)
    expri_table = Counter(Spectrum)
    elements_exp = list(expri_table.elements())
    score = 0
    for pep in theo_table:
        if pep in elements_exp:
            if theo_table[pep] >= expri_table[pep]:
                score += expri_table[pep]
            else:
                score += theo_table[pep]

    return score


# Peptide = [114,128,129,113]
# Spectrum = [0,99,113,114,128,227,257,299,355,356,370,371,484]
# print(ScoreLinearPeptide(Peptide,Spectrum))

def Trim(Leaderboard, Spectrum, N):
    score_board = Counter()
    new_board = []
    if not Leaderboard:
        return new_board
    for i,pep in enumerate(Leaderboard):
        score_board[i] = ScoreLinearPeptide(pep,Spectrum)
        # print(score_board[i])
    most_common_board  = score_board.most_common()

    for i,(index,_) in enumerate(most_common_board):
        if i >= N:
            if most_common_board[i][1] < most_common_board[i-1][1]:
                break
        new_board.append(Leaderboard[index])



    return new_board

def Trim_ver2(Leaderboard, Spectrum, N):
    score_board = Counter()
    new_board = []
    if not Leaderboard:
        return new_board
    for i,pep in enumerate(Leaderboard):
        score_board[i] = ScoreCyclePeptide(pep,Spectrum)
    print("Trimver2:",score_board)
    print("N = 40: ",score_board.most_common(42))
    most_common_board = score_board.most_common(N)
    # print("Trimver2/most_common_board:",most_common_board)
    # print("Trimver2/Leaderboard:",Leaderboard)

    for i,_ in most_common_board:
        new_board.append(Leaderboard[i])
    return new_board


# Spectrum = [0,71,87,101,113,158,184,188,259,271,372]
# candidates = "LAST ALST TLLT TQAS".split()
# N=3
# Leaderboard = []
#
# for t in candidates:
#     peptide = []
#     for c in t:
#         peptide.append(aminoAcidMass[c])
#     Leaderboard.append(peptide)
# print(Trim(Leaderboard,Spectrum,N))


def LeaderboardCyclopeptideSequencing(Spectrum,N, mass_aa_list = mass_of_aa):
    Leaderboard = [[]]
    LeaderPeptide = []
    ParentMass = max(Spectrum)
    # print("Parent Mass:", ParentMass)
    score_leaderpeptide = 0
    # index = 0

    while not not Leaderboard:
        Leaderboard = Expand(Leaderboard,mass_aa_list)

        # index += 1
        # print("\n\n The loop: ", index, "time")
        #
        print("Leader Board:",Leaderboard)
        # print("Len leader board:",len(Leaderboard))

        # num_of_pop = 0
        choose_board = []
        for peptide in Leaderboard:
            mass_peptide = Mass(peptide)
            #print(mass_peptide)
            if mass_peptide == ParentMass:
                score_peptide = ScoreLinearPeptide(peptide,Spectrum)
                if score_peptide >= score_leaderpeptide:
                    LeaderPeptide = peptide
                    print("if score_peptide >= score_leaderpeptide: ",peptide,"\n",score_peptide)
                    score_leaderpeptide = score_peptide

            elif mass_peptide < ParentMass:
                choose_board.append(peptide)
                # num_of_pop +=1

                # while peptide in Leaderboard:
                #     print("POP PEPTIDE:",peptide)
                #
                #     print("Length of Leaderbord:", len(Leaderboard))
        # print("Num of pop:",num_of_pop)
        print("Choose_Board:",choose_board)
        Leaderboard = Trim(choose_board,Spectrum,N)
        # print(len(Leaderboard))
        # print("LeaderBoard after loop and is ranked top N peptide that is highest score:\n", Leaderboard, "\n" )

    return LeaderPeptide

def LCS_ver2(Spectrum, N, num_return):
    Leaderboard = [[]]
    LeaderPeptide = []
    ParentMass = max(Spectrum)
    score_leaderpeptide = 0
    candidatepeptides = []

    while not not Leaderboard:
        Leaderboard = Expand(Leaderboard)
        chooseboard = []
        for peptide in Leaderboard:
            mass_peptide = Mass(peptide)
            if mass_peptide == ParentMass:
                candidatepeptides.append(peptide)
                # score_peptide = ScoreCyclePeptide(peptide,Spectrum)
                # if score_peptide >= score_leaderpeptide:
                #     candidatepeptides.append(peptide)
                #     score_leaderpeptide = score_peptide
                    # chooseboard.append(peptide)
            elif mass_peptide < ParentMass:
                chooseboard.append(peptide)
        # print("Leaderboard: ", Leaderboard)
        # print("candidate peptides:",candidatepeptides)

        Leaderboard = Trim(chooseboard,Spectrum,N)

    # print(candidatepeptides)

    return Trim_ver2(candidatepeptides,Spectrum,num_return)



N = 10
Spectrum = [0,71,113,129,147,200,218,260,313,331,347,389,460]



def convert_ouput(raw_output):
    str_output = ""

    for num in raw_output:
        str_output += str(num) + "-"

    return str_output[:-1]
# print(convert_ouput(LeaderboardCyclopeptideSequencing(Spectrum,N)))

def convert_input(raw_input):
    lis_in = raw_input.split("\n")
    N = int(lis_in[0])
    lis_in = lis_in[1].split()
    spectrum = []

    for m in lis_in:
        spectrum.append(int(m))

    return N,spectrum

def convert_output_ver2(raw_output):
    str_ouput = ""

    for pep in raw_output:
        for num in pep:
            str_ouput += str(num) + "-"
        str_ouput = str_ouput[:-1] + "\n"

    return str_ouput[:-1]
# print(convert_output_ver2(LCS_ver2(Spectrum,N)))