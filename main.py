class SymbolicOPCode():
    def __init__(self,Input):
        self.Loc=None
        self.HLTflag=False
        self.op_code=[[None for i in range(3)] for j in range (len(Input)-self.ORGCounter(len(Input),Input))]
        
           
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
        
    def ORGCounter(self,n,Input):
        count=0
        for i in range(n):
            if Input[i][0]=="ORG":
                count+=1
        return count
    
    def Run(self,Input):
        for i in range (len(Input)):
            if (Input[i][0]=="ORG"):
                self.OH(int(Input[i][1]))
                
            elif(Input[i][0]=="HLT" or Input[i][0]=="END"):
                if (Input[i][0]=="END"):
                    self.op_code[-1][0]=self.Three_Bitter(self.Loc)
                    self.op_code[-1][1]=self.Three_Bitter(0)
                    return
                elif (Input[i][0]=="HLT"):
                    ORGCounter=self.ORGCounter(i,Input)
                    self.op_code[i-ORGCounter][0]=self.Three_Bitter(self.Addressing())
                    self.op_code[i-ORGCounter][1]=Input[i][0]
                    self.OH(Input[i][0])
                
            elif(self.HLTflag==False):
                ORGCounter=self.ORGCounter(i,Input)
                Address=self.Three_Bitter(self.Addressing())
                self.op_code[i-ORGCounter][0]=Address
                self.op_code[i-ORGCounter][1]=Input[i][0]
                
            elif(self.HLTflag==True):
                Address=self.Three_Bitter(self.Addressing()) 
                for j in range (len(Input)):
                    if Input[j][0]=="HLT" or Input[j][0]=="END" :
                        break
                    if (len(Input[j])>=3):
                        if Input[j][1]==Input[i][0]:
                            ORGCounter=self.ORGCounter(j,Input)
                            self.op_code[j-ORGCounter][2]=Address
                ORGCounter=self.ORGCounter(i,Input)
                self.op_code[i-ORGCounter][0]=Address
                self.op_code[i-ORGCounter][1]=self.ToHex(int(Input[i][2]))
                
                
# -----------------------------------------------------------------------------------

class HexaProgram():
    def __init__(self,op_code):
        self.OPCodeList=op_code #op_code is an object for "class SymbolicOPCode()"
        self.Hex_Program=[[None for i in range(2)] for j in range (len(self.OPCodeList.op_code))]
    
    
    def OPCodeBuilder(self,op_code,address): # get 3 bit address and an Instructions and return 4 bit op-code
        if op_code=="ADD":
            x="0"
            return x+str(address)
        elif op_code=="AND":
            x="1"
            return x+str(address)
        elif op_code=="LDA":
            x="2"
            return x+str(address)
        elif op_code=="STA":
            x="3"
            return x+str(address)
        elif op_code=="BUN":
            x="4"
            return x+str(address)
        elif op_code=="BSA":
            x="5"
            return x+str(address)
        elif op_code=="ISZ":
            x="6"
            return x+str(address)
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        elif op_code=="ISZ":
            pass
        
    def Run(self):
        for i in range(len(self.OPCodeList.op_code)):
            self.Hex_Program[i][0]=self.OPCodeList.op_code[i][0]
            self.Hex_Program[i][1]=self.OPCodeBuilder(self.OPCodeList.op_code[i][1],self.OPCodeList.op_code[i][2])
        


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

OP_Code_List=SymbolicOPCode(Input)
OP_Code_List.Run(Input)

for i in range (len(OP_Code_List.op_code)):
    print(OP_Code_List.op_code[i])

# --------------------
print("---------------")
# --------------------
# Hexa program List:


# hex_List=HexaProgram(OP_Code_List)
# hex_List.Run()


# for i in range (len(hex_List.Hex_Program)):
#     print(hex_List.Hex_Program[i])
