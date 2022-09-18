with open("readfil.txt") as f:
    content=f.read()

content=content.replace("donkey","*******")

with open("readfil.txt","w") as f:
    content=f.write(content)