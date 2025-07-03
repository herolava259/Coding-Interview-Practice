from C2_W2 import EulerCycle

from Convert_Data import list_to_string


filename = "C://Users\Admin\Desktop\dataset_203_2 (1).txt"
in_put = []
with open(filename, "r") as file:
    in_put = file.read().split("\n")

out_put = EulerCycle.RealEulerCycler(in_put)

with open("result.txt", "w") as file:
    file.write(out_put)

print(out_put)