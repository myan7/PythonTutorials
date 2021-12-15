# Chapter 12 File input and Output

from Common import _section_str as sec ,_segment_str as seg ,myPrint as sysout

print("Chapter 12 File input and Output")

print(f"""{sec}
12.1 Files and the File System
""")

print(f"""{seg}
The Anatomy of a File
Ultimately, a file is just a sequence of bytes called the contents of the file.
Different type of files have their ways of representation of the data.

The important thing to know here is
that there is nothing intrinsic to the file itself that
dictates how to interpret the contents
""")


print(f"""{seg}""")
print(r"""
File Path
for example:
1. Windows: C:\Users\myan\Documents\hello.txt
2. macOS: /Users/myan/Documents/hello.txt
3. Linux: /home/myan/Documents/hello.txt

The other major difference between Windows, macOS, and Ubuntu
files paths is that directories in a Windows file path are separated by
back slashes (\), whereas directories in macOS and Ubuntu file paths
are separated by forward slashes (/).
""")


print(f"""{sec}
12.2 Working With File Paths in Python
""")
import pathlib

print(f"""{seg}
Creating Path Objects
    1. from a string
""")

path = pathlib.Path("E:/pythonProject/PythonTutorials")
print(f"path is {path}")

print(r"""# Notice that the path of windows are different from what is in the intro
# this is because if you use back slash shown as in the intro,
# python will give out a SyntaxError:
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
# in position 2-3: truncated \UXXXXXXXX escape
# there are 2 ways to get around this problem:
# 1. use slash instead of back slash in the Windows path
#    Python can interpret this just fine and
#    will translate the path appropriately and
#    automatically when interfacing with the Windows operating system.
# 2. use (r"your path ") to convert the string to a raw string
#    This tells Python to ignore any escape sequences and just read the
#    string as-is.
""")

path2 = pathlib.Path(r"E:\pythonProject\PythonTutorials")
print(f"path2 is {path2}")

print(f"""{seg}
Creating Path Objects
    2. with Path.home() and Path.cwd() class method
""")

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()
print(f"home is {home}")
print(f"cwd is {cwd}")
print(r"""The Path.home() class method creates a Path object representing the
home directory regardless of which operating system the code runs
on:
home = pathlib.Path.home()

The Path.cwd() class method returns a Path object representing the
current working directory, or CWD.
The current working directory is a dynamic reference to a directory
that depends on where a process on the computer is currently working.
""")

print(f"""{seg}
Creating Path Objects
    3. with the /operator
""")
print(r"""If you have an existing Path object, you can use the / operator to extend
the path with subdirectories or file names.
""")

packagePath = cwd/"mypackage"/"mysubpackage"
print(packagePath,"\n\n")

print(f"""{seg}
Absolute vs. Relative Paths
""")

relativePath = pathlib.Path("Desktop")
sysout(relativePath)
print(r'relativePath = pathlib.Path("Desktop")')
print(f"""relativePath is {relativePath},
is it an absolute path: {relativePath.is_absolute()},
its absolute path is {relativePath.absolute()}
its absolute path as posix is {relativePath.absolute().as_posix()}
""")

relativePath2 = pathlib.Path(r"Desktop")
print(r'relativePath2 = pathlib.Path(r"Desktop")')
print(f"""relativePath2 is {relativePath2},
is it an absolute path: {relativePath2.is_absolute()},
its absolute path is {relativePath2.absolute()}
""")



print(f"""{seg}
Accessing File Path Components
""")

print(r"""
type(relativePath) will give you the type of that object
dir(relativePath) will give you the properties defined in that object

>>> type(relativePath.parent)
<class 'pathlib.WindowsPath'>

>>> dir(relativePath)
['__bytes__', '__class__', '__class_getitem__', '__delattr__', '__dir__',
'__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__fspath__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__rtruediv__', '__setattr__',
'__sizeof__', '__slots__', '__str__', '__subclasshook__', '__truediv__',
'_accessor', '_cached_cparts', '_cparts', '_drv', '_flavour',
'_format_parsed_parts', '_from_parsed_parts', '_from_parts', '_hash',
'_init', '_make_child', '_make_child_relpath', '_opener', '_parse_args',
'_parts', '_pparts', '_raw_open', '_root', '_str', 'absolute', 'anchor',
'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 'exists', 'expanduser',
'glob', 'group', 'home', 'is_absolute', 'is_block_device', 'is_char_device',
'is_dir', 'is_fifo', 'is_file', 'is_mount', 'is_relative_to', 'is_reserved',
'is_socket', 'is_symlink', 'iterdir', 'joinpath', 'lchmod', 'link_to',
'lstat', 'match', 'mkdir', 'name', 'open', 'owner', 'parent', 'parents',
'parts', 'read_bytes', 'read_text', 'readlink', 'relative_to', 'rename',
'replace', 'resolve', 'rglob', 'rmdir', 'root', 'samefile', 'stat', 'stem',
'suffix', 'suffixes', 'symlink_to', 'touch','unlink', 'with_name',
'with_stem', 'with_suffix', 'write_bytes', 'write_text']

for usage,check help()
""")
_dirList = relativePath.absolute().parents

sysout(_dirList)
for x in _dirList:
    print(x)
print()
print("That means you can save parents in a list")
_dirList = list(relativePath.absolute().parents)

sysout(_dirList)
for x in _dirList:
    print(x)

print(r"""
relativePath.absolute().anchor will give you the root directory

""")
print(f"{relativePath.absolute().anchor}")


print(r"""
relativePath.name will give you the name of the directory or the file name
""")
print(f"relativePath.name is {relativePath.name}")
relativePath = pathlib.Path("mypackage/__init__.py")
print(f"""After relativePath = pathlib.Path("mypackage/__init__.py")
relativePath.name is {relativePath.name}""")

print(r"""
for a file name, left to the dot(.) is called stem
right to the dot(.), including the dot, is called extension, or suffix
""")

print(f"relativePath.stem is {relativePath.stem}")
print(f"relativePath.suffix is {relativePath.suffix}")

print(f"""{seg}
Checking Whether Or Not a File Path Exists

relativePath.exists() = {relativePath.exists()}
relativePath.is_dir() = {relativePath.is_dir()}
relativePath.is_file() {relativePath.is_file()}
""")


print(f"""{sec}
12.3 Common File System Operations
you will learn how to
create/move a file or directory
""")

print(f"""{seg}
Creating Directories and Files
    1. Creating Directories
    to create directory, you need to call mkdir()
    passing exist_ok=True if directory already exists, and 
    and parents=True if nested directories are needed.
""")

print(r"""
>>> help(Path.mkdir)
Help on function mkdir in module pathlib:

mkdir(self, mode=511, parents=False, exist_ok=False)
    Create a new directory at this given path.
""")

from pathlib import Path

currPath = Path.cwd()
wdPath = currPath/"chapter12_Exercise"
if wdPath.exists():
    file = "directory" if wdPath.is_dir() else "file"
    print(f"{file} of {wdPath} already exists.")
else:
    wdPath.mkdir()

print(r"""
although if else works fine
you can also use wdPath.mkdir(exist_ok=True)
and it is shorter and doesn't sacrifice readability.
""")
wdPath.mkdir(exist_ok=True)

nestedPath = wdPath/"folder_A"/"folder_B"
try:
    nestedPath.mkdir()
except FileNotFoundError:
    print(r"""Traceback (most recent call last):
  File "E:\pythonProject\PythonTutorials\chapter12_File_Input_and_Output.py",
  line 227, in <module>
    nestedPath.mkdir()
  File "D:\Program Files\Python39\lib\pathlib.py", line 1323, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [WinError 3] The system cannot find the path specified:
'E:\\pythonProject\\PythonTutorials\\chapter12_Exercise\\folder_A\\folder_B'

to solve this issue, you need to specify another parameter
parents = True
""")
except FileExistsError:
    print(f"file already exists")

nestedPath.mkdir(parents=True, exist_ok=True)

print(f"""{seg}
Creating Directories and Files
    2. Creating Files
    to create files, you need to call touch()
""")
print(r"""
>>> help(Path.touch)
Help on function touch in module pathlib:

touch(self, mode=438, exist_ok=True)
    Create this file with the given access mode, if it doesn't exist.
    notice there is no parents in the definition, so this means
    you need to create the parents directory first.
    also exist_ok is default to True, so no need to worry if you will
    overwrite the file.
    see review exercise as an example.
""")

file = nestedPath/"test_a_b.txt"
file.touch()

print(f"""{seg}
Iterating Over Directory Contents
""")

print(r"""
Using pathlib, you can iterate over the contents of a directory.

Path.iterdir() method returns an iterator over Path objects
representing each item in the directory.

>>> help(Path.iterdir)
Help on function iterdir in module pathlib:

iterdir(self)
    Iterate over the files in this directory, so check is_dir() will be nice.
    Does not yield any result for the special paths '.' and '..'.
""")

file_iterdir = file.iterdir()
print(f"""file.iterdir() is {file.iterdir()}
its type is {type(file_iterdir)}

""")


if file.is_dir():
    for p in file_iterdir:
        print(p)
else:
    print("not a directory.")

dir_iterdir = nestedPath.iterdir()
if nestedPath.is_dir():
    for p in dir_iterdir:
        print(p)
else:
    print("not a directory.")

print(r"""
generator type is iterable, so you can save it to a list as well.
You won’t often need to convert this to a list,
but we’ll do it in subsequent examples to keep the code short.
Generally, you’ll use .iterdir()
in a for loop like you did in the first example
""")
list_dir_iterdir = list(nestedPath.iterdir())

if nestedPath.is_dir():
    for p in list_dir_iterdir:
        if p.is_dir():
            print("Directory:",p)
        elif p.is_file():
            print("File:",p)
        else:
            print("Unknown:",p)
else:
    print("not a directory.")

print(r"""
Notice that .iterdir() only returns items that are directly contained
in the new_directoy/ folder.
That is, you can’t what is in the subfolder if there is any.
in this case, folder_C
""")


print(f"""{seg}
Searching For Files In a Directory
""")

print(r"""
You can use the Path.glob() method
on a path representing a directory to get an iterable over directory
contents that meet some criteria.

>>> help(Path.glob)
Help on function glob in module pathlib:

glob(self, pattern)
    Iterate over this subtree and yield all existing files (of any
    kind, including directories) matching the given relative pattern.
""")

nestedPath_glob = nestedPath.glob("test_?.txt")

for f in nestedPath_glob:
    if f.is_file():
        print(f)
print()
nestedPath_glob2 = nestedPath.glob("test*.txt")
for f in nestedPath_glob2:
    if f.is_file():
        print(f)
print()
nestedPath_glob3 = nestedPath.glob("test_[abc]*.txt")
for f in nestedPath_glob3:
    if f.is_file():
        print(f)
print()
relativePath_parent = relativePath.absolute().parent
relativePath_parent_glob = relativePath_parent.glob("*")
list_relativePath_parent_glob = list(relativePath_parent_glob)
for f in list_relativePath_parent_glob:
    print(f"files are {f}")
    if f.is_file():
        print(f"is a file")
    elif f.is_dir():
        print(f"is a directory")



print(r"""
Recursive Matching With The ** Wildcard
but how to go to the sub directories for target files?
use ** wildcard.
""")

relativePath_parent2 = relativePath_parent.parent
relativePath_parent2_glob2 = relativePath_parent2.glob("**/*test*")
list_relativePath_parent2_glob2 = list(relativePath_parent2_glob2)
for f in list_relativePath_parent2_glob2:
    print(f"files are {f}")
    if f.is_file():
        print(f"is a file")
    elif f.is_dir():
        print(f"is a directory")


print(r"""
or you can use rglob() for recursive matching.
""")
relativePath_parent2_glob2 = relativePath_parent2.rglob("test*")
list_relativePath_parent2_glob2 = list(relativePath_parent2_glob2)
for f in list_relativePath_parent2_glob2:
    print(f"files are {f}")
    if f.is_file():
        print(f"is a file")
    elif f.is_dir():
        print(f"is a directory")


print(f"""{seg}
Moving and Deleting Files and Folders
    1.To move a file, use the .replace() method.
""")
print(r"""
>>> help(Path.replace)
Help on function replace in module pathlib:

replace(self, target)
    Rename this path to the target path, overwriting if that path exists.
    
    The target path may be absolute or relative. Relative paths are
    interpreted relative to the current working directory, *not* the
    directory of the Path object.
    
    Returns the new Path instance pointing to the target path.
""")
currPath = Path.cwd()
chapter12 = currPath/"chapter12_Exercise"
chapter12.mkdir(exist_ok=True)

## check what files are in this directory
chapter12_glob = list(chapter12.glob("*"))
origin = ""
for f in chapter12_glob:
    tempPath = chapter12
    if f.is_dir():
        print(f"Dictory:{f}")
    if f.is_file():
        print(f"File: {f}")
        if "test" in f.__str__():
            origin = f
print(r"""
1st time run:
Dictory:E:\pythonProject\PythonTutorials\chapter12_Exercise\folder_A
File: E:\pythonProject\PythonTutorials\chapter12_Exercise\test.txt
E:\pythonProject\PythonTutorials\chapter12_Exercise\test.txt has been moved to
E:\pythonProject\PythonTutorials\chapter12_Exercise\folder_A\destination_of_replace.txt
""")

print(r"""
2nd time run:
E:\pythonProject\PythonTutorials\chapter12_Exercise\folder_A\destination_of_replace.txt already exists.
are you sure you want to replace?Y
Traceback (most recent call last):
  File "E:\pythonProject\PythonTutorials\chapter12_File_Input_and_Output.py", line 469, in <module>
    origin.replace(destination)
TypeError: replace expected at least 2 arguments, got 1
This is because the source file has been moved to destination already.
there is no source file, origin in the directory.
origin is now "".
""")

print(r"""
3rd time run:
after I added a file check for origin:
origin file is missing, could be moved already.
You can always create a file with "test" in directory chapter12_Exercise,
and play with it.
""")

destination = chapter12/"folder_A"/"destination_of_replace.txt"

if origin != "":
    if not destination.exists():
        origin.replace(destination)
        print(f"""{origin}
    has been moved to
    {destination}""")
    else:
        message = input(f"""{destination} already exists.
    are you sure you want to replace?""")
        if message.title() == 'Y':
            origin.replace(destination)
else:
    print("origin file is missing, could be moved already.")



print(f"""
If the destination path already exists, .replace() overwrites the
destination with the source file without raising any kind of exception.
This can cause undesired loss of data if you aren’t careful.
You may want to first check if the destination file exists, and
move the file only in the case that it does not:
if not destination.exists():
    source.replace(destination)

also you may want to check if the source exists too!
{seg}
Moving and Deleting Files and Folders
    2.To move a directory, use the .replace() method.
""")


print(f"""{seg}
Moving and Deleting Files and Folders
    3.To remove a file, use the .unlink() method.
    If the path that you call .unlink() does not exists, a FileNotFoundError
    exception is raised:
        FileNotFoundError:The system cannot find the file specified:
    If you want to ignore the exception,
    set the optional missing_ok parameter to True:
        file_path.unlink(missing_ok=True)
    In this case, nothing actually happens because the file located at
    file_path does not exist.
""")


print(f"""{seg}
Moving and Deleting Files and Folders
    4.To remove a directory, use the .rmdir() method.
    .unlink() only works for paths representing files.
    To remove a directory, use the .rmdir() method. 
""")


print(f"""{seg}
Moving and Deleting Files and Folders
    5.To remove a directory with sub directories,
    use the rmtree() method from the built-in shutil module.
""")

print(f"""{sec}
12.5 Reading and Writing Files
{sec}
""")


print(f"""{seg}
Understanding Text Files
{seg}
refer to encoding
https://realpython.com/python-encodings-guide/#enter-unicode
""")


print(f"""{seg}
Python File Objects
{seg}
1. open a file
{seg}

built-in open() vs Path.open()
according to io's documentation:
io.open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
This is an alias for the builtin open() function.
https://docs.python.org/3/library/io.html#io.open

pathlib.Path.open is just a wrapper for the built-in open function.
{seg}
The with Statement
{seg}
To ensure that file system resources are cleaned up even if a program
crashes, you can open a file in a with statement.
this is called context manager.
Context managers allow you to allocate and release resources precisely when you want to.
The most widely used example of context managers is the with statement.

refer to:
https://book.pythontips.com/en/latest/context_managers.html


""")

print(f"""{seg}
Python File Objects
{seg}
2. Reading data from a file
{seg}
The .read() method reads all of the text in the file and returns it as a
string value

The .readlines() method returns an iterable of lines from the file.
""")

print(f"\nprint the destination file directly and then it's name:")
with open(destination,"r") as f:
        print(f"destination is \n{f}")
        print(f"destination.name is \n{f.name}")


print(f"\nprint the file by looping thru it:")
with open(destination,encoding='utf8') as f:
#    print(f"destination is {f}")
    print()
    if len(f.readlines()) > 0:
        print(f"yes, length is {len(f.readlines()) }")
        for c in f.readlines():
            print(f"content of destintion is {c}")
    else:
        print(f"length of destination is len(f.readlines())")

print(f"\nread the file first and then check the type and length.")
with open(destination,"r",encoding='UTF-8') as f:
    text = f.readlines()
    print(f"type of text is {type(text)}")
    print(f"length of text is {len(text)}")          # why this works？
    print(f"length of f.readlines() is {len(f.readlines())}") # why this doesn't work?
    text2 = f.read()
    print(f"type of text2 is {type(text2)}")
    print(f"test2 is {text2}")
    print(f"length of text2 is {len(text2)}")          
    print(f"length of f.read() is {len(f.read())}") 
    
    print(f"content of destintion is:")
    lineNum = 1
    for c in text:
        print(f"{lineNum}: {c}",end='')
        lineNum += 1
print(r"""
read(size=-1, /) method of _io.TextIOWrapper instance
    Read at most n characters from stream.
    
    Read from underlying buffer until we have n characters or we hit EOF.
    If n is negative or omitted, read until EOF.

>>> help(f.readlines)
Help on built-in function readlines:

readlines(hint=-1, /) method of _io.TextIOWrapper instance
    Return a list of lines from the stream.
    
    hint can be specified to control the number of lines read: no more
    lines will be read if the total size (in bytes/characters) of all
    lines so far exceeds hint.
""")


destination2 = chapter12/"folder_A"/"destination_of_replace2.txt"

#destination2.touch()

with open(destination2,"w") as f:
    f.write("Hello\nPython\nMy name is Ming")

with open(destination2,"r") as f:
    text = f.readlines()
    print(f"""
destination2 is {destination2};
destination2 type is {type(destination2)};
length of f.readlines() is {len(f.readlines())};

# you have to store f.readlines() to a variable
text = f.readlines()

text is {text};
text type is {type(text)}
length of text is {len(text)};
""")
    for c in text:
        print(c,end='')


print(f"""
{seg}
Python File Objects
{seg}
3. Writing Data To a File
{seg}

To write data to a plain text file, you pass a string to a file object’s
.write() method. The file object must be opened in write mode by
passing the value "w" to the mode parameter.

You can append data to the end of a file by opening the file in append
mode by passing the value "a" to the mode parameter.

You can write multiple lines to a file at the same time using the
.writelines() method. First, create a list of strings:
Then open the file in write mode and use the .writelines() method to
write each string in the list to the file:
""")


print(f"""{seg}
Python File Objects
{seg}
Review Exercises
{seg}
""")

revEx_12 = chapter12/"ReviewExercise"/"chapter12_reviewExercise"/"revEx.txt"
# revEx_12 points to a new file that hasn't been created, along with the parents dir
# first, create the parent directory


revEx_12.parent.mkdir(parents=True,exist_ok=True)
print(f"parent directory has been created.")

# contents need to be written in the file needs to be a list of strings
# with newlines.
contents = ["Discovery\n","Enterprise\n","Defiant\n","Voyager"]

if revEx_12.exists():
    pass
else:
    with open(revEx_12,"w") as rv:
        rv.writelines(contents)

with open(revEx_12,"r") as rv:
    text = rv.readlines()
    for l in text:
        print(l,end='')

print()
print()
print("only print out startship starting with letter D")
with open(revEx_12,"r") as rv:
    text = rv.readlines()
    for l in text:
        if l[0] == 'D':
            print(l,end='')



print(f"""{sec}
12.6 Read and Write CSV Data
{sec}
""")

csv_12 = chapter12/"csv_12"
csv_12.mkdir(parents = True,exist_ok=True)
temperature_readings = [68, 65, 68, 70, 74, 72]
temp_csv = csv_12/"temp_readings.csv"
with open(temp_csv,"w") as csv:
    csv.write(str(temperature_readings[0]))
    for t in temperature_readings[1:]:
        csv.write(f",{t}")

with open(temp_csv,"r") as csv:
    content = csv.read()
    print(content)
    sysout(content)

temps = content.split(",")
sysout(temps)

# list comprehension.
temps_int = [int(x) for x in temps]
sysout(temps_int)


print(f"""{seg}
The csv Module
1. Writing CSV Files With csv.writer
2. Reading CSV Files With csv.reader
{seg}
""")

import csv

daily_temps = [[68, 65, 68, 70, 74, 72],[67, 67, 70, 72, 72, 70],[68, 70, 74, 76, 74, 73],]

# create a csv file that you want to write data in.
daily_temps_csv = csv_12/"daily_temps.csv"

# without with statement

# create a file object.
file = daily_temps_csv.open(mode = "w",encoding="utf8")

# create a new csv writer object
writer = csv.writer(file)

for row in daily_temps:
    print(f"row is {row}")
    print(f"type of row is {type(row)}")
    writer.writerow(row)
    print("row appended.")

file.close()


# use with statement:
daily_temps_csv2 = csv_12/"daily_temps2.csv"
with open(daily_temps_csv2,"w",encoding = "utf8") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(daily_temps)

print("csv_writer completed")
print()
with open(daily_temps_csv2,"r") as f:
    content = f.readlines()
    print(content)

print(f"""{seg}
The csv Module
2. Reading CSV Files With csv.reader
{seg}
""")


print(f"""{seg}
The csv Module
1. Writing CSV Files With csv.writer
2. Reading CSV Files With csv.reader
3.
{seg}
""")
