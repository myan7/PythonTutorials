import inspect
import collections
import time
from timeit import default_timer as timer

# use signature()
# print(inspect.signature(collections.Counter))
_section_str = "================================================================================"
_segment_str = "--------------------------------------------------------------------------------"

print(" Chapter 9 Tuples, Lists, and Dictionaries ")

print(f"{_section_str} \n 9.1 Tuples Are Immutable Sequences ")

print(f"{_segment_str} \n How to create a tuple ")
print(f"{_segment_str} \n 1. tuple literals ")

def __print_tuple(t):
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') +1:-1].split(',')
    names = []
    for i in args:
        if i.find('=') != -1:
            names.append(i.split('=')[1].strip())
        else:
            names.append(i)
    print(f"type of {names[0]} is {type(t)}")
    print(f"{names[0]} is {t}")
    print()


def myPrint(t):
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') +1:-1].split(',')
    names = []
    for i in args:
        if i.find('=') != -1:
            names.append(i.split('=')[1].strip())
        else:
            names.append(i)
    print(f"type of {names[0]} is {type(t)}.")
    print(f"length of {names[0]} is {len(t)}.")
    print(f"{names[0]} is {t}.")
    print()

print(f"{_segment_str} \n to create an empty tuple ")
_tuple_0 = ()
print(f"type of _tuple_0 is {type(_tuple_0)}")
print(f"_fuple_0 is {_tuple_0}")
print(f"{_segment_str} \n")


_tuple_1 = ('a','b','c')
__print_tuple(_tuple_1)

_tuple_2 = (1)
__print_tuple(_tuple_2)
_tuple_3 = (1,)
__print_tuple(_tuple_3)


print(f"{_segment_str} \n 2. the tuple() built-in ")
_tuple_4 = tuple(_tuple_1)
__print_tuple(_tuple_4)

_tuple_5 = tuple(range(3))
__print_tuple(_tuple_5)

print("single value tuple?, you have to append a comma after that single value")

_tuple_6 = tuple("Python")
__print_tuple(_tuple_6)


try:
    _tuple_7 = tuple(1,2,3,4)
    _tuple_8 = tuple(1)
except:
    print("TypeError: tuple expected at most 1 ITERABLE argument")

_tuple_7 = tuple()
__print_tuple(_tuple_7)

_tuple_8 = tuple(range(10))
__print_tuple(_tuple_8)

_tuple_9 = _tuple_8[2:5]
__print_tuple(_tuple_9)

print(f"{_segment_str} \n Tuples are Immutable and iterable")

for e in _tuple_8:
    if e%2 == 0:
        print(e)
    if e%2 != 0:
        try:
            e = 99
        except:
            print("Tuples are immutable")
        finally:
            print(" ")

for i in range(len(_tuple_8)):
    if _tuple_8[i] % 3 != 0:
        try:
            _tuple_8[i] = 3*i
            print(_tuple_8[i])
        except TypeError:
            print("'tuple' object does not support item assignment")
    else:
        print(_tuple_8[i])


print(f"{_segment_str} \n Tuple Packing and Unpacking ")
print("""
There is a third, although less common, way of creating a tuple.
You can type out a comma-separated list of values and leave off the parentheses:
this is called pack
""")

coordinates = 4.21,9.29
__print_tuple(coordinates)

print(f"coordinates[0] is {coordinates[0]}, and coordinates[1] is {coordinates[1]}")

print("""
you can also unpack a tuple by assing the values to different variables:
x,y = coordinates
""")
x,y = coordinates
print(f"x is {x}")
print(f'y is {y}')

print("""
This leads to a new way of assigning variables
a,b,c = x,y,z
for example:
""")

fName, lName, address, occupation = 'Ming', 'Yan', "200 N Jefferson st APT 507 Chicago IL", "Sr Analyst"
print(f'First name is {fName}, \nLast name is {lName}, \naddress is {address}, \nand occupation is {occupation}')

print("""
what really happened here is
on the right hand side of assignment,the 4 values were packed into a tuple.
then the values of the tuple were unpacked into 4 individual variables.
That being side, the number of values and variables, should be the same.
if they are not the same, Python will throw out an excpetion of ValueError
either "Not enough values to unpack",
or "Too many values to unpack".
You can test it out yourself.
""")

_friends = tuple(["Yue","Jiacheng","Shaobo","Gen","Eric","Gavin"])
__print_tuple(_friends)

print(f"check if Christine is in my friend list: {'Jayson' in _friends}")


print(f"{_section_str} \n 9.2 Lists Are Mutable Sequences ")



print(f"{_segment_str} \n I. Create a list using List literal example ")
_furnitures = ["shoe stand","shoe shelf","dining table","sofa","coffee table","desk","bookshelf","office chair","bed","coat rack","nothing else"]

myPrint(_furnitures)

print(f"{_segment_str} \n II. Use list constructor, list()")
_list_0 = list(_tuple_1)
myPrint(_tuple_1)
myPrint(_list_0)

print("""
this makes an interesting point, when we want to update a tuple, which is immutable,
we can convert it to a list and update the list, because list is mutable,
and then convert it back to a tuple.

""")

print("""
Lists implement all of the common and mutable sequence operations.
refer to https://docs.python.org/3/library/stdtypes.html
""")


print("list() takes any iterable objects. run help(list) for help.")
_list_1 = list("Python")
myPrint(_list_1)

_fruits = "cherry, jostaberry, blackberry,blueberry,raspberry,burberry,strawberry,gooseberry"
myPrint(_fruits)

print(f"{_segment_str} \nIII. Use str.split() which returns a list")

_list_fruits_0 = _fruits.split()
myPrint(_list_fruits_0)
print("string.split() will split a string by blank space by default")

## use list comprehension to strip each element from the splitted string
_list_fruits_1 = [x.strip() for x in _fruits.split(",")]
myPrint(_list_fruits_1)

print("""
this will be very useful if you read from a csv file,
you can save the line you read in as a string,
and then conver it to a list or a tuple.
because both of them accept an iterable object as argument.
""")

print(f"{_segment_str} \n List features and common functions ")

print(f"{_segment_str} \n 1. slicing, the same as tuple, string ")
_list_fruits_2 = _list_fruits_1[2:5]
myPrint(_list_fruits_2)

print(f"{_segment_str} \n 2. insert and remove ")
print("list.insert(index,object) will not return a list. it will modify the original list")
_list_fruits_2.insert(len(_list_fruits_2),"joysenberry")
myPrint(_list_fruits_2)

print("list.insert(index, object), index could be negative value, or exceed the len:")
_list_fruits_2.insert(-1,"pinapple")
myPrint(_list_fruits_2)
_list_fruits_2.insert(-len(_list_fruits_2),"apple")
myPrint(_list_fruits_2)
_list_fruits_2.insert(len(_list_fruits_2)+3,"banana")
myPrint(_list_fruits_2)

print("""list.pop(self, index = -1,/) remove and return item at index, default to the last one
will raise IndexError if list is empty or index is out of bound
      """)

_element_popped = _list_fruits_2.pop()
print(_element_popped)
myPrint(_list_fruits_2)

_list_notBerry = []
for i in range(len(_list_fruits_2)):
    if("berry" not in _list_fruits_2[i]):
        _list_notBerry.append(i)

myPrint(_list_notBerry)

_list_fruits_2_cp = _list_fruits_2.copy()

print(f"_list_fruits_2_cp = _list_fruits_2 : {_list_fruits_2_cp == _list_fruits_2}\n")

_index_notBerry = 0
print("""if you want to pop from a list,
you may want to start from the end to the start.
because pop() will mess with the indices.\n
""")
for i in range(-len(_list_fruits_2), 0):
    if "berry" not in _list_fruits_2[i]:
        _list_notBerry[_index_notBerry] = _list_fruits_2.pop(i)
        _index_notBerry += 1

myPrint(_list_notBerry)

myPrint(_list_fruits_2)

myPrint(_list_fruits_2_cp)

try:
    for i in range(len(_list_fruits_2_cp)):
        if "berry" not in _list_fruits_2_cp[i]:
            _list_notBerry[_index_notBerry] = _list_fruits_2_cp.pop(i)
            _index_notBerry += 1
except IndexError:
    print("""You cannot loop from the beginning to the end for pop,
it will mess with indices
_list_fruits_2_cp is copy of _list_fruits_2
look what it becomes now?\n """)
myPrint(_list_fruits_2_cp)

print(f"_list_fruits_2_cp = _list_fruits_2 : {_list_fruits_2_cp == _list_fruits_2}\n")

print("List Comprehensions:")

_tuple_num = (1,2,3,4,5)
myPrint(_tuple_num)

_list_num = [num**2 for num in _tuple_num]
myPrint(_list_num)

print("""
List comprehensions are commonly used to convert values in one list
to a different type.
For instance,
suppose you needed to convert a list of strings containing floating point values
to a list of float objects.
""")

_list_float_str = ['3.5', '10.24',10.11]
myPrint(_list_float_str)
_list_float = [float(element) for element in _list_float_str]
myPrint(_list_float)


print(f"{_section_str}")
print(" 9.3 Nesting, Copying, and Sorting Tuples and Lists ")

print(f"""{_segment_str}
nested list""")
_list_2by2 = [[1,2],['a','b']]

for i in range(len(_list_2by2)):
    for j in range(len(_list_2by2[i])):
        print(f"_list_2by2[{i}][{j}] is {_list_2by2[i][j]}")

## another loop enhanded for loop

for l in _list_2by2:
    for e in l:
        print(e)

print(f"{_segment_str} \n copy a list")

_list_fruits_3 = []
_list_fruits_3 = [_list_fruits_3.append(element) for element in _list_fruits_0]
print(f" _list_fruits_3 == _list_fruits_0 ? {_list_fruits_3 == _list_fruits_0}\n")
myPrint(_list_fruits_3)

print("""Notice you cannot use list comprehension to copy a list
but you can use slice [:]\n""")
_list_fruits_3 = _list_fruits_0[:]
myPrint(_list_fruits_0)
myPrint(_list_fruits_3)
print(f" _list_fruits_3 == _list_fruits_0 ? {_list_fruits_3 == _list_fruits_0}\n")

_list_fruits_3[0] = "???"
myPrint(_list_fruits_0)
myPrint(_list_fruits_3)
print(f" _list_fruits_3 == _list_fruits_0 ? {_list_fruits_3 == _list_fruits_0}\n")


print(f"{_segment_str} \n to prove that using slicing is a shallow copy, let's copy a matrix: \n")

_list_matrix = [[1,2],['a','b','c'],["Ming","Yan"]]
_list_matrix_cp = _list_matrix[:]
myPrint(_list_matrix)
myPrint(_list_matrix_cp)
print(f" _list_matrix == _list_matrix_cp ? {_list_matrix == _list_matrix_cp}\n")

print("now we change the last element in the copied matrix:\n")
_list_matrix_cp[2] = ["Gen","Li"]
myPrint(_list_matrix)
myPrint(_list_matrix_cp)
print(f" _list_matrix == _list_matrix_cp ? {_list_matrix == _list_matrix_cp}\n")
print("""You think everything is as expected, and we have individual matrix right?
now we change one of the element in row 2 col 1 in the copied matrix:\n""")

_list_matrix_cp[1][0] = "Gen"
myPrint(_list_matrix)
myPrint(_list_matrix_cp)
print(f" _list_matrix == _list_matrix_cp ? {_list_matrix == _list_matrix_cp}\n")

print("""You notice not only the copied matrix was updated, the original matrix was
also updated!!!!
this is because when copying a list using slicing, Python only copies the references
to the objects, not creates a copy of the object.
Not only using slicing to copy, .copy() also return a shallow copy!!!

{_segment_str}
To Prove .copy() is also a shallow copy:
""")

list_matrix = [[1,2],['a','b','c'],["Ming","Yan"]]
_list_matrix_cp = _list_matrix.copy()
print(f"""1111111-After shallow copy,
_list_matrix == _list_matrix_cp ?: \t\t\t {_list_matrix == _list_matrix_cp},
id(_list_matrix) == id(_list_matrix_cp) ?: \t\t {id(_list_matrix) == id(_list_matrix_cp)},
id(_list_matrix[0]) == id(_list_matrix_cp[0]) ?: \t {id(_list_matrix[0]) == id(_list_matrix_cp[0])},
id(_list_matrix[0][0]) == id(_list_matrix_cp[0][0]) ?: \t {id(_list_matrix[0][0]) == id(_list_matrix_cp[0][0])}
\n""")
myPrint(_list_matrix)
myPrint(_list_matrix_cp)
print("\n\n\n")

_list_matrix_cp[1][0] = "Gen"
print(f"""2222222-After updating copied matrix[1][0] to 'Gen'
_list_matrix == _list_matrix_cp ?: \t\t\t {_list_matrix == _list_matrix_cp},
id(_list_matrix) == id(_list_matrix_cp) ?: \t\t {id(_list_matrix) == id(_list_matrix_cp)},
id(_list_matrix[1]) == id(_list_matrix_cp[1]) ?: \t {id(_list_matrix[1]) == id(_list_matrix_cp[1])},
id(_list_matrix[1][0]) == id(_list_matrix_cp[1][0]) ?: \t {id(_list_matrix[1][0]) == id(_list_matrix_cp[1][0])}
\n""")
myPrint(_list_matrix)
myPrint(_list_matrix_cp)
print("\n\n\n")

_list_matrix[1][0] = "Bo"
print(f"""3333333-After updating original matrix[1][0] to 'Bo',
_list_matrix == _list_matrix_cp ?: \t\t\t {_list_matrix == _list_matrix_cp}
id(_list_matrix) == id(_list_matrix_cp) ?: \t\t {id(_list_matrix) == id(_list_matrix_cp)},
id(_list_matrix[1]) == id(_list_matrix_cp[1]) ?: \t {id(_list_matrix[1]) == id(_list_matrix_cp[1])},
id(_list_matrix[1][0]) == id(_list_matrix_cp[1][0]) ?: \t {id(_list_matrix[1][0]) == id(_list_matrix_cp[1][0])}
\n""")
myPrint(_list_matrix)
myPrint(_list_matrix_cp)
print("\n\n\n")

print(f"""{_segment_str}
To perform a deep copy, we need to import module copy, and use deepcopy():\n""")
import copy

_list_matrix = [[1,2],['a','b','c'],["Ming","Yan"]]
_list_matrix_cp2 = copy.deepcopy(_list_matrix)
print(f"""111111-After deep copy,  _list_matrix == _list_matrix_cp2 ? {_list_matrix == _list_matrix_cp2}
id(_list_matrix) == id(_list_matrix_cp2) ?: \t\t {id(_list_matrix) == id(_list_matrix_cp2)},
id(_list_matrix[0]) == id(_list_matrix_cp2[0]) ?: \t {id(_list_matrix[0]) == id(_list_matrix_cp2[0])},
id(_list_matrix[0][0]) == id(_list_matrix_cp2[0][0]) ?:\t {id(_list_matrix[0][0]) == id(_list_matrix_cp2[0][0])}
\n""")
myPrint(_list_matrix)
myPrint(_list_matrix_cp2)
print("\n\n\n")

_list_matrix_cp2[0][0] = "Gen"

print(f"""22222222-After updating copied matrix[1][0] to 'Gen'
_list_matrix == _list_matrix_cp2 ?: \t\t\t {_list_matrix == _list_matrix_cp2}
id(_list_matrix) == id(_list_matrix_cp2) ?: \t\t {id(_list_matrix) == id(_list_matrix_cp2)},
id(_list_matrix[0]) == id(_list_matrix_cp2[0]) ?: \t {id(_list_matrix[0]) == id(_list_matrix_cp2[0])},
id(_list_matrix[0][0]) == id(_list_matrix_cp2[0][0]) ?:\t {id(_list_matrix[0][0]) == id(_list_matrix_cp2[0][0])}
\n""")
myPrint(_list_matrix)
myPrint(_list_matrix_cp2)
print("\n\n\n")


_list_matrix[0][0] = "Bo"
print(f"""3333333-After updating original matrix[1][0] to 'Bo'
_list_matrix == _list_matrix_cp2 ? {_list_matrix == _list_matrix_cp2}
_list_matrix == _list_matrix_cp2 ?: \t\t\t {_list_matrix == _list_matrix_cp2}
id(_list_matrix) == id(_list_matrix_cp2) ?: \t\t {id(_list_matrix) == id(_list_matrix_cp2)},
id(_list_matrix[0]) == id(_list_matrix_cp2[0]) ?: \t {id(_list_matrix[0]) == id(_list_matrix_cp2[0])},
id(_list_matrix[0][0]) == id(_list_matrix_cp2[0][0]) ?:\t {id(_list_matrix[0][0]) == id(_list_matrix_cp2[0][0])},
\n""")
myPrint(_list_matrix)
myPrint(_list_matrix_cp2)

print(f"""{_segment_str}
Sorting lists \n""")


print(f"_list_fruits_1 is {_list_fruits_1}")
_list_fruits_4 = copy.deepcopy(_list_fruits_1)
print(f"_list_fruits_4 is {_list_fruits_4}")

_list_fruits_4.sort()
print(f"""111111-After sort by default: ascending order alphanumerically
_list_fruits_4 is {_list_fruits_4}""")

_list_fruits_4.sort(reverse = True)
print(f"""222222-After sort in reverse order:
_list_fruits_4 is {_list_fruits_4}""")

_list_fruits_4.sort(key=len)
print(f"""333333-After sort by key of len():
_list_fruits_4 is {_list_fruits_4}""")

_list_fruits_4.sort(key=len,reverse = True)
print(f"""444444-After sort by key of len() in descending order:
_list_fruits_4 is {_list_fruits_4}""")
print("\n\n\n")



print(f"""{_section_str}
9.6 Store Relationships in Dictionaries
""")

print(f"""{_segment_str}
What is a Dictionary?
A dictionary in Python holds information in pairs of data call key:value paris.
That is, each object in a dictionary has two parts: a key and a value.
key has to be immutable.
Dictionary works like Map in Java.
""")

print(f""" How to create a dictionary?
{_segment_str}
1. create a dictionary literal containing keys and values:
if you want to initialize an object of dictionary, just pass {{}}
## to escape a {{ in f print, use the same character.
""")


_dict_0 = {}
myPrint(_dict_0)

_dict_1 = {"California":"Sacramento","New York":"Albany","Texas":"Austin"}

myPrint(_dict_1)

print(f""" {_segment_str}
2. create a sequece of tuples using the dict() constructor:
if you want to create an empty dictionary, just call dict()
""")

_tuple_dict_0 = dict()
myPrint(_tuple_dict_0)

_tuple_dict_1 = (
    ("California","Sacramento"),
    ("New York","Albany"),
    ("Texas","Austin"))
_dict_tuple_1 = dict(_tuple_dict_1)
myPrint(_dict_tuple_1)


print(f""" {_segment_str}
Accessing Dictionary Values
To access a value in a dictionary, enclose the corresponding key in
square brackets ([ and ]) at the end of dictionary or a variable name
assigned to a dictionary
""")

print(f"_dict_1['Texas'] is {_dict_1['Texas']}")

print(f""" {_segment_str}
Adding and Removing Values in a Dictionary.
Like lists, dictionaries are mutable data structures.
This means you can add and remove items from a dictionary.

Each key in a dictionary can only be assigned a single value.
If a key is given a new value, Python just overwrites the old one:
""")

_dict_1['Colorado'] = 'Denver'

myPrint(_dict_1)

print("after _dict_1['Colorado'] = 'Not Denver'")
_dict_1['Colorado'] = 'Not Denver'

myPrint(_dict_1)

print("To remove an item from a dictionary, use the del keyword ")

del _dict_1['Colorado']
print("after del _dict_1['Colorado'] ")
myPrint(_dict_1)

print(f""" {_segment_str}
Checking the Existence of Dictionary Keys
""")

print(f"check if 'Texas' in _dict_1: {'Texas' in _dict_1 }")

print(f""" {_segment_str}
Iterate over a dictionary.
1. loop thru the keys
""")

_dict_1['Colorado'] = 'Denver'
del _dict_1['Texas']
_dict_1['Arizona'] = 'Pheonix'

print("Key:\t\t\tValue")
for k in _dict_1:
    print(f"""{k}:\t\t{_dict_1[k]}""")

print(f""" 
2. loop thru the items()
""")

print(f"""type of _dict_1.items() is {type(_dict_1.items())}""")

print("Key:\t\t\tValue")
for k, v in _dict_1.items():
    print(f"""{k}:\t\t{v}""")
    

print(f""" {_segment_str}
Dictionary Keys and Immutability
There is only one restriction on what constitutes a valid dictionary key.
Only immutable types are allowed. This means, for example, that a list cannot be a dictionary key.
""")

try:
    _dict_1[['a',2,'MY']] = "not a good key"
except TypeError:
    print("""Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'""")
except NameError:
    print("You must have some undefined variables listed")


print(f""" {_segment_str}
Nested Dictionaries
you cannot created nested dictionary using tuples, 
""")

_tuple_dict_2 = (
    ("California",("Sacramento","California Poppy")),
    ("New York",("Albany","Rose")),
    ("Texas",("Austin","Bluebonnet"))
    )

_dict_tuple_2 = dict(_tuple_dict_2)

myPrint(_dict_tuple_2)

print("you can create using dictionary literal: ")

_dict_2 = {
"California": {
"capital": "Sacramento",
"flower": "California Poppy"},
"New York": {
"capital": "Albany",
"flower": "Rose"},
"Texas": {
"capital": "Austin",
"flower": "Bluebonnet"}
}

myPrint(_dict_2)

for k1, v1 in _dict_2.items():
    for k2,v2 in v1.items():
        if k2 == 'capital':
            cap = v2
        elif k2 == 'flower':
            flower = v2
    print(f"The capital of {k1} is {cap}, and the flower of {k1} is {flower}")


print(f""" {_segment_str}
Review exercises
""")
captains = {}
captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'

captains = dict(
    (
        ('Enterprise','Picard'),
        ('Voyager','Janeway'),
        ('Defiant','Sisko')
    ))
_tuple_9_6_review = ('Enterprise', 'Discovery')

for t in _tuple_9_6_review:
    if(t in captains):
        pass
    else:
        captains[t] = 'unknown'

myPrint(captains)


print(f""" {_segment_str}
9.8 How to Pick a Data Structure
think about it by thinking what are the features each data structure has.
You should be able to figure out by yourself.
""")
