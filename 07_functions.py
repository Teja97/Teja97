# The part containing the exact set of instructions which are executed during the function call
# -> it is of 2 types
# -> 1. built-in function         ; example:- print(),  len(),  range() .... etc
# -> 2. user defined function     ; exp :- below program

'''
def great(name):
    print("good morning, " + name)


def ms(n1, n2):
    return n1 + n2


great("harry")
s = ms(1, 2)
print(s)
'''

# Default argument :-
'''
def greet(name="Stranger"):
    print("Good day, " + name)


greet()
greet("Hulk")
'''


# recursive:-
# recursion is a function which calls itself
# it directly uses a mathematical formula as a function
def recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * recursive(n - 1)


r = int(input("Enter a number: "))
print(recursive(r))

# prevent a new line at the end using print() function :-
'''
print("I", end=" ")
print("am", end=" ")
print("Thor", end=" ")
'''
