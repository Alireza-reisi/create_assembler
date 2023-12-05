def OHE(Var): # ORG - HLT - END
    if(Var=="HLT"):
        global HLTflag
        HLTflag=True
        
    elif(Var=="END"):
        for i in range(len(op_code)):
            print(op_code[i])
        exit()
        
    else:
        global Loc
        Loc=Var


def Addressing():
    global Loc
    R=Loc
    Loc+=1
    return R
    


Input=[]
with open("input.txt") as w_input:
    length=len(w_input.readlines())
with open("input.txt") as w_input:
    for i in range (length):
        Input.append(w_input.readline())
        Input[i]=Input[i].upper()
        Input[i]=Input[i].split()

Loc=None
HLTflag=False
op_code=[[0 for i in range(3)] for j in range (len(Input)-3)]
# Hex_Program=[[0 for i in range(2)] for j in range (len(Input))]


# try:    
for i in range (len(Input)):
    if (Input[i][0]=="ORG"):
        OHE(int(Input[i][1]))
        
    elif(Input[i][0]=="HLT" or Input[i][0]=="END"):
        if (Input[i][0]=="END"):
            op_code[-1][0]=Loc
        OHE(Input[i][0])
        
    elif(HLTflag==False):
        Address=Addressing()
        op_code[i-1][0]=Address
        op_code[i-1][1]=Input[i][0]
        
    elif(HLTflag==True):
        Address=Addressing()
        for j in range (len(Input)):
            if Input[j][0]=="HLT":
                break
            elif Input[j][1]==Input[i][0]:
                op_code[j-1][2]=Address
        op_code[i-2][0]=Address
        op_code[i-2][1]=hex(int(Input[i][2]))
                        
# except:
#     print("Eror")


