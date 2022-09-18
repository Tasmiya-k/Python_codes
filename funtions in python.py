
def percent(marks):
    p=(sum(marks)/400)*100
    return p

marks1=[96,67,87,98]
percent1=percent(marks1)

marks2=[87,78,91,90]
percent2=percent(marks2)

#print(percent1, percent2)

def greeting(name):
        print("Hello",name)

name1=(input("enter your name "))
greeting(name1)