import urllib.request

#! try except else
try:
    webpage = urllib.request.urlopen("http://www.google.com")
except: # if fail
    print("Could not access webpage!")
else:   # if success
    for line in webpage:
        print(line)

#! raise Exception("Error Message")
class CircuitBreaker:
    def __init__(self, max_amps):
        self.capacity = max_amps
        self.load = 0

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception("Connection will exceed capacity.")
        elif self.load + amps < 0:
            raise Exception("Connection will cause a negative load.")
        else:
            self.load += amps

cb = CircuitBreaker(20)
print(cb.capacity >= cb.load)

cb.connect(12)
cb.connect(7)
cb.connect(1)
print(cb.capacity >= cb.load)

#! Custom Exception Error
class ElectricalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f"The {self.device} is {self.problem}!"

class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f"The {self.device} is {self.problem}!"

def cause_error(error_type):
    if error_type == "electrical":
        raise ElectricalError("circuit breaker", "overloaded")
    elif error_type == "plumbing":
        raise PlumbingError("dishwasher", "spraying water")
    else:
        raise Exception("a generic household problem")
    
try:
    # cause_error('electrical')
    # cause_error('plumbing')
    cause_error('yard')
except ElectricalError as e:
    print(e)
    print('Barron fix it')
except PlumbingError as e:
    print(e)
    print('Call the plumber')
except:
    print('Call the landlord')