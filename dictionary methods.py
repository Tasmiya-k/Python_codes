#dictionary methods

mydict={
   "Fast":"In a quick manner",
   "Tasmiya":"A coder",
   "marks":[1,2,3],
   "anotherdict":{'harry':'player'}
}

print(mydict.keys())              #Prints the keys in the dictionary
print(list(mydict.values()))      #prints all the values in dictionary
print(mydict.items())             #prints the keys, value of dictionary

updateDict={
"lovish":"friend",
}
mydict.update(updateDict)       #update the dic by adding values
print(mydict)
print(mydict.get('Tasmiya1'))      #if tasmiya1 is not present then it will return none
print(mydict["Tasmiya1"])          #it will throw error