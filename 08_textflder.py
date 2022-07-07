def gw():
    return 122


score = gw()
with open("gamescore.txt", "r") as f:
    hg = f.read()
if hg < score:
    with open("gamescore.txt", "w") as f:
        f.write(str(score))
