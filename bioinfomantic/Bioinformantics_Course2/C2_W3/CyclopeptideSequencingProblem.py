

mass_of_aa = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

Spectrum = [0,113,128,186,241,299,314,427]

def Expand(candidates,massaa):

    new_candidates =[]
    for pep in candidates:
        for aa in massaa:
            newpep = pep.copy()
            newpep.append(aa)
            new_candidates.append(newpep)

    return new_candidates

candidates = [[0, 57], [0, 71], [0, 87], [0, 97], [0, 99], [0, 101], [0, 103], [0, 113], [0, 114], [0, 115], [0, 128], [0, 129], [0, 131], [0, 137], [0, 147], [0, 156], [0, 163], [0, 186], [113, 57], [113, 71], [113, 87], [113, 97], [113, 99], [113, 101], [113, 103], [113, 113], [113, 114], [113, 115], [113, 128], [113, 129], [113, 131], [113, 137], [113, 147], [113, 156], [113, 163], [113, 186], [128, 57], [128, 71], [128, 87], [128, 97], [128, 99], [128, 101], [128, 103], [128, 113], [128, 114], [128, 115], [128, 128], [128, 129], [128, 131], [128, 137], [128, 147], [128, 156], [128, 163], [128, 186]]


#print(Expand(candidates,mass_of_aa))



def Mass(peptide):
    total_mass = 0
    for m in peptide:
        total_mass +=m
    return total_mass


def Consistent(Spectrum, Peptide):
    mass_subpeptides = [0]
    n = len(Peptide)

    for i in range(n):
        for j in range(n-i):
            mass_subpeptides.append(Mass(Peptide[j:j+i+1]))

    mass_subpeptides.sort()
    #print(mass_subpeptides)
    max_spectrum = max(Spectrum)
    for pep in mass_subpeptides:
        if pep > max_spectrum:
            return False
        for spec in Spectrum:
            if pep == spec:
                break
            elif pep < spec:
                return False
    # print("peptideis consitent",Peptide)
    return True


# if Consistent(Spectrum,[113]):
#     print("Consistent")
# else:
#     print("Incosistent")


def Cyclospectrum(Peptide):
    n = len(Peptide)
    subpeptides = [[0],Peptide.copy()]

    for i in range(2,n,1):
        mass_length_i = []
        for j in range(n):
            mass_j = Peptide[j]
            k = (j+1)%n
            mass_j += subpeptides[i-1][k]
            mass_length_i.append(mass_j)
        #print(mass_length_i)
        subpeptides.append(mass_length_i)

    flat_arr=[]
    for lis in subpeptides:
        for item in lis:
            flat_arr.append(item)
    #print(flat_arr)
    flat_arr.append(Mass(Peptide))
    flat_arr.sort()
    return flat_arr

Peptide = [113,128,186]

# print("Cyclospectrum:",Cyclospectrum(Peptide))

def CompareCyclospectrum(Peptide,Spectrum):
    cyclespectrum = Cyclospectrum(Peptide)
    n = len(cyclespectrum)
    if n != len(Spectrum):
        return False
    for m1,m2 in zip(cyclespectrum,Spectrum):
        if m1 != m2:
            return False

    return True
# if CompareCyclospectrum(Peptide,Spectrum):
#     print("Equal")

def isInFinalPeptide(Peptide,FinalPeptides):

    for pep in FinalPeptides:
        if len(Peptide) != len(pep):
            continue
        count = 0
        for aa1,aa2 in zip(Peptide,pep):
            if aa1 != aa2:
                break
            count +=1
        if count == len(Peptide):
            return True
    return False


def CyclopeptideSequencing(Spectrum, massaa):

    CandidatePeptides = [[]]
    FinalPeptides = []
    Spectrum.sort()
    ParentMass = max(Spectrum)
    #print(ParentMass)

    # count = 0

    while not not CandidatePeptides:
        CandidatePeptides = Expand(CandidatePeptides,massaa)
        # count +=1
        # print("Cdd:",len(CandidatePeptides))
        # print(CandidatePeptides[-1])
        # LastPeptide = CandidatePeptides[0]
        NewCandiatePeptides = []
        for i,Peptide in enumerate(CandidatePeptides):

            # LastPeptide = Peptide
            if Mass(Peptide) == ParentMass:
                if CompareCyclospectrum(Peptide,Spectrum) and not isInFinalPeptide(Peptide,FinalPeptides):
                    #print("Pepetide:",Peptide)
                    FinalPeptides.append(Peptide)

            elif Consistent(Spectrum, Peptide):
                NewCandiatePeptides.append(Peptide)

        CandidatePeptides = NewCandiatePeptides
        # if count == 3:
        #     print(CandidatePeptides)
        #     print("LastPaptide:",LastPeptide)
    return FinalPeptides
#print(Expand([[]],mass_of_aa))

def output_string(Spectrum, massaa):
    lis_output = CyclopeptideSequencing(Spectrum,massaa)
    str_out = ""

    for pep in lis_output:
        for aa in pep:
            str_out +=str(aa) + "-"
        str_out = str_out[:-1]
        str_out += " "

    return str_out[:-1]

# print("Results:",CyclopeptideSequencing(Spectrum,mass_of_aa))
# print("Result:",output_string(Spectrum,mass_of_aa))