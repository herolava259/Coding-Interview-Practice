from C2_W1 import OverlapGraphProblem
from Convert_Data import list_to_string

filename = "C://Users\Admin\Desktop\dataset_198_10.txt"
in_put = []

with open(filename, "r") as file:
    in_put = file.read().split()


col_pats = in_put

out_put = OverlapGraphProblem.OvetlapGraphStr(col_pats)

out_put = list_to_string(out_put)


filename = "result.txt"
with open(filename, "w") as file:
    file.write(out_put)

