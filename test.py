from main import Input


def Addressing():
    global Loc
    R=bin(Loc)
    return(R)
    
    
    
Loc=0
with open("input.txt") as w_input:
    length=len(w_input.readlines())
with open("input.txt") as w_input:
    for i in range (length):
        Input.append(w_input.readline())
        Input[i]=Input[i].upper()
        =Input[i].split()