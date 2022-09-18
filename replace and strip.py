def delandstrip(string,word):
    s=string.replace(word,"")
    return s.strip()

string=input("enter the string")
word=input("enter the word from string")
t=delandstrip(string,word)
print(t)