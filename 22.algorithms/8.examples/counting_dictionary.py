items = ["apple", "pear", "orange", "banana", "apple", "orange", "apple", "pear", "banana", "orange", "apple", "kiwi", "pear", "apple", "orange"]

# ToDo: create a hashtable object to hold the items and counts
counter = dict()

# ToDo: iterate over each item and increment the count for each one
for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)  # {'apple': 5, 'pear': 3, 'orange': 4, 'banana': 2, 'kiwi': 1}