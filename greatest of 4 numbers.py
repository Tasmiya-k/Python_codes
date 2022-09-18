#greatest of 2 numbers

a=int(input("enter no1 "))
b=int(input("enter n02 "))
c=int(input("enter n03 "))
d=int(input("enter n04 "))

if(a>b):
    f1=a
else:
    f1=b

if(c>d):
    f2=c
else:
    f2=d

if(f1>f2):
    print(str(f1),"is the greatest")
else:
    print(str(f2),"is the greatest")


