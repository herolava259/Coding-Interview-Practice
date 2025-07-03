
def Composition_kd(k, d, Text):
    '''Given integers k, d and a DNA string Text, return the composition of k,d-mers that make up Text. Output will be in lexicographical order.'''
    composition = []
    for i in range(len(Text)):
        start_0 = i
        end_0 = start_0 + k
        start_1 = i + k + d
        end_1 = start_1 + k
        if end_1 <= len(Text):
            kmer_0 = Text[start_0:end_0]
            kmer_1 = Text[start_1:end_1]
            composition.append([kmer_0, kmer_1])
        else:
            break
    return sorted(composition)

composition = Composition_kd(3, 2, 'TAATGCCATGGGATGTT')
print(composition)