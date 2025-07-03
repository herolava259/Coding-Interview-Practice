from C2_W1 import DeBrujinGraphProblem
from Convert_Data import list_to_string
filename = "C://Users\Admin\Desktop\dataset_199_6.txt"
in_put = []

with open(filename, "r") as file:
    in_put = file.read().split()

k = int(in_put[0])
txt = in_put[1]

def convertdata(out_put):
    lis_out = []
    for pat in out_put:
        str_out = pat + " -> "
        for s in out_put[pat]:
            str_out = str_out + s + ","
        lis_out.append(str_out[:-1])
    str_out = list_to_string(lis_out)
    return str_out

out_put = DeBrujinGraphProblem.DeBrujinGraph(k,txt)

out_put = convertdata(out_put)

filename = "result.txt"

with open(filename, 'w') as file:
    file.write(out_put)
