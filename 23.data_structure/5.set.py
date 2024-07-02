primary_colors = set(["red", "blue", "yellow"])
color = "green"
if color in primary_colors:
    print(color + " is a primary color")
else:
    print(color + " is not a primary color")
#_________________________________________________________________

letters = set(['a', 'b'])
letters.add('c')
print(letters)  # {'b','a','c'}
#_________________________________________________________________

set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

union_set = set_A.union(set_B)
print(union_set)    # {70, 40, 10, 50, 20, 60, 30}

intersection_set = set_A.intersection(set_B)
print(intersection_set) # {40, 50, 30}

difference_set = set_A.difference(set_B)
print(difference_set)   # {10, 20}

difference_set_BA = set_B.difference(set_A)
print(difference_set_BA)    # {60, 70}

symmetric_difference_set = set_A.symmetric_difference(set_B)
print(symmetric_difference_set) # {20, 70, 10, 60}
#_________________________________________________________________

primary_colors = frozenset(["red", "blue", "yellow"])
if "blue" in primary_colors:
    print("Blue in the set!")

primary_colors.add("green") # got error since forzenset can't change initial value
#_________________________________________________________________
# liner time complexity
def has_unique_characters(data):
    unique_data = set(data)
    return len(data) == len(unique_data)

print(has_unique_characters("sample"))
print(has_unique_characters("hello world"))
print(has_unique_characters("linkedin"))
print(has_unique_characters("python"))