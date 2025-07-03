from C2_W2.Eulerian_Path_Problem import EulerianPath

filename = "C://Users\Admin\Desktop\dataset_203_6.txt"
in_put = []
with open(filename, "r") as file:
    in_put = file.read().split("\n")

out_put = EulerianPath(in_put)

with open("result.txt", "w") as file:
    file.write(out_put)

print(out_put)