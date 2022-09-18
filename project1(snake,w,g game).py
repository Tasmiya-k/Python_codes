
import random

def game(comp, you):
    if comp==you:
        return None

    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True




print("Comp Turn: Snake(1) Water(2) Gun(3)?")
randNO=random.randint(1,3)
if randNO==1:
    comp='s'
elif randNO==2:
    comp='w'
elif randNO==3:
    comp='g'

you=input("Your's Turn: Snake(s) Water(g) Gun(w)?")

a=game(comp, you)
print("comp is", comp)
print("you are", you)
if(comp=='s' and you=='g'):
    print("Aap ne snake ko gun se uda diya")
elif(comp=='s' and you=='w'):
    print("snake ne aap ko pi liya")
elif(comp=='g' and you=='s'):
    print(" gun ne aap ko uda diya")
elif(comp=='g' and you=='w'):
    print("gun aap me dub gayi")
elif(comp=='w' and you=='g'):
    print("Aap pani me dub gaye")
elif(comp=='w' and you=='s'):
    print("Aap ne pani pi liya")

if a==None:
    print("game tie hogayi!")
elif a:
    print("Aap jeet gaye")
else:
    print("Aap haar gaye")

