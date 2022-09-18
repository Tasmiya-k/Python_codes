def greatestof3(a,b,c):
    if(a>b):
        num1=a
    else:
        num1=b

    if(num1>c):
        print(num1)
    else:
        print(c)
#a=int(input("enter 1st no "))
#b=int(input("enter 2nd no "))
c=int(input("enter 3rd no "))
#greatestof3(a,b,c)

def faran(deg):
    return (deg*(9/5))+32

print(faran(c))


