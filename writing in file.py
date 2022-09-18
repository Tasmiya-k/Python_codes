#f=open('another.txt','w')
#f.write("I am appending")
#f.close()

#read and write file with "with" statement

with open('another.txt','r') as f:
    a=f.read()
with open('another.txt','w') as f:
   a=f.write("hello")

print(a)