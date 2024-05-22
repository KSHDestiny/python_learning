class Shirt:
    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean - True

red = Shirt()
crimson = red
print(id(red))
print(id(crimson))
print(red is crimson)   # True

red.make_dirty()
print(red.clean)
print(crimson.clean)

crimson = Shirt()
print(id(red))
print(id(crimson))
print(red.clean)
print(crimson.clean)
print(red is crimson)   # False