def HammingDistance(text1,text2):
    n = len(text2)
    ham_dis=0
    for i in range(n):
        if text1[i] != text2[i]:
            ham_dis +=1
    return ham_dis

lis_txt = []
filename = "C://Users\Admin\Desktop\dataset_9_3.txt"
with open(filename, "r") as file:
    lis_txt = file.read().split()

text1, text2 = lis_txt

print(HammingDistance(text1,text2))