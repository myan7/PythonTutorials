#main.py

import mypackage.module1, mypackage.module2
mypackage.module1.greet("Yan")
mypackage.module2.depart("Yan")
print()

# you can 1
from mypackage import module1, module2
module1.greet("Ming")
module2.depart("Ming")
print()

# you can 2
from mypackage import module1 as m1,module2 as m2
m1.greet("Pythonista")
m2.depart("Pythonista")
print()

# you can 3
from mypackage.module1 import greet
from mypackage.module2 import depart
greet("Pythonista")
depart("Pythonista")



print("Review exercise")
from mypackage.string import shout
from mypackage.mysubpackage.math import area

print()
print(shout("fuck off!"))
print(area(15,20))

_area = area(15,20)
_str = f"the area of a 15-by-20 rectangle is {_area}"
print(f"{shout(_str)}")
