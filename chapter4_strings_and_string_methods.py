print("This is Chapter 4 - Strings and String Methods")
# 4.1 what is a String?

## ================================================================ ##
print()
# in the interactive window, type
## ================================================================ ##
print("## ================================================================ ##")
print("4.1 String has a type, class 'str'")
type("Hello world!")
# you should see something like this:
##>>> type("Hello world!")
##<class 'str'>
# type() also works with variable
phrase = "Hello Python！"
type(phrase)
##>>> phrase = "Hello Python！"
##>>> type(phrase)
##<class 'str'>

# every string has 3 properties
# contains all characters
# has a length
# all characters appear in a sequence

# you can use either single quote or double quotes, but they have to be in pair.
# and you can using single quote within double quotes or vice versa.
# for example

str1 = "He said 'Python will help you do a better job!'"
str2 = 'I replied "Thank you, that is why I am learning it."'
print(str1)
print(str2)

# Notice it is your responsibility to keep consistency of your code.
# use either double quotes or single quote only, do not mix them like str1 and str2!

print("4.1 String has a length, len()")
letters = "abcdefg"
print("letter is",letters,", and its length is ",len(letters))

# multiple lines of string
# 1, you can you backslash to separate long string into a new line.
# to be PEP8 compliant, the total length of the line, including the backslash
# must be 79 characters or less.
long_string = "This is a very long string, because I need to show you how long \
it is so that I need to put some mumble jumbo here and there to demonstrate \
what I meant. This string is using backslash."
print(long_string)

# 2, you can use triple quotes, no matter single or double quotes
long_string1 ="""                 This is a very long string using triple quotes, because I
                 need to show you how long it is so that I need to put some
                 mumble jumbo here and there to demonstrate what I meant.
                 and it preserves white spaces...."""
print(long_string1)
# notice triple quotes preserve whitespaces, including new lines.
# used as docstrings, for documentation.



## ================================================================ ##
print("## ================================================================ ##")
print("4.2 Concatenation, Indexing, and Slicing")

# concatenation
string1 = "python"
string2 = "tutorial"
string_12 = string1+string2
print(string_12)
string_1_2 = string1 + " " + string2
print(string_1_2)

# indexing
# string is an array of character.
# index starts from 0.
# use [] square brackets to index char in a string
print("string1 is",string1)
print("string1[0] is",string1[0])
print("The length of string1 is",len(string1))
print("string1[6] will give you an index out of bound error,\
and string1[5] is the last character in string1, which is",string1[5])
print("Python also supports negative index, string1[-1] is", string1[-1])
print()
print("for i in range(len(string1)):")
for i in range(len(string1)):
    print(string1[i])
print()
print("for i in string1:")
for i in string1:
    print(i)
print()
print("for i in range(-6,-1):")
for i in range(-6,-1):
    print(string1[i])
print()
print("for i in range(-6,0):")
for i in range(-6,0):
    print(string1[i])
print()
print("for i in range(-6):")
for i in range(-6):
    print(i)
    print(string1[i])
##>>> range(6)
##range(0, 6)
##>>> range(-6)
##range(0, -6)
   
print()
print("for i in range(-6,-1,2):")
for i in range(-6,-1,2): 
  print(string1[i])

print()
# string slicing
# you can use [start_index:end_index] to extract a portion of a string
address = "200 N Jefferson street Chicago, IL 60661 APT 507"
street_number = address[0:3]
print("street_number is",street_number)
direction = address[4:5]
print("direction is",direction)
street_name = address[6:22]
print("street_name is",street_name)
city = address[23:30]
print("city is",city)
state = address[32:34]
print("state is",state)
zip_code = address[35:41]
print("zip_code is",zip_code)
unit_number = address[-3:] # to include the final character, omit the 2nd number
print("Unit_number is",unit_number)
print(type(address))
print(type(unit_number))

print()
# converting string case
# it is a string, use .lower() and .upper()
# the function definition is .lower(), instead of lower()
address_lower = address.lower()
print("address_lower is",address_lower)
address_upper = address.upper()
print("address_upper is",address_upper)
address_len = len(address)
print("address_len is", address_len)
# len() is a stand-alone function,
# .upper() and .lower() must be used in conjunction with a string.


print()
### remove whitespace from a string
##there are 3 string methods that you can use to remove white spaces from a string
##.rstrip() - removes whitespace from the right-hand side
##.lstrip() - removes whitespace from the left-hand side
##.strip() - removes whitespace from both sides

print("\noriginal strings:")
string_wt_leftB = "     My name is Ming."
print(string_wt_leftB)
string_wt_rightB = "My name is Ming.     "
print(string_wt_rightB)
string_wt_bothB = "     My name is Ming.     "
print(string_wt_bothB)
string_wt_extraB = "     My  name  is  Ming.     "
print(string_wt_extraB)


print("\nsanitized strings:")
string_sanitized = string_wt_leftB.lstrip()
print(string_sanitized)
string_sanitized = string_wt_rightB.rstrip()
print(string_sanitized)
string_sanitized = string_wt_bothB.strip()
print(string_sanitized)
import re
string_sanitized = re.sub(' +', ' ', string_wt_extraB).strip()
print(string_sanitized)

print()
# Determine if a string starts or ends with a particular string
starship = "Enterprise"
ans = starship.startswith("en")
print(ans)
ans = starship.startswith("En")
print(ans)
ans = starship.endswith("prise")
print(ans)

print()
# string methods and immutability
# string is immutable and you can use IDLE's intelligence feature by adding . and
# wait for the auto complete.

ans = starship.isascii()
print(ans)

print()
## ================================================================ ##
print("## ================================================================ ##")
print("4.4 Interact With User Input")

# input() will give you the ability to take user input, you can test it in the
# interactive window. whatever you put in the interactive window, python will
# it and output it in the interactive window.

# uncomment the following real code by pressing alt+4
prompt = "Hey, what's up?\n"
user_input = input(prompt)
print("You replied:", user_input)


print()
## ================================================================ ##
print("## ================================================================ ##")
print("4.5 Challenge: Pick aprt your user's input")

# in this section, we are going to test the functionality
# and then create another python script called chapter4_first_letter.py
# which will prompt the user to input his password,
# and get the first letter and capitalize it.

# uncomment the following real code by pressing alt+4
user_input = input("gimme your password!\n")
print("My password is",user_input[0].upper())


print()
## ================================================================ ##
print("## ================================================================ ##")
print("4.6 Working with Strings and Numbers ")
# learn how to convert, learn how to apply arithmetic operations on strings

# to concatenate, use +
id = "001"
print("id is",id)
print("id+id is",id+id)
print("id*3 is",id*3)

# converting strings to numbers

print("id is",id)
print("type of id is",type(id))

int_id = int(id)
print("int_id is",int_id)
print("type of int_id is",type(int_id))

float_id = float(id)
print("float_id is",float_id)
print("type of float_id is",type(float_id))

# convert numbers to strings

number_of_phones = 6
print("I got "+str(number_of_phones)+" phones.")
for i in range(6):
    if(number_of_phones - i != 1):
        print("I got "+str(number_of_phones - i)+" phones.")
    else:
        print("I got "+str(number_of_phones - i)+" phone.")

# you can also str() those keywords
print(str(print))
print(str(int))

print()
## ================================================================ ##
print("## ================================================================ ##")
print("4.7 Streamline your print statement")
# string interpolation

first_name = "Ming"
last_name = "Yan"
years_of_service = 3
company = "Transunion"
from datetime import date
join_date = date(2018,7,9)
print(join_date)
print(first_name + " " + last_name + " joined " + company + " "+
      str(years_of_service) + "years ago,"+ " on " +
      str(join_date) +".")
# it is hard to read, fortunately, there is a third way of combining strings.
# formmated string literals, more commonly known as f-strings.
sentence_1 = f"""{first_name} {last_name} joined {company} {years_of_service}
                years ago, on {str(join_date)}."""
sentence_2 = f"{first_name} {last_name} joined {company} {years_of_service} years ago, on {join_date}."
print(sentence_1)
print(sentence_2)
# 1. the string literal starts with the letter f before the opening
#    quotation mark
# 2. variable names surrounded by curly braces {}, are replaces with their
#    corrsponding values without using str()

# f-strings supports python expressions.
# f-strings are only available in Python version 3.6 and above.
num1 = 3
num2 = 4
calculation = f"{num1} * {num2} equals {num1*num2}."
print(calculation)

# In earlier versions of Python, the .format() method can be used to get the
# same results. but it is hard to read as well. 
sentence_3 = "{} {} joined {} {} years ago, on {}.".format(first_name,last_name,company,years_of_service,join_date)
print(sentence_3)
# For an in-depth guide to f-strings and
# comparisons to other string formatting techniques,
# check out the
# Python 3’s f-Strings: An Improved String Formatting Syntax (Guide)
# https://realpython.com/python-f-strings/

# you can also use the similar style of printf() function in C, use %d %s to format those strings
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
sentence_4 = '%(first)s has been working for %(company1)s for %(years)02d years.' %{'first': "Ming", "company1": "Transunion", "years": 3}
print(sentence_4)
# just need to know this type of formatting and understand it, don't use it in your code.



print()
## ================================================================ ##
print("## ================================================================ ##")
print("4.8 Find a string in a string")
position = sentence_1.find("Trans")
print(f"Trans first appears at index of {position} in string: {sentence_4}")



dummy_string = "On a case by case basis"
print(dummy_string)

updated_dummy_string = dummy_string.replace("case","CASE")
print(updated_dummy_string)

