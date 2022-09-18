#pattern 1
'''n=int(input("enter n "))
for i in range(n+1):
    print("*"*i)'''

#pattern 2
n=int(input("enter n "))

'''for i in range(n):
    print(" "*(n-i-1), end=" ")
    print("*"*(2*i+1), end=" ")
    print(" "*(n-i-1))'''

#pattern 3
for i in range(n):
    for j in range(n):

        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")








