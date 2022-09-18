#name=input("enter your username")

#if(len(name)<10):#
#      print("user name is valid")
#else:
#    print("invalid username")


list=["tas", "khan", "hello", 3, False]
#if(name in list):
#    print("the word is there in list")
#else:
#    print("the word is not there in list")

m=int(input("enter the marks "))
if(90<m<100):
    print("Your grade is E")
elif(80<m<90):
    print("Your grade is A")
elif(70<m<80):
    print("Your grade is B")
elif(60<m<70):
    print("Your grade is C")
elif(50<m<60):
    print("Your grade is D")
else:
    print("Your grade is F")
