from collections import Counter
from collections import defaultdict

def FrequencyTable(Text,k):

    freq_map = defaultdict(int)
    n = len(Text)

    for i in range(n-k+1):
        pattern = Text[i:i+k]
        freq_map[pattern] +=1

    return Counter(freq_map)

def FindClumps(Text, k, L, t):

    Patterns = []

    n = len(Text)

    for i in range(n-L+1):
        window = Text[i:i+L]
        freq_Map = FrequencyTable(window,k)
        #print(freq_Map)
        for key in freq_Map.keys():
            if freq_Map[key] >= t:
                Patterns.append(key)

    return list(set(Patterns))

filename ="C://Users\Admin\Desktop\dataset_4_5.txt"

with open(filename, "r") as file:
    doc = file.read().split()

#print(doc)
Text = doc[0]
k,L,t= doc[1:]

tmp =FindClumps(Text,int(k), int(L), int(t))

for i in range(len(tmp)):
    print(tmp[i])