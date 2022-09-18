comment=input("enter the comment ")

if("make a lot of money" in comment):
    Scam=True
elif("buy now" in comment):
    Scam=True
elif("Subscribe this" in comment):
    Scam=True
elif("click this" in comment):
    Scam=True
else:
    Scam=False


if(Scam):
    print("This comment is spam")
else:
    print("This comment is not spam")
