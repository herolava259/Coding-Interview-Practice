from convert_list_to_string import list_to_string

def HammingDistance(pat1,pat2):
    n = len(pat1)
    count =0
    for i in range(n):
        if pat1[i] !=pat2[i]:
            count +=1
    return count

def Neighbors(Pattern,d):
    nucleotides = {"A","C","G","T"}
    if d ==0:
        return {Pattern}
    if len(Pattern) ==1:
        return nucleotides

    Neighborhood = set()
    SuffixNeighbors = Neighbors(Pattern[1:],d)
    suff_pat = Pattern[1:]
    for txt in SuffixNeighbors:
        if HammingDistance(txt,suff_pat) < d:
            for c in nucleotides:
                Neighborhood.add(c+txt)
        else:
            Neighborhood.add(Pattern[0]+txt)
    return Neighborhood

filename = "C://Users\Admin\Desktop\dataset_3014_4.txt"
in_put = []
with open(filename,"r") as file:
    in_put = file.read().split()

pattern,d = in_put

set_neighbor = Neighbors(pattern,int(d))
str_neighbor = ""

for txt in set_neighbor:
    str_neighbor += " " + txt
filename = "result.txt"
with open(filename, "w")as file:
    file.write(str_neighbor)