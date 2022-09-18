class Employee:
    company="Google"
    salary=10

harry=Employee()
rajni=Employee()

#creating instance attribute salary for both attribute
harry.salary=400
rajni.salary=300

print(harry.salary)
print(rajni.salary)

#Below will show error as address is not present in class/instance
#print(rajni.address)

