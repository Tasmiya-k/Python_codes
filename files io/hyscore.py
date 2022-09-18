def game():
    return 789

score=game()
with open("highscore.txt") as f:
    hiscorestr=f.read()

if hiscorestr=='':
    with open("highscore.txt","w") as f:
        f.write(str(score))


elif int(hiscorestr)<score :
    with open("highscore.txt","w") as f:
        f.write(str(score))

