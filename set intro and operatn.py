#sets in python

a={1,2,3,4,5,4}           #it does not have repeatative items
print(type(a))
print(a)

a={}                     #it is an empty dictionary
print(type(a))

#creating an empty set
b=set()
print(type(b))

#Adding values to an empty set
b.add(4)
b.add(5)
b.add(3)                  #adding a value repedetly cannot change a set
b.add(3)
b.add((4,6,3))              #we can add tuple in set but not (list, dictionary)
print(b)

#set methods
print(len(b))         #it will gives len of this set
#b.remove(5)
print(b)
#print(b.pop())
#b.clear()
#print(b)
b.union((1,2,3))
print(b)
