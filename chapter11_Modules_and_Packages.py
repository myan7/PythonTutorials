# Chapter 11 Modules and Packages

from Common import _section_str as sec ,_segment_str as seg ,myPrint as p


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
