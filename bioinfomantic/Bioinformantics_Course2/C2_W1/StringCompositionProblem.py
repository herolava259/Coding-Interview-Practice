





def StrCompProblem(k, txt):
    
    lis_comp = []
    n = len(txt)
    for i in range(n-k+1):
        lis_comp.append(txt[i:i+k])
        
    return lis_comp
