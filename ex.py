import random


def gw(comp, u):
    if comp == u:
        return None
    if comp == "s":
        if u == "w":
            return False
        elif u == "g":
            return True
    if comp == "w":
        if u == "g":
            return False
        elif u == "s":
            return True
    if comp == "g":
        if u == "s":
            return False
        elif u == "w":
            return True


for i in range(10):
    print("comp Turn snake(s), water(w), gun(g)")
    r = random.randint(1, 3)
    if r == 1:
        comp = "s"
    elif r == 2:
        comp = "w"
    elif r == 3:
        comp = "g"

    u = input("Choose any one of this option s,w,g : ")
    a = gw(comp, u)
    print(f"computer chose {comp} and your chose {u}")
    if a is None:
        print("The game is tie")
    elif a:
        print("you win!")
    else:
        print("you loss!")

