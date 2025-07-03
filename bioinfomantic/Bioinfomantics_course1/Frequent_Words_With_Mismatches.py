from collections import defaultdict
from collections import Counter
from convert_list_to_string import list_to_string
from base_exchange import ReverseComp
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


def FrequentWordsWithMatches(text,k,d):
    patterns = []
    freqMap = defaultdict(int)
    n = len(text)
    for i in range(n-k+1):
        pat = text[i:i+k]
        neighborhood = list(Neighbors(pat,d))
        for j in range(len(neighborhood)):
            freqMap[neighborhood[j]] +=1
    max_freq = Counter(freqMap).most_common(1)[0][1]
    for key in freqMap.keys():
        if freqMap[key] == max_freq:
            patterns.append(key)
    return patterns

filename = "C://Users\Admin\Desktop\dataset_9_10.txt"
in_put = []
with open(filename,"r") as file:
    in_put =file.read().split()

text,k,d = in_put
list_output = FrequentWordsWithMatches(text,int(k),int(d))
list_output2 = FrequentWordsWithMatches(ReverseComp(text),int(k),int(d))
str_output = list_to_string(list_output)
str_output2 = list_to_string(list_output2)

with open("result.txt","w") as file:
    file.write(str_output+" "+str_output2)

txt1 ="TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
txt2 ="GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"
print(HammingDistance(txt1,txt2))