print(" Chapter 8 Conditional Logic and Control Flow ")

print("=======================================================================")
print(" 8.1 Compare Values ")

print("a is larger than b? ", 'a' > 'b')
## to output a character's value in Python, use ord()
## ord(c, /), Return the Unicode code point for a one-character string. 
print("character a can be reprensented by an int, " ,ord('a'))
print("character b can be reprensented by an int, " ,ord('b'))
print("character A can be reprensented by an int, " ,ord('A'))


print("=======================================================================")
print(" 8.4 Challenge: Find the Factors of a Number ")


def _find_factors_of(x):
    for i in range(1,x):
        if(x % i == 0):
            print(f'{i} is a factor of {x}.')

_find_factors_of(12)

print("another example ")

def _find_factors_of2(x):
    for i in range(1,x):
        if((x/i).is_integer()):
            print(f'{i} is a factor of {x}.')

_find_factors_of2(12)

def _sum_of_evens(x):
    sum = 0
    for i in range(1,x):
        if (i % 2 == 0):
            sum += i
            #print(sum)
    return sum

x = 100
print(f'sum of even to {x} is {_sum_of_evens(x)}')


print("=======================================================================")
print(" 8.5 Break Out of the Pattern ")

## The break keyword tells Python to literally break out of a loop. That is,
## the loop stops completely and any code after the loop is executed.
print()
print("example of break, output 0~5")
for i in range(0,5):
    if(i == 2):
        break
    print(f"current number is {i}")

print()
print("example of continue, output 0~5")
## The break keyword tells Python to literally break out of a loop. That is,
## the loop stops completely and any code after the loop is executed.

for i in range(0,5):
    if(i == 2):
        continue
    print(f"current number is {i}")


## To summarize, the break keyword is used to stop a loop if a certain
## condition is met, and the continue keyword is used to skip an iteration
## of a loop when a certain condition is met.
print()
print("for else loops example")

## use the following two strings to see for else loop.
print("phrase = 'This is just a testing phrase'")
phrase = "This is just a testing phrase"
for c in phrase:
    if c == 'X':
        break
else:
    print("There was no 'X' in the phrase")
    
print()
print("updated phrase = 'X marks the spot.'")

phrase = "X marks the spot"
for c in phrase:
    if c == 'X':
        break
else:
    print("There was no 'X' in the phrase")

## Any code in the else block after a for loop is executed only if the for
## loop completes without encountering a break statement
print()
print("Practical example of for else loop")
for n in range(3):
    password = input("Password:")
    if password == "I<3Ming":
        break
    print("Password is incorrect")
else:
    print("Suspicious activity. The authorities have been alerted.")

## everything discussed here also works for while loops.
## That is, you can use break and continue inside a while loop. while
## loops can even have an else clause!

print("=======================================================================")
print(" 8.6 Recover From Errors ")

print()
print("A ValueError occurs when an operation encounters an invalid value")
print()
print("""A TypeError occurs
      when an operation is performed on a value of the wrong type""")
print()
print("""A NameError occurs when you try to use a variable name
      that hasn’t been defined yet""")
print()
print("A ZeroDivisionError occurs when the divisor in a division operation is 0")
print()
print("""An OverflowError occurs
      when the result of an arithmetic operation is too large.""")
print()
print("""Instead of letting the program crash,
you can catch the error if it occurs and do something else instead. """)

try:
    number = int(input("Enter an integer: \n"))
    print(f"the number you entered is {number}")
except ValueError:
    print("That was not an integer")

num1 = float(input("Please specify num1: \n"))
num2 = float(input("Please specify num2: \n"))

def divide(a, b):
    try:
        res = a/b
        print(f"num1/num2 is {res:.2f}.")
## The colon (:) after the variable n indicates that everything after it is
## part of the formatting specification. In this example, the formatting
## specification is .2f
    except (TypeError, ZeroDivisionError):
        print("Encountered a problem.")

divide(num1, num2)


def divide2(a, b):
    try:
        res = a/b
        print(f"num1/num2 is {res:.2f}.")
    except TypeError:
        print("Both arguments must be numbers.")
    except ZeroDivisionError:
        print("num2 must not be 0")

divide2(num1, num2)

## You can use the except keyword by itself without naming specific exceptions:
## This might sound like a great way to ensure your program never
## crashes, but this is actually bad idea and the pattern is
## generally frowned upon!
def divide3(a, b):
    try:
        res = a/b
        print(f"num1/num2 is {res:.2f}.")
    except:
        print("Something is wrong.")

divide3(num1, num2)

print("=======================================================================")
print(" 8.7 Simulate Events and Calculate Probabilities ")

import random
import time
print(random.randint(1,100))
"""
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
"""


## Return an object that produces a sequence of integers
## from start (inclusive) to stop (exclusive) by step.
## range(i, j) produces i, i+1, i+2, ..., j-1.

toss_time = int(input("Enter how many times you want me to toss the coin: \n"))

## random.randInt(i,j) will return a random int between i and j (inclusive)
## for other random functions, refer to the API

def _flip_fair_coin(x):
    __dict = {'head':0,'tail':0}
    for i in range(0,x): 
        if(random.randint(0,1) == 0):
            __dict['head'] += 1
        else:
            __dict['tail'] += 1
    return __dict 

__start_time = time.time()
__dict_fCoin = _flip_fair_coin(toss_time)
__end_time = time.time()

__ratio_head = __dict_fCoin['head']/(__dict_fCoin['head'] + __dict_fCoin['tail'])
__ratio_tail = __dict_fCoin['tail']/(__dict_fCoin['head'] + __dict_fCoin['tail'])

print(f'ratio of head using a fair coin is {__ratio_head:.5%}')
print(f'ratio of tail using a fair coinis {__ratio_tail:.5%}')
print(f"execution time is {__end_time - __start_time}")


## random.random() without any argument will return a floating-point number greater
## than or equal to 0.0 but less than 1.0

def _toss_unfair_coin(x):
    __dict = {'head':0,'tail':0}
    for i in range(0,x):
        if(random.random() < 0.6):
            __dict['head'] += 1
        else:
            __dict['tail'] += 1
    return __dict

__start_time = time.time()
__dict_unFCoin = _toss_unfair_coin(toss_time)
__end_time = time.time()

__ratio_head = __dict_unFCoin['head']/(__dict_unFCoin['head'] + __dict_unFCoin['tail'])
__ratio_tail = __dict_unFCoin['tail']/(__dict_unFCoin['head'] + __dict_unFCoin['tail'])

print(f'ratio of head using an unfair coinis {__ratio_head:.5%}')
print(f'ratio of tail using an unfair coinis {__ratio_tail:.5%}')
print(f"execution time is {__end_time - __start_time}")

"""
1_000_000
ratio of head using a fair coin is 50.09370%
ratio of tail using a fair coinis 49.90630%
execution time is 1.6079387664794922
ratio of head using an unfair coinis 60.04300%
ratio of tail using an unfair coinis 39.95700%
execution time is 0.2918055057525635

1_000_000_000
ratio of head using a fair coin is 50.00224%
ratio of tail using a fair coinis 49.99776%
execution time is 1716.642420053482
ratio of head using an unfair coinis 59.99813%
ratio of tail using an unfair coinis 40.00187%
execution time is 317.77892804145813
"""
    
    
