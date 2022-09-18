#with open("log.txt") as f:
#    content=f.read()

#if 'python' in content:
#    print("yes python is present")
#content=True

content=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline()
        if 'python' in content:
            print(content)
            print(f"python is present in {i} line")
        i+=1







