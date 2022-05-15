# List and tuple examples :-
"""
a1 = input("Enter Fruit number 1 ")
a2 = input("Enter Fruit number 2 ")
a3 = input("Enter Fruit number 3 ")
a4 = input("Enter Fruit number 4 ")
a5 = input("Enter Fruit number 5 ")
a6 = input("Enter Fruit number 6 ")
a7 = input("Enter Fruit number 7 ")
a = [a1, a2, a3, a4, a5, a6, a7]
print(a) """
from this import s

"""m1 = int(input("Enter marks of a student 1: "))
m2 = int(input("Enter marks of a student 2: "))
m3 = int(input("Enter marks of a student 3: "))
m4 = int(input("Enter marks of a student 4: "))
m5 = int(input("Enter marks of a student 5: "))
m6 = int(input("Enter marks of a student 6: "))

m = [m1, m2, m3, m4, m5, m6]
m.sort()
print(m)"""
"""a = [1, 2, 3]
print(a[0] + a[1] + a[2])
print(sum(a))"""
"""a = (7, 0, 8, 0, 0, 9)
print(a.count(0))"""
# Dictionary example
'''
d = {
    "pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are: ", d.keys())
a = input("Enter the Hindi word\n ")
print("The meaning of this word is: ", d.get(a))
'''
# Set Example:-
'''a1 = input("Enter number 1\n ")
a2 = input("Enter number 2\n ")
a3 = input("Enter number 3\n ")
a4 = input("Enter number 4\n ")
a5 = input("Enter number 5\n ")
a6 = input("Enter number 6\n ")
a7 = input("Enter number 7\n ")
a8 = input("Enter number 8\n ")
a = {a1, a2, a3, a4, a5, a6, a7, a8}
print(a)'''
"""
dc = {}
dc[input()] = input("Enter number 1\n ")
dc[input()] = input("Enter number 2\n ")
dc[input()] = input("Enter number 3\n ")
dc[input()] = input("Enter number 4\n ")
print(dc)
"""
'''
n1 = int(input("enter number1: "))
n2 = int(input("enter number2: "))
n3 = int(input("enter number3: "))
n4 = int(input("enter number4: "))
if n1 > n4:
    f1 = n1
else:
    f1 = n4
if n2 > n3:
    f2 = n2
else:
    f2 = n3
if f1 > f2:
    print(str(f1) + " is greatest ")
else:
    print(str(f2) + " is greatest ")
'''
'''
n1 = int(input("enter sub1: "))
n2 = int(input("enter sub2: "))
n3 = int(input("enter sub3: "))

if n1 < 33 or n2 < 33 or n3 < 33:
    print("your are not passed")
elif (n1+n2+n3)/3 < 40:
    print("you not passed the test")
else:
    print("you passed the test")
'''
"""
l = ["hulk", "thor", "iron man", "marvel"]
a = input("enter a name: ")
if a.lower() in l:
    print("you are an avenger")
else:
    print("your are not an avenger")
"""
'''
n = int(input("Enter a number: "))
for i in range(1, 11):
    #  print(str(n) + " X " + str(i) + " = " + str(n*i))
    print(f"{n} x {i}= {n * i}")
'''
'''
n = int(input("Enter a number: "))
p = True
for i in range(2, n):
    if n % i == 0:
        p = False
        break
if p:
    print("Entered number is a prime")
else:
    print("the given number is not a prime")
'''
'''
n = int(input("Enter a number: "))
f = 1
for i in range(1, n+1):
    f = f * i
print(f"{n} = {f}")
'''

# function example:-
"""
def mx(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    else:
        if n2 > n3:
            return n2
        else:
            return n3


m1 = int(input("enter ur number: "))
m2 = int(input("enter ur number: "))
m3 = int(input("enter ur number: "))
print(mx(m1, m2, m3))
"""


def p(num):
    if num < 0:
        return "Enter a positive number"
    return num + p(num-1)


num = int(input("Enter a number: "))
print("The sum is", num)
