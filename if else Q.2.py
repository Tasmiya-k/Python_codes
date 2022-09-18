num1=int(input("enter marks of subj 1 "))
num2=int(input("enter marks of subj 2 "))
num3=int(input("enter marks of subj 3 "))

m1=((num1+num2+num3)/3)

if(num1<33 or num2<33 or num3<33):
    print("you are fail bcoz you scored less than 33 in all sub")

elif(m1<40):
    print("you are fail")

else:
    print("you are pass")




