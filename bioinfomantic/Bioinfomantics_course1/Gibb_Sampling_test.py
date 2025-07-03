from Bio_w4 import Gibb_Sampling
from convert_list_to_string import list_to_string

in_put = []
filename = "C://Users\Admin\Desktop\dataset_161_5.txt"
with open(filename,"r") as file:
    in_put = file.read().split()



Dna = in_put[3:]
k,t,N = int(in_put[0]), int(in_put[1]), int(in_put[2])

print("My output:\n")
#out_put = Gibb_Sampling.GibbsSampler(Dna,k,t,N)
print(Gibb_Sampling.GibbsSampler(Dna,k,t,2000))
#print(list_to_string(out_put[0]))
print("\n")

filename ="C://Users\Admin\Desktop\Test.txt"
out_put = ""
with open(filename, "r") as file:
    out_put = file.read()

print("Accurate results:\n")
#print(out_put)
