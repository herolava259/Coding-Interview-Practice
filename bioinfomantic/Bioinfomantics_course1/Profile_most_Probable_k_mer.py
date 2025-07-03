

def Prob_k_mer(k_mer, Profile):
    Prob = float(1)
    for i,c in enumerate(k_mer):
        Prob *= Profile[c][i]
        #print(Prob)

    return Prob

def list_to_dict(Profile):
    profile_dict = {}

    for i,c in enumerate("ACGT"):
        profile_dict[c] = Profile[i]

    return profile_dict

def Most_probable_k_mer(txt,k,Profile):

    if type(Profile) == type([]):
        Profile = list_to_dict(Profile)

    prob = float(0)

    n = len(txt)

    most_k_mer = txt[0:k]
    for i in range(n-k+1):
        tmp =  Prob_k_mer(txt[i:i+k],Profile)
        #print(tmp)
        #print(txt[i:i+k])
        #print("\n")
        if tmp > prob:
            prob =  tmp
            most_k_mer = txt[i:i+k]


    return most_k_mer


def convert_data(in_put):
    lis1 = in_put.split("\n")
    txt = lis1[0]
    k = int(lis1[1])
    profile_str = lis1[2:]

    matrix_profile = []
    for str_row in profile_str:
        str_list = str_row.split()
        str_float = []

        for c in str_list:
            str_float.append(float(c))

        matrix_profile.append(str_float)

    return txt, k, matrix_profile

raw_txt = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT\n5\n0.2 0.2 0.3 0.2 0.3\n0.4 0.3 0.1 0.5 0.1\n0.3 0.3 0.5 0.2 0.4\n0.1 0.2 0.1 0.1 0.2'

filename = "C://Users\Admin\Desktop\dataset_159_3 (1).txt"
with open(filename,"r") as file:
    raw_txt = file.read()

txt,k,profile = convert_data(raw_txt)




print(Most_probable_k_mer(txt,k,profile))
