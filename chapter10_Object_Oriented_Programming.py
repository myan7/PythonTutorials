

from Common import _section_str,_segment_str,myPrint

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
## refer to https://realpython.com/operator-function-overloading/
## for overloading
# for default constructor, you can give the default values in the argument
# unlike Java, you cannot have 2 __init__ methods in a class,
# the later one will always over load the previous one.
#    def __init__():
#        self.name = 'Midnight'
#        self.gender = 'Male'
#        self.age = 3
    
    def __init__(self, name="Midnight", gender="Male",age=3):
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

    def _speak(self, language):
        return f"{self.name} speaks {language}"

    def _toStr(self):
        pronoun = 'he' if self.gender == 'Male' else 'she'
        print( f"{self.name} is {self.age} years old, and {pronoun} is a {Dog.species}")

    ## this is the same as toString() in Java, when print out an instance of this class,
    ## this function will be called.
    ## and it is supposed to return a string instead of outputing in the consolse.dir
    ## if you don't overwrite this function, when print out the instand of this object,
    ## you will get a memory address.
    def __str__(self):
        pronoun = 'he' if self.gender == 'Male' else 'she'
        return f"{self.name} is {self.age} years old, and {pronoun} is a {Dog.species}"
    

print(f"""{_section_str}
10.2 Instantiate an object.
""")    

## to construct an object with default value,
## Python doesn't behave like Java, which can have a default constructor,
## instead, you need to put some default values in the argument list
midNight = Dog()
myPrint(midNight)


jason = Dog("Jason",'Female',15)
myPrint(jason)

print(f"""    Wth out overwrite __str__, when you print out an object, you will get
    type of jason is <class '__main__.Dog'>.
    jason is <__main__.Dog object at 0x000002466C989AF0>.
    """)

bourne = Dog('Bourne','Male',5)

jason._sleep()
jason._play()
bourne._bark()
jason._toStr()
bourne._toStr()

print(f"""{_segment_str}
Class and Instance Attributes
Notice: The default behavior of the == operator can be overridden.
How this is done is outside the scope of this book
you can refer to https://realpython.com/operator-function-overloading/
""")

print(f"""{_segment_str}
Review Exercises 
""")

# 1
class Cat:
    def __init__(self, name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name}'s coat is {self.coat_color}"

philo = Cat("Philo", 3, "brown")
print('# 1')
print(philo)


# 2
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

blue = Car("blue",20_000)
red = Car("red",30_000)
print('# 2')
print(blue)
print(red)

# 3 redefine the Car class by adding a drive method
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def _drive(self, trip):
        self.mileage += trip
        
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

myCar = Car("silver",64030)
print(myCar)
myCar._drive(50)
print(f"after drive 50 miles, {myCar}")




print(f"""{_section_str}
10.3 Inherit From Other Classes.
""")
print(f"similar to Java, blah blah blah.")

print(f"""{_segment_str}
The object Class
""")
print("""
The most basic type of class is an object, which generally all other
classes inherit from as their parent.
class Dog(object):
pass

In Python 3, this is the same as:
class Dog:
pass

The inheritance from object is stated explicitly in the first definition by
putting object in between parentheses after the Dog class name. This
is the same pattern used to create child classes from your own custom
classes.
""")

print(f"""{_segment_str}
Dog Park Example
Parent Classes vs Child Classes
""")

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

matt = JackRussellTerrier("Matt", "Female" ,4)
damon = Dachshund("Damon", "Male",10)

print(matt)
myPrint(matt)
print(damon)
myPrint(damon)

print(f"""{_segment_str}
Dog Park Example
Extending the Functionality of a Parent Class
super()
Note:
overriding functions from the parent class
be careful in real world when calling super()
a class can have multiple parents, multi inheritance.
""")

class JackRussellTerrier(Dog):
    breed = "JackRussellTerrier"
    ## to inherite a method from a parent, you have to use super(). to call the function in
    ## the parent class.
    def _speak(self, language = "English"):
        return super()._speak(language)

    ## simply override, super()._bark print out instead of return.
    def _bark(self, sound = "Arf"):
        return (f"{self.name} says {sound}.")

    ## override 
    def __str__(self):
        pronoun = 'he' if self.gender == 'Male' else 'she'
        return f"{self.name} is {self.age} years old, and {pronoun} is a {JackRussellTerrier.breed}"

class Dachshund(Dog):
    breed = "Dachshund"
    def _speak(self, language = "Dutch"):
        return super()._speak(language)
    def __str__(self):
        pronoun = 'he' if self.gender == 'Male' else 'she'
        return f"{self.name} is {self.age} years old, and {pronoun} is a {Dachshund.breed}"

class Bulldog(Dog):
    breed = "Bulldog"
    def _speak(self, language = "Doggish"):
        return super()._speak(language)
    def __str__(self):
        pronoun = 'he' if self.gender == 'Male' else 'she'
        return f"{self.name} is {self.age} years old, and {pronoun} is a {Bulldog.breed}"
    def _play(self, toy="ball"):
        pronoun = 'his' if self.gender == 'Male' else 'her'
        print(f"{self.name} is playing with {pronoun} {toy}.")

matt = JackRussellTerrier("Matt", "Female" ,4)
damon = Dachshund("Damon", "Male",10)

print(matt)
myPrint(matt)
print(damon)
myPrint(damon)
matt._play()


jason._bark()
print(matt._bark())
ugly = Bulldog("Ugly","Male",2)
ugly._play()
ugly._play("Sponge Bob")

print(jason._speak("shit"))
print(matt._speak())
print(ugly._speak())


print(f"""{_segment_str}
Review Exercises
""")

# 1
print("# 1")

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    breed = "GoldenRetriever"
    def speak(self, sound = "Bark"):
        return super().speak(sound)

erMao = GoldenRetriever("ErMao",3)

print(erMao.speak())

# 2
print("# 2")

class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Square(Rectangle):
    def __init__(self,side_length):
        return super().__init__(side_length,side_length)

    def area(self):
        return super().area()

rec = Rectangle(3,4)
print(rec.area())

sqa = Square(4)
print(sqa.area())


