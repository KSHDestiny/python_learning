cheese = "cheddar"

def mix_and_cook():
    print("Mixing the ingredients")
    print("Greasing the frying pan")
    print("Pouring the mixture into a frying pan")
    print("Cooking the first side")
    print("Flipping it!")
    print("Cooking the other side")

def make_omelette(name, ingredient):
    mix_and_cook()
    return f"{name} is having a {ingredient} omelette \n"

def make_pancake(name):
    mix_and_cook()
    return f"{name} is having a {cheese} pancake \n"

def make_fancy_omelette(name, *ingredients):        # Asterisk(*) is used to accept all arguments as parameter
    mix_and_cook()
    return f"{name} is having a fancy omelette with {len(ingredients)} ingredients \n"

print(make_omelette("Destiny", "bacon"))
print(make_pancake("Oak"))
print(make_fancy_omelette("Clear", "sausage", "onion", "pepper", "spinach", "mushroom", "tomato", "goat cheese"))