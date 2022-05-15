'''
import random
r = random.randint(1, 100)
g = None
ug = 0
while g != r:
    g = int(input("Enter a number: "))
    ug += 1
    if g == r:
        print("U are guess is correct")
    elif g < r:
        print("Please enter a greater number")
    elif g > r:
        print("Please enter a lower number")
print(f"{ug}")
'''



