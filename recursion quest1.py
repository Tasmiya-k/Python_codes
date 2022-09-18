def sumofn(n):

    if n==0:
        return n

    return n+sumofn(n-1)

n=int(input("enter the no"))
#print(sumofn(n))


for i in range(n):
    print("*"*(n-i))

