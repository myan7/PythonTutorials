"""
The actual requirements are open to interpretation, but try to adhere
to these guidelines:

1. You should have at least four classes: the parent Animal class, and
then at least three child animal classes that inherit from Animal.

2. Each class should have a few attributes and at least one method
that models some behavior appropriate for a specific animal or all
animals—such as walking, running, eating, sleeping, and so on.

3. Keep it simple. Utilize inheritance. Make sure you output details
about the animals and their behaviors.
"""


## instead of animal, I would like to solve a real life problem:
## what house you want to buy.


class Property:
    def __init__(self,address,city,state,zipCode):
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def __str__(self):
        return f"""{self.address} is in {city}, {state} {zipCode}"""


class Apartment(Property):
    def __init__(self,address, city, state, zipCode, yearofBuild, unitNO = 507):
        self.address = address
        self.unitNO = unitNO
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.yearofBuild = yearofBuild

    def __str__(self):
        return f"""{self.address} {unitNO} is in {city}, {state} {zipCode}
and it is built in {self.yearofBuild}"""

class TownHouse(Property):
    def __init__(self,address, city, state,zipCode,yearofBuild, stories = 2):
        self.address = address
        self.stories = stories
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.yearofBuild = yearofBuild
    
    def __str__(self):
        return f"""{self.address} is a townhouse in {city}, {state} {zipCode}
and it is a {stories} stories townhouse."""

class SingleHouse(Property):
    def __init__(self,address, city, state,zipCode,yearofBuild, stories = 2, lotSize = 1000):
        self.address = address
        self.stories = stories
        self.lotSize = lotSize
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.yearofBuild = yearofBuild
    
    def __str__(self):
        return f"""{self.address} is a single house in {city}, {state} {zipCode}
and it is a {stories} stories single house with {lotSize} square feet lot."""

address = "200 N Jefferson"
unitNO = "507"
city = "Chicago"
state = "IL"
zipCode = "60661"
yearofBuild = "2006"

unit507 = Apartment(address, city,state,zipCode, yearofBuild, unitNO)
print(unit507)

address = "3517 S Dearborn st"
city = "Chicago"
state = "IL"
zipCode = "60609"
yearofBuild = "2008"
stories = 4

tHouse3517 = TownHouse(address, city, state,zipCode,yearofBuild, stories)
print(tHouse3517)
