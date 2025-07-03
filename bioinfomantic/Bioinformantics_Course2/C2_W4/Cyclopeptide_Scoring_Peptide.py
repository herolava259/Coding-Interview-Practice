from collections import Counter


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

def Subpeptides(Peptide):
    lis_subpeptides = ["",Peptide]
    n = len(Peptide)
    for i in range(n):
        for j in range(1,n,1):
            subpep = ""
            k = i+j
            if k > n:
                subpep += Peptide[i:n] + Peptide[0:k-n]
            else:
                subpep += Peptide[i:k]
            lis_subpeptides.append(subpep)

    return lis_subpeptides


def MassofSubpeptides(Peptide,mass_table):

    subpeptides = Subpeptides(Peptide)
    #print(subpeptides)
    spectrum = []
    for subpep in subpeptides:
        mass = 0
        for aa in subpep:
            mass += mass_table[aa]
        spectrum.append(mass)

    spectrum.sort()
    return spectrum



def Cyclopeptide_Scoring(Peptide, Spectrum):

    theoretical_spectrum = MassofSubpeptides(Peptide,aminoAcidMass)
    #print(theoretical_spectrum)
    theorem_table = Counter(theoretical_spectrum)
    #print(theorem_table)
    experi_table = Counter(Spectrum)
    #print(experi_table)
    element_exp = list(experi_table.elements())
    #print("element_exp",element_exp)
    score = 0
    for c in theorem_table:
        #print("theorem:",c)
        if c in element_exp:
            #print(c)
            if theorem_table[c] >= experi_table[c]:
                score += experi_table[c]
            else:
                score += theorem_table[c]

    return score

# Peptide = "NQEL"
#
# Spectrum = [0,99,113,114,128,227,257,299,355,356,370,371,484]
#
# print(Cyclopeptide_Scoring(Peptide,Spectrum))
