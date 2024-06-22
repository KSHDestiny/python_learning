items = ["apple", "pear", "orange", "banana", "apple", "orange", "apple", "pear", "banana", "orange", "apple", "kiwi", "pear", "apple", "orange"]

# ToDo: create a set to perform a filter
unique_items = set()

# ToDo: loop over each item and add to the set
for item in items:
    unique_items.add(item)
print(unique_items) # {'orange', 'banana', 'kiwi', 'pear', 'apple'}

# ToDo: Count the unique letters in a sentence
sentence = "The quick brown dox jumps over the lazy dog."
unique_items = {c for c in sentence.lower() if c.isalnum()} # lower() is used to remove counting both "t" and "T" as diff letter
print(unique_items) # {'h', 'b', 'j', 'q', 'w', 't', 'c', 'p', 's', 'n', 'u', 'l', 'x', 'm', 'g', 'a', 'r', 'v', 'o', 'e', 'k', 'z', 'y', 'd', 'i'}