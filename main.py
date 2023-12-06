class SymbolicOPCode():
    def __init__(self,Input):
        self.Loc=None
        self.HLTflag=False
        self.op_code=[[None for i in range(3)] for j in range (len(Input)-3)]
        self.Hex_Program=[[0 for i in range(2)] for j in range (len(Input))]
           
    def OH(self,Var): # ORG - HLT - END
        if(Var=="HLT"):
            self.HLTflag=True
            
        else:
            self.Loc=Var

    def Addressing(self):
        R=self.Loc
        self.Loc+=1
        return R
    
    def ToHex(self,x):
        if x<0:
            x=hex(x)[3:]
            x="-"+x
            return x
        else:
            return (hex(x)[2:])
        
    def Three_Bitter(self,x):
        if x<10:
            return "00"+str(x)
        elif x<100:
            return "0" +str(x)
        elif x<1000: 
            return ""  +str(x)
        
    def Run(self,Input):
        for i in range (len(Input)):
            if (Input[i][0]=="ORG"):
                self.OH(int(Input[i][1]))
                
            elif(Input[i][0]=="HLT" or Input[i][0]=="END"):
                if (Input[i][0]=="END"):
                    self.op_code[-1][0]=self.Three_Bitter(self.Loc)
                    return
                elif (Input[i][0]=="HLT"):
                    self.OH(Input[i][0])
                
            elif(self.HLTflag==False):
                Address=self.Three_Bitter(self.Addressing())
                self.op_code[i-1][0]=Address
                self.op_code[i-1][1]=Input[i][0]
                
            elif(self.HLTflag==True):
                Address=self.Three_Bitter(self.Addressing()) 
                for j in range (len(Input)):
                    if Input[j][0]=="HLT":
                        break
                    elif Input[j][1]==Input[i][0]:
                        self.op_code[j-1][2]=Address
                self.op_code[i-2][0]=Address
                self.op_code[i-2][1]=self.ToHex(int(Input[i][2]))



# getting input:
Input=[]
with open("input.txt") as w_input:
    length=len(w_input.readlines())
with open("input.txt") as w_input:
    for i in range (length):
        Input.append(w_input.readline())
        Input[i]=Input[i].upper()
        Input[i]=Input[i].split()



#--------------------
# Symbolic OP-Code List:

OP_Code=SymbolicOPCode(Input)
OP_Code.Run(Input)
for i in range (len(OP_Code.op_code)):
    print(OP_Code.op_code[i])

