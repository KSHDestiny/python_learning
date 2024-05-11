def mix_and_cook():
    print("Mixing the ingredients")
    print("Greasing the frying pan")
    print("Pouring the mixture into a frying pan")
    print("Cooking the first side")
    print("Flipping it!")
    print("Cooking the other side")

def make_omelette(ingredient):
    mix_and_cook()
    return f"Destiny is having a {ingredient} omelette \n"

def make_pancake():
    mix_and_cook()
    return "Oak is having a delicious pancake \n"

def make_fancy_omelette(*ingredients):
    mix_and_cook()
    return f"Clare is having a fancy omelette with {len(ingredients)} ingredients \n"

print(make_omelette("bacon"))
print(make_pancake())
print(make_fancy_omelette("sausage", "onion", "pepper", "spinach", "mushroom", "tomato", "goat cheese"))