from C2_W3.CyclopeptideSequencingProblem import output_string, mass_of_aa

filename = "C://Users\Admin\Desktop\dataset_100_6.txt"
in_put = []
with open(filename, "r") as file:
    in_put = file.read().split()

Spectrum = []
for c in in_put:
    Spectrum.append(int(c))

print(output_string(Spectrum,mass_of_aa))