class Sample:
    a="tas"

    @staticmethod
    def greet():
        print("hello sir")


obj=Sample()
obj.a="neha"                 #it doesnt change the class attribute
#Sample.a="neha"              #we can change class attribute like this

print(Sample.a)
print(obj.a)
obj.greet()