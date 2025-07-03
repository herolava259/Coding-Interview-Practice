from C2_W4.LeaderboardCyclopeptideProblem import LCS_ver2
from C2_W4.LeaderboardCyclopeptideProblem import convert_output_ver2
from C2_W4.LeaderboardCyclopeptideProblem import convert_input
from C2_W4.LeaderboardCyclopeptideProblem import ScoreCyclePeptide

filename = "C://Users\Admin\Desktop\dataset_102_10.txt"
raw_input = ""
with open(filename, "r") as file:
    raw_input = file.read()

N,spectrum = convert_input(raw_input)

peptide = [97,147,113,128,99,163,71,57,57,57,147,115,71]


print(convert_output_ver2(LCS_ver2(spectrum,N,40)))
print(ScoreCyclePeptide(peptide,spectrum))