
aminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

def LinearSpectrum(Peptide, AminoAcidMass):
    PrefixMass = [0]
    n = len(Peptide)

    total_mass = 0

    for aa in Peptide:
        total_mass += AminoAcidMass[aa]
        PrefixMass.append(total_mass)
    spectrum = [0]
    #print(PrefixMass)
    for i in range(n):
        for j in range(i+1,n+1,1):
            spectrum.append(PrefixMass[j]-PrefixMass[i])

    spectrum.sort()

    return spectrum


Peptide = "HVEHCRQQIYMAEFYRPNQWRVNWFPINKCKSLFMKA"

out_put = LinearSpectrum(Peptide,aminoAcidMass)

str_out  = ""

for c in out_put:
    str_out += str(c) + " "
print(str_out[:-1])


