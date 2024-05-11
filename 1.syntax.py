print("Python is fun to learn!")

name = "Destiny"
age = 24
school = input("What is your high school name?")

def myself():
    print("My name is", name, "and I am", age, "years old.")
    if(age > 18):
        print("I am an adult.")
    else:
        print("I am a kid.")
    print("I have studied in", school)

myself()