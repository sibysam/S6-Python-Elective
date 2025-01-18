message = input("\nEnter the Message: ")
key = int(input("Enter the Key : "))
encmsg=""

for ch in message:
    x=ord(ch)
    x+=key
    if x > ord("z"):
        x=ord("a")+(x-ord("z"))-1
    encmsg+=chr(x)
print("\nEncoded Message : ",encmsg)


decmsg=""
for ch in encmsg:
    x=ord(ch)
    x-=key
    if x < ord("a"):
        x=ord("z")-(ord("a")-x)+1
    decmsg+=chr(x)
print("\nEncoded Message : ",decmsg)

if message==decmsg:
    print("\nGiven Message is Encoded Message\n")
else:
    print("\nGiven Message is Not Encoded Message\n")
