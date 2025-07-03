def Suffix(Pattern):
    return Pattern[1:]


def Prefix(Pattern):
    return Pattern[0:-1]

def PathToGenome(Path):
    SEQ = ''
    n = len(Path)
    for i in range(n):
        if i == 0 or i == n:
            SEQ += Path[i]
        else:
            SEQ += Path[i][-1]

    return SEQ

# Function to generate all the b-strings

def binList(bits):
    binaryList = []
    for i in range(2**bits):
        format = '0' + str(bits) + 'b'
        binaryList.append(f"{i:{format}}")

    return binaryList

# Main Function for k-universal

def kUniversal(binaryList):
    def wrapper(elem, binaryList, bString, N):
        glSol = []
        n = len(binaryList)

        for i in range(n):
            if Suffix(elem) == Prefix(binaryList[i]):
                bString.append(binaryList[i])

                if len(bString) == N:
                    glSol.append(bString.copy())
                    bString.pop()
                    continue

                glSol.extend(wrapper(binaryList[i], binaryList[0:i] +
                                     binaryList[i + 1:], bString, N))
                bString.pop()  # Backtracking

        return glSol

    bString = []
    gSol = []
    n = len(binaryList)

    for i in range(n):
        bString.append(binaryList[i])
        gSol.extend(wrapper(binaryList[i], binaryList[0:i] +
                            binaryList[i + 1:], bString, n))
        bString.pop()  # Backtracking

    return gSol  # Return Global Solutions


binaryList = binList(4)
print(f"binaryList:\t{binaryList}")
kuni = kUniversal(binaryList)
print(len(kuni))
# Converting the paths to genome sequences
for ku in kuni:
    print(PathToGenome(ku))