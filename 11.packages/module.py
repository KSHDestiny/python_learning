# https://docs.python.org/3/py-modindex.html    // all package modules url

import random   #* import entire package module
from random import randint   #* import specific method of the package
from random import random as rand   #* solve random same name conflict

print(random.randint(1,20))
print(randint(1,20))
print(rand())