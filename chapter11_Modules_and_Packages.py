# Chapter 11 Modules and Packages

from Common import _section_str as sec ,_segment_str as seg ,myPrint as sysout


print(" Chapter 11 Modules and Packages ")

print(f"""{sec}
11.1 Working With Modules
Module is like package in Java, just a namespace which can be imported
to make everything in there becomes available locally without recoding them.
""")

print(f"""{seg}
Creating Modules
Technically, every Python script file
that you have created while reading this book is a module
""")

print(f"""{seg}
Importing One Module Into Another

A namespace is a collection of names, such as variable names,
function names, and class names. Every Python module has its own
namespace.

To access a name in an imported module from the calling module, type
the imported module’s name followed by a dot (.) and the name you
want to use:
<module>.<name>


""")


print(f"""{seg}
Import Statement Variations

1. import <module> as <other_name>
You can change the name of an import using the as keyword
    There are two reasons you might use the
    import <module> as <other_name> format:
        1. The module name is long and you wish to import an abbreviated
           version of it
        2. The module name clashes with an existing name in the calling
           module


2. from <module> import <name>
Instead of importing the entire namespace,
you can import only a specific name from a module.
if you want to import more than 1 package,
use comma as separation.
""")

print(f"""{seg}
Summary of Import Statements
Why Use Namespaces?

1. They group names into logical containers
2. They prevent clashes between duplicate names
3. They provide context to names

""")



print(f"""{sec}
11.2 Working With Packages

Modules allow you to divide a program in to individual files that can be
reused as needed. Related code can be organized into a single module
and kept separate from other code.
Package take this organizational structure one step further
by allowing you to group related modules under a single namespace.
""")

print(f"""{seg}
A package is a folder that contains one or more Python modules. It
must also contain a special module called __init__.py.

The __init__.py module doesn’t need to contain any code! It only
needs to exist so that Python recognizes the mypackage/ folder as a
Python package.
""")


## the following code existing in /chapter11_package/main.py as well.
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


print(f"""{seg}
Guidelines For Importing Packages

The same guidelines for importing names from modules apply to importing modules form packages. You should prefer that imports be
as explicit as possible, so that the modules and names imported from
the package into the calling module have the appropriate context.

the following format is generally ambiguous and should only
be used when there is no risk of importing a name from a module that
clashes with a name in the calling module:

from <package>.<module> import <name>
""")


print(f"""{seg}
Importing Modules From Subpackages (nested package)

I created a sub folder under mypackage, called mysubpakcage,
in which there are 2 files. __init__.py and module3.py
""")

from mypackage.mysubpackage.module3 import people

sysout(people)

for p in people:
    greet(p)
    depart(p)
