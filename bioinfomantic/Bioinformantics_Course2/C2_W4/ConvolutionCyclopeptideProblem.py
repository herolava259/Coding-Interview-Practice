from C2_W4.SpectralConvolutionProblem import SpectralConvolutionSet
from collections import Counter
from C2_W4 import LeaderboardCyclopeptideProblem as LCP

def Top_M_convoluntion_of_spectrum(spectrum,M,start = 57, end=200):

    covolution_table = Counter(SpectralConvolutionSet(spectrum))
    covolution_keys = list(covolution_table.keys())
    topM_needchoose = Counter()
    for i in range(start,end+1,1):
        if i in covolution_keys:
            topM_needchoose[i] = covolution_table[i]

    m_most_commons = topM_needchoose.most_common(M)
    topM_mass = []
    for i,_ in m_most_commons:
        topM_mass.append(i)
    return topM_mass

spectrum = [57,57,71,99,129,137,170,186,194,208,228,265,285,299,307,323,356,364,394,422,493]

def ConvolutionCyclopetideSequecing(M,N,spectrum,start=57,end=200):
    mass_aa_list = Top_M_convoluntion_of_spectrum(spectrum,M,start,end)
    print("Mass_aa_list:",mass_aa_list,"\n\n")
    return LCP.LeaderboardCyclopeptideSequencing(spectrum,N,mass_aa_list)

print(Top_M_convoluntion_of_spectrum(spectrum,20))
print("Peptide need find:",ConvolutionCyclopetideSequecing(20,60,spectrum))

peptide =[99,71,137,57,72,57]
print("Real Score",LCP.ScoreLinearPeptide(peptide,spectrum))
