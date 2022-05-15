# Creation of a set
a = {1, 2, 3, 1, 5}    # set is a collection of a non-repetitive elements
# print(a)

# Creation of an empty set

# b = {}                # It shows as empty dictionary
b = set()               # It is an empty set
print(type(b))

# Set Methods
'''1 .add()    2 len()    3 .remove()    4  .pop()    5  .clear()  6  .union()  7 .intersection() '''
b.add(5)               # .add() is used to add elements in a set
b.add(6)
# b.add(5)               # If u add the same element two times it will take only one time in a set
# b.add([2, 3, 8])     # we cannot add 'list' in a set ; TypeError: unhashable type: 'list'
# b.add({1: 2, 3: 4})   # we cannot add 'dictionary' in a set ; TypeError: unhashable type: 'dict'
# b.add((3, 4, 5))       # we can add 'tuple' in a set
# print(len(b))         # prints the length of this set
# b.remove(5)           # removes elements from set ex:- 5 from set b
# b.remove(15)          # throws an error because '15' is not present in set 'b'
# print(b.pop())        # removes an arbitrary element from set
# print(b.union({4, 9, 5}))   # returns a new set with all the items from both the set
# print(b.intersection({6, 8}))  # returns a set which contains only the items in both set


