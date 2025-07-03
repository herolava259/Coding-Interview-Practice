from collections import defaultdict

filename = "C://Users\Admin\Desktop\RNA_codon_table_1.txt"
str_codon = ""
with open(filename, 'r') as file:
    str_codon = file.read().split('\n')

codon_table = defaultdict(str)

for line in str_codon:

    its = line.split()
    #print(its)

    if len(its)  == 1:
        continue

    codon_table[its[0]] = its[1]
#print(codon_table)
def Translation_Protein(RNA_string, GeneticCode):

    protein = ""

    for i in range(0,len(RNA_string),3):

        #print(RNA_string[i:i+3])
        codon = GeneticCode[RNA_string[i:i+3]]
        if(not codon):
            continue

        protein += codon
    return protein
filename = ""


RNA = "AUGGC"


#print(Translation_Protein(RNA, codon_table))

