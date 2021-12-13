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
""")
