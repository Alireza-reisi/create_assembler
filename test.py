# x=0
# if x==0:
#     print("yes")


def Three_Bitter(x):
    if x<10:
        return "00"+str(x)
    elif x<100:
        return "0" +str(x)
    elif x<1000: 
        return ""  +str(x)
    
print(Three_Bitter(2))
print(Three_Bitter(23))
print(Three_Bitter(223))