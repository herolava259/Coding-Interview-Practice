from math import log2

def ReverseComp(text):
    reverse_txt = ""
    for c in text:
        if c == "A":
            reverse_txt = "T" + reverse_txt
        elif c == "T":
            reverse_txt = "A" + reverse_txt
        elif c == "G":
            reverse_txt = "C" + reverse_txt
        elif c == "C":
            reverse_txt = "G" + reverse_txt

    return reverse_txt