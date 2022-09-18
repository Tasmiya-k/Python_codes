students=["ram", "shyam","kishan", "AYAN", "radhika"]  #list

for student in students:
    if student == "AYAN":
        break;
    print(student)

for student in students:
    if student=="kishan":
        continue;
    print(student)

marks={"english": 95, "chemistry": 98, "physics" : 97}

print(marks["chemistry"])
marks["physics"]=97;
print(marks)

marks["physics"]=100;
print(marks)
