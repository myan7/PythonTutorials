

_section_str = "================================================================================"
_segment_str = "--------------------------------------------------------------------------------"


print(" Chapter 10 Object-Oriented Programming (OOP) ")

print(f"""{_section_str} \n 10.1 Define a Class.

to define the properties, you need to define or we should call it overwrite a function
__init__(self,propertyA, propertyB,...,propertyZ)
This method will be run every time a new instance of that Object is created
and initialize the values.
the self should always be the first positional argument, which is a place holder
that is used to build the blue print.
""")

class Dog:
    # class attribute:
    species = 'Canis Failiaris'
    
    # similar to constructor in Java
    def __init__():
        self.name = 'Midnight'
        self.gender = 'Male'
        self.age = 3
    
    def __init__(self, name, gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    # Instance method
    """
    refer to https://docs.python.org/3/tutorial/classes.html#private-variables
    Any identifier of the form __spam
    (at least two leading underscores, at most one trailing underscore)
    is textually replaced with _classname__spam,
    where classname is the current class name with leading underscore(s) stripped.
    This mangling is done without regard to the syntactic position of the identifier,
    as long as it occurs within the definition of a class.
    """
    def _sleep(self):
        print(f"{self.name} is sleeping.")

    def _bark(self):
        print(f"{self.name} is barking to the tree.")

    def _play(self):
        pronoun = 'his' if self.gender == 'Male' else 'her'
        print(f"{self.name} is playing with {pronoun} toys.")

    def _toStr(self):
        pronoun = 'he' if self.gender == 'Male' else 'she'
        print( f"{self.name} is {self.age} years old, and {pronoun} is a {Dog.species}")

print(f"""{_section_str}
10.2 Instantiate an object.
""")    
jason = Dog("Jason",'Female',15)
bourne = Dog('Bourne','Male',5)

jason._sleep()
jason._play()
bourne._bark()
jason._toStr()
bourne._toStr()

print(f"{_segment_str} \n How to create a tuple ")
