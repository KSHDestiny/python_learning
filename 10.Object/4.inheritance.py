class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f"The {self.color} {self.manufacturer} goes VROOOM!!!")
        else:
            print(f"The {self.color} {self.manufacturer} sputters out of gas...")

    def fill(self):
        if self.gas < 4:
            self.gas = 4
            print("Fill full tank of gas!")
        else:
            print("Already Full!")

class Car(Vehicle):
    def radio(self):
        print("Rockin' Tunes!")

    def window(self):
        print("Ahhh... fresh air!")

class Motorcycle(Vehicle):
    def helmet(self):
        print("Helmet on - nice and safe!")

my_car = Car("red", 'Mercedes')
my_car.radio()
my_car.window()
my_car.drive()
print(my_car.gas)

my_mc = Motorcycle("silver", "Harley")
my_mc.helmet()
my_mc.drive()

# overriding parent method
class ElectricCar(Car):
    def drive(self):
        print(f"The {self.color} {self.manufacturer} goes ssshhh...")

my_ecar = ElectricCar("white", "Nissan")
my_car.window()
my_ecar.drive()