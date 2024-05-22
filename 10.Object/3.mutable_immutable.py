# list objects are mutable
closet = ['shirt', 'hat', 'pants', 'jacket', 'socks']
print(closet)
print(id(closet))
closet.remove('hat')
print(closet)
print(id(closet))

# string objects are immutable
words = "You're wearing that "
print(words)
print(id(words))
words = words + "because you look great!"
print(words)
print(id(words))
# note - the plus operator creates a new string containing the concatenated phrase and binds the new object to the name words

text = "Hello"
greeting = text
print(text is greeting)

text = text + " Mello"
print(text is greeting)
print(text)
print(greeting)
