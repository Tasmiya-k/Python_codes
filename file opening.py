#Use open funtion to read the content of file

#f=open('readfil.txt','r')
f=open('readfil.txt')            #by default the mode is r
#data= f.read()
#data= f.read(5)              #it reads 5 starting characters
data=f.readline()             #it will reads 1st line
print(data,end="")
data=f.readline()             #it will read 2nd line
print(data)
f.close()



