def HammingDistance(pattern1,pattern2):
    n = len(pattern2)
    ham_dis=0
    for i in range(n):
        if pattern1[i] != pattern2[i]:
            ham_dis +=1
    return ham_dis

def Approx_Pattern_Matching(text,pattern,d):
    n = len(text)
    k = len(pattern)
    index_lis = []
    for i in range(n-k+1):
        part = text[i:i+k]
        tmp = HammingDistance(pattern,part)
        if tmp <=d:
            index_lis.append(i)
    return index_lis

filename ="C://Users\Admin\Desktop\dataset_9_4 (2).txt"
lis = []
with open(filename,"r") as file:
    lis = file.read().split()

pattern, text, d = lis

index_lis = Approx_Pattern_Matching(text,pattern,int(d))
str_index = ""

for i in index_lis:
    str_index = str_index + " " + str(i)

filename = "result_9_4.txt"

with open(filename,'w',encoding = 'utf-8') as f:
    f.write(str_index)