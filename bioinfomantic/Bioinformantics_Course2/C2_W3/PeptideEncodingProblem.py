from C2_W3.Protein_Translation_Problem import codon_table, Translation_Protein


def ReverseComplementDNA(DNA):

    reverse_pat = ""
    comp_nucle = {"A":"T","G":"C","T":"A","C":"G"}
    for c in DNA:
        reverse_pat = comp_nucle[c] +reverse_pat

    return reverse_pat

def Transcribed(DNA):

    RNA = ""

    map_rna = {"A":"A", "T":"U","G":"G","C":"C"}
    for c in DNA:
        RNA += map_rna[c]

    return RNA


def PeptideEncoding(DNA, Peptide, GeneticCode):

    ReverseDNA = ReverseComplementDNA(DNA)
    RNA = Transcribed(DNA)


    RevRNA = Transcribed(ReverseDNA)

    DNAs = [DNA, DNA[1:], DNA[2:], ReverseDNA, ReverseDNA[1:], ReverseDNA[2:]]
    RNAs = [RNA,RNA[1:],RNA[2:],RevRNA,RevRNA[1:],RevRNA[2:]]

    proteins = [Translation_Protein(rna,GeneticCode) for rna in RNAs]


    for p in proteins:
        print(p)

    k = len(Peptide)


    substrings = []

    for j,protein in enumerate(proteins):

        n = len(protein)
        print(n)
        for i in range(0,n-k+1):


            if j < 3:
                if protein[i:i + k] == Peptide:
                    print(protein[i:i+k])
                    print(j)
                    substrings.append(DNAs[j][3 * i:3 * (i + k)])
            else:
                if protein[i:i+k] == Peptide:
                    print(j)
                    print(protein[i:i + k])

                    substrings.append(ReverseComplementDNA(DNAs[j][3*i:3*(i+k)]))


    substrings = list((substrings))

    return substrings

filename = "C://Users\Admin\Desktop\Bacillus_brevis.txt"

with open(filename, "r") as file:
    in_put = file.read().split()

DNA = ""

for line in in_put:
    DNA += line

Peptide = "VKLFPWFNQY"


out_put = PeptideEncoding(DNA,Peptide,codon_table)

for arr in out_put:
    print(arr)

print(len(out_put))
