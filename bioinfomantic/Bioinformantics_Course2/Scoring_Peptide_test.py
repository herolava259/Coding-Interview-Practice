from C2_W4.Cyclopeptide_Scoring_Peptide import Cyclopeptide_Scoring

def convert_input(in_put):
    arr = in_put.split("\n")
    Peptide = arr[0]
    raw_spectrum = arr[1].split()
    spectrum = []
    for c in raw_spectrum:
        if c != "":
            spectrum.append(int(c))

    return Peptide,spectrum

filename = "C://Users\Admin\Desktop\dataset_102_3.txt"
in_put = ""

with open(filename, 'r') as file:
    in_put = file.read()

Peptide, Spectrum = convert_input(in_put)

print(Cyclopeptide_Scoring(Peptide,Spectrum))

