from Frequent_Words_With_Mismatches import FrequentWordsWithMatches
from convert_list_to_string import list_to_string
from base_exchange import ReverseComp

def FreqWord_and_ReverseComp_with_Mismatches(text,k,d):
    patterns = FrequentWordsWithMatches(text,k,d)
    for c in patterns:
        patterns.append(ReverseComp(c))

    return patterns

filename = "C://Users\Admin\Desktop\dataset_9_10.txt"
in_put = []
with open(filename,"r") as file:
    in_put =file.read().split()

text,k,d = in_put
list_output = FreqWord_and_ReverseComp_with_Mismatches(text,int(k),int(d))
str_output = list_to_string(list_output)

with open("result.txt","w") as file:
    file.write(str_output)