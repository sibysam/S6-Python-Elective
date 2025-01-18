num1=int(input("\nEnter a Number: "))

if num1<2:
    print("\nSquare Root: ",num1)
else:
    a=num1
    b=(a+(num1/a))/2
    while abs(b-a)>= 0.000001:
        a=b
        b=(a + (num1/a))/2
    print("\nSquare Root: ",b)