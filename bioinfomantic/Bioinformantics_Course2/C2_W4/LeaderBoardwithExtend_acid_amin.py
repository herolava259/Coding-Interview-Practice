from C2_W4 import LeaderboardCyclopeptideProblem as LCP

def extend_mass_list(start, end):

    extend_list = []

    for i in range(start,end+1,1):
        extend_list.append(i)

    return extend_list

mass_aa_list = extend_mass_list(57,200)

filename = ""
raw_input = ""

with open(filename, "r") as file:
    raw_input = file.read()

N, spectrum = LCP.convert_input(raw_input)

print(LCP.convert_output_ver2(LCP.LCS_ver2(spectrum,N,34)))