i=1
while i<=5:
   print(i*"*")
   i+=1

i=5
while i>=0:
    print(i*"*")
    i-=1

for i in range(5):
    print(i)

marks=[95,96,98]
marks.append(99)
print(marks)

marks.insert(0,100)
print(marks)

print(99 in marks)        #check karenga
print(len(marks))         #length of marks
marks.clear()
print(marks)
