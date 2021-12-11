
##=======================================================================
print("=======================================================================")
print("6.1 Waht is a function, really? ")
## functions are values and can be assigned to a variable
## that means you can assign a value to the built-in function
## for example len = "Ming Yan" will prevent you from calling len("Ming Yan") in the following
## code. you can use del keyword.
## for normal attribute names,
## del will detach the name from the values, and delete the name.
## for built-in names, dict, len, pow
## del will only detach the name from the value, keep the name.




print("=======================================================================")
print("6.6 Understand Scope in Python ")

def __generate_power(exponent):
	def power(base):
		return base**exponent
	return power

raise_two = __generate_power(3)
print(raise_two(2))
print(raise_two(3))

## try running these following 2 lines to see what will happen.
## power(3)
## __generate_power(3)

## LEGB rule
"""
a useful way to remember how Python resolves scope is with the LEGB rule.
This rule is an acronym for Local, Enclosing, Global, Built-in
"""


## try running the follow commented lines
## total = 0
## def add_x_to_total(x):
##         total = total + x
##         return total
## print(f'total is {add_x_to_total(3)}')


total = 0
def add_x_to_total(x, total):
        total = total + x
        return total

print(f'total is {add_x_to_total(3,total)}')
print(f'total is {add_x_to_total(3,total)}')
print(f'total is {add_x_to_total(3,total)}')
## ask yourself
## why total is always 3? shouldn't it be added by 3 every time the function gets invoked?
## I hope you understand it.
## want to have a better understanding?
## https://realpython.com/inner-functions-what-are-they-good-for/

print(" or ")


total = add_x_to_total(3,total)
print(f'total is {add_x_to_total(3,total)}')
total = add_x_to_total(3,total)
print(f'total is {add_x_to_total(3,total)}')
total = add_x_to_total(3,total)
print(f'total is {add_x_to_total(3,total)}')

print(" or ")
def add_x_to_total2(x):
    total = 0
    total += x
    return total
total = add_x_to_total2(5)
print(f'total is {add_x_to_total(3,total)}')



print("=======================================================================")
print("6.7 Summary and Additional Resources ")


