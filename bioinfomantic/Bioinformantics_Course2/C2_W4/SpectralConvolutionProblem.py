
def SpectralConvolutionSet(spectrum):
    n = len(spectrum)
    convolution_set = []
    for i, pep in enumerate(spectrum):
        for i in range(i+1,n,1):
            convolution_set.append(abs(pep-spectrum[i]))

    return convolution_set

spectrum = [0,137,186,323]

# print(SpectralConvolutionSet(spectrum))

def convert_input(raw_input):
    spectrum = []
    lis_str = raw_input.split()
    for s in lis_str:
        spectrum.append(int(s))
    return spectrum
def convert_output(raw_output):
    str_out = ""
    for c in raw_output:
        str_out += str(c) + " "

    return str_out[:-1]
# print(convert_output(SpectralConvolutionSet(spectrum)))
#
# filename = "C://Users\Admin\Desktop\dataset_104_4.txt"
# raw_input = ""
#
# with open(filename, "r") as file:
#     raw_input = file.read()
#
# Spectrum = convert_input(raw_input)
#
# print(convert_output(SpectralConvolutionSet(Spectrum)))
