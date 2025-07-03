from C2_W1 import StringCompositionProblem

from Convert_Data import list_to_string

filename = "C://Users\Admin\Desktop\dataset_197_3.txt"
in_put = []

with open(filename, "r") as file:
    in_put = file.read().split()

k = int(in_put[0])
txt = in_put[1]

#k = 5
#txt = "CAATCCAAC"
out_put = StringCompositionProblem.StrCompProblem(k, txt)

out_put = list_to_string(out_put)

filename = "result.txt"

with open(filename, "w") as file:
    file.write(out_put)

