

filename = "C://Users\Admin\Desktop\integer_mass_table.txt"
in_put = []

with open(filename, "r") as file:
    in_put = file.read().split("\n")

mass_table = {}

for line in in_put:
    if len(line) <1:
        continue
    elems = line.split()
    mass_table[elems[0]] = int(elems[1])

def ListOfSubPeptides(peptide):

    subpeptides = [""]
    n = len(peptide)
    for i in range(n-1):
        for j in range(n):
            k = i+1+j
            if k > n:
                subpeptides.append(peptide[j:]+peptide[0:k-n])
            else:
                subpeptides.append(peptide[j:j+i+1])

    subpeptides.append(peptide)
    return subpeptides

Peptide = "IDKRKRLIFLFCW"
#print(ListOfSubPeptides(peptide=Peptide))
                

def MassOfExperimentalSpectrum(Peptide,mass_table):

    massofsubpeptides = []

    subpeptides = ListOfSubPeptides(Peptide)

    for spep in subpeptides:
        mass_pep = 0
        for aa in spep:
            mass_pep += mass_table[aa]
        massofsubpeptides.append(mass_pep)

    massofsubpeptides.sort()

    return massofsubpeptides

def string_output(Peptide,mass_table):
    lis_output = MassOfExperimentalSpectrum(Peptide,mass_table)
    str_out = str(lis_output[0])

    for m in lis_output[1:]:
        str_out += " " + str(m)

    return str_out

#print(string_output(Peptide,mass_table))