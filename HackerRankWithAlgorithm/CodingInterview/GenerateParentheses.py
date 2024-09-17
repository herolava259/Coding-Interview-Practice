import copy

def generate_parentheses(n ,s_open,  oc):
    if n==0:
        for i in range(s_open):
            oc+=")"
        print(oc)
        return

    if  s_open > 0:
        origin = str(oc)
        oc+= ")"
        s_open -= 1
        generate_parentheses(n,s_open,oc)
        oc = origin
        s_open +=1

    origin = str(oc)
    oc += "("
    s_open+=1
    generate_parentheses(n-1,s_open,oc)
    s_open -=1
    oc = origin

print(generate_parentheses(3,0,""))
