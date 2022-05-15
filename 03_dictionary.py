a = {
    "Fast": "In a quick manner",
    "jack": "Is a writer",
    "a1": {
        "marks": [1, 2, 3],
        "jack": 3
    }
}
# print(a['jack'])     # prints the dictionary items
# print(a['a1']['marks'])     # prints value of a dictionary in a dictionary ;
# ex:- 'a' is a dictionary and 'a1' is another dictionary inside 'a'

# a['a1']['marks'] = [4, 5, 6]    # changes the values in dictionary

# Dictionary Methods

# print(a.keys())             # prints the keys of the dictionary
# print(a.values())           # prints the values in the dictionary
# print(list(a.keys()))       # prints the keys of the dictionary as a list
# print(list(a.values()))     # prints the values of the dictionary as a list
# print(a.items())            # prints the (key, values) for all contents of the dictionary

# b = {
#    1: 2                   # update the dictionary by adding key-values pairs from "b"
# }
# a.update(b)
# print(a)

# get() method ; difference in .get and [] syntax in Dictionary
print(a.get("Fast2"))     # Returns None as "Fast2" key is not present in the dictionary
print(a["Fast2"])         # throws an error as "Fast2" key is not present in the dictionary


