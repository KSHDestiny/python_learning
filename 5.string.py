# string concat -> +
name = input('Enter your name: ')
print("Good morning, " + name)

# string multiply -> *
greeting = "Hello "
print(greeting * 5)

value_str = input('Enter a number: ')   # string output
print(value_str * 10)
value_int = int(value_str)  # str to int method
print(value_int * 10)

miles = input('Enter a distance in miles: ')
miles_float = float(miles)  # str to float
kilometers = miles_float * 1.609344
print('That value in kilometers is', kilometers)

#! string methods
# capitalize()
name = 'malala'
name_cap = name.capitalize()
print(name_cap)

# find(), [start:end]
note = 'award: Nobel Peace Prize'
award_location = note.find('award: ')
print(award_location)
award_text = note[7:]
print(award_text)