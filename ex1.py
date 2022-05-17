import random


def gm1(comp, y):
    if comp == y:
        return None
    if comp == "r":
        if y == "s":
            return False
        elif y == "p":
            return True
    if comp == "s":
        if y == "p":
            return False
        elif y == "r":
            return True
    if comp == "p":
        if y == "r":
            return False
        elif y == "s":
            return True


print("Computer choose rock(r), paper(p), scissors(s):")
n = random.randint(1, 3)
if n == 1:
    comp = "r"
elif n == 2:
    comp = "p"
elif n == 3:
    comp = "s"
y = input("Enter any option r, p, s : ")
a = gm1(comp, y)
print(f"computer choose {comp} and player choose {y}")
if a is None:
    print("The game is tie")
elif a:
    print("u win the game")
else:
    print("u loss the game")


