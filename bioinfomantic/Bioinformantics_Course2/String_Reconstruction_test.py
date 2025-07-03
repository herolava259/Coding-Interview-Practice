from C2_W2.String_Reconstruction import StringReconstruction

filename = "C://Users\Admin\Desktop\dataset_203_7.txt"
in_put = []

with open(filename, "r") as file:
    in_put = file.read().split()

k = int(in_put[0])
patterns = in_put[1:]

out_put = StringReconstruction(k,patterns)

print(out_put)