#string question
#a=input("enter your name")
#print("Good Afternoon "+a)


#making template
letter='''Dear <|NAME|>
Greetings from microsoft, We are happy to tell you about your selection
You are selected!

Date: <|DATE|>
'''
name=input("enter your name")
date=input("enter date")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date)
print(letter)