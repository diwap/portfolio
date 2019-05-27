from random import choice
from collections import Counter

a = 12
list1 = ['apple','ball','cat','dog','egg']
list2 = [
    'Apple is fruit',
    'Ball is toy',
    'Cat is an animal',
    'Dog is an animal',
    'Egg is laid by female bird'
]
list3 = ['fish','gun','hen']
list4 = ["d", "a", "t", "a", "c", "a", "m", "p","t","a"]

# Check whether the given value is string
def check_if_string(a):
    return isinstance(a, str)

# Select 2nd element from given list
def get_element(list):
    return list[1]

# get last element from list whatever the length
def get_last_element(list):
    return list[-1]

# get random element from list
def return_random(list):
    return choice(list)


# Join list of string to a string
# Output: appleballcatdogegg
def join_string(list):
    return ', '.join(list)

# Convert list to dictionaries
def convert_list_to_dict(list1, list2):
    return dict(zip(list1, list2))

# print(convert_list_to_dict(list1, list2))

# Get size or length of list
def get_length(list):
    return len(list)

# Append any list in list1
def list_appender(list):
    a = ['fish','gun']
    return list.append(a)


# Extend any list in list1
def list_extender(list):
    a = ['fish','gun']
    return list.extend(a)

# Concatenate two list
def concat_list(list1, list2):
    return list1 + list2

# Create list of 10 numbers using range()
def return_list():
    list = []
    for x in range(11):
        list.append(x)
    return list


def return_list_1():
    return [x for x in range(11)]

# Count occurance of an item in a list
def count_item(list, item):
    return list.count(item)

# Count occurance of all item in a list
def count_all_item(list):
    return Counter(list)

counted_list = count_all_item(list4)
# print(counted_list.get("a"))

# Get index of item in a list
def enumerate_list(list):
    dict = {}
    for i, val in enumerate(list):
        dict[i] = val
    return dict


# Remove duplicates from list
def duplicate_remover(list1):
    return sorted(list(set(list1)))

print(duplicate_remover(list4))
