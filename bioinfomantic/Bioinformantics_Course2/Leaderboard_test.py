from C2_W4.LeaderboardCyclopeptideProblem import LeaderboardCyclopeptideSequencing,convert_ouput,convert_input

filename = "C://Users\Admin\Desktop\dataset_102_10.txt"
in_put = ""
with open(filename, "r") as file:
    in_put = file.read()

N, Spectrum = convert_input(in_put)

print(convert_ouput(LeaderboardCyclopeptideSequencing(Spectrum,N)))