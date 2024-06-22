items1 = dict({"key1" : 1, "key2" : 2, "key3" : 3})
print(items1)    # {'key1': 1, 'key2': 2, 'key3': 3}

items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)   # {'key1': 1, 'key2': 2, 'key3': 3}

# ToDo: replace an item
items2["key2"] = "two"
print(items2)   # {'key1': 1, 'key2': 'two', 'key3': 3}

# ToDo: try to access a nonexistent key
#print(items1["key6"])   # KeyError: 'key6'

# ToDo: iterate the keys and values in the dictionary
for key, value in items2.items():
    print("Key:",key," value:",value)