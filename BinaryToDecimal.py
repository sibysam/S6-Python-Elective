bin1=input("\nEnter Binary Number: ")
int1=0
for i in range(-1,-(len(bin1)+1),-1):

    if bin1[i]=="1":
        int1+=(2**((-i)-1))

print("\nInteger Value :",int1)