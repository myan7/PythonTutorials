print(" Chapter 7 Finding and Fixing Code Bugs ")

print("=======================================================================")
print("7.1 Use the Debug Control Window ")

def __multiply_by_2(x):
    res = x*2
    return res

for i in range(1,4):
    j = __multiply_by_2(i)
    print(f"i is {i} and j is {j}")

## use right clike to set/clear breakpoint
## set break point at line 11
## go will take you the debug point or the end of the program
## step will step into the the function call.
## over will run over function
    

print("=======================================================================")
print("7.2 Squash Some Bugs ")

def __add_undScore(word):
    res = "_"
    for i in range(0,len(word)):
        res += word[i] + "_"
    return res

print(__add_undScore("Ming"))

## play with it, you will see some trend and understand how to use debugger
## alternative way to find out the error in your code is to output
## in the console step by step, which will also help you see what is going on.

## The process of re-writing existing code to be cleaner, easier to read
## understand, or adhere to code standards set by a team is called
## refactoring.

def __add_undScore(word):
    res = "_"
    for c in word:
        res += c + "_"
    return res

print(__add_undScore("Ming"))


## practice makes perfect.
