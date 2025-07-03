from C2_W2.Reconstruction_from_Reads_Pairs_Problem import ReFromReadPairs

filename = "C://Users\Admin\Desktop\dataset_204_16.txt"
in_put = []

with open(filename, "r") as file:
    in_put = file.read().split()

k = int(in_put[0])
d = int(in_put[1])

out_put = ReFromReadPairs(k,d,in_put[2:])

print(out_put)