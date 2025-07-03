from C2_W1 import DeBruijnGraph_with_k_mers_problem
from Convert_Data import list_to_string

filename = "C://Users\Admin\Desktop\dataset_200_8.txt"
in_put = []

with open(filename, "r") as file:
    in_put = file.read().split()

out_put = DeBruijnGraph_with_k_mers_problem.DeBruijnGraph(in_put)
def ConvertData(out_put):

    lis_out = []

    for first in out_put:
        str_adj = first + " -> "

        for end in out_put[first]:
            str_adj = str_adj + end +","
        lis_out.append(str_adj[:-1])

    return list_to_string(lis_out)

out_put = ConvertData(out_put)

filename = "result.txt"

with open(filename, "w") as file:
    file.write(out_put)


