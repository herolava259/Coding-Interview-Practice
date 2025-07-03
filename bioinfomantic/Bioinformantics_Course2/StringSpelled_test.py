from C2_W1 import StringSpelled_by_a_GAT
from Convert_Data import list_to_string

filename = "C://Users\Admin\Desktop\dataset_198_3.txt"
in_put = []

with open(filename, "r") as file:
    in_put = file.read().split()

out_put = StringSpelled_by_a_GAT.PathToGenome(in_put)

filename = "result.txt"

with open(filename, "w") as file:
    file.write(out_put)


