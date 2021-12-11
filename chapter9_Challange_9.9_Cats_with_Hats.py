"""
You have 100 cats.
One day you decide to arrange all your cats in a giant circle. Initially,
none of your cats have any hats on. You walk around the circle 100
times, always starting at the same spot, with the first cat (cat # 1).
Every time you stop at a cat, you either put a hat on it if it doesn’t have
one on, or you take its hat off if it has one on.
1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you only stop at every second cat (#2, #4, #6,
#8, etc.).
3. The third round, you only stop at every third cat (#3, #6, #9, #12,
etc.).
4. You continue this process until you’ve made 100 rounds around
the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.
"""
import inspect
from timeit import default_timer as timer


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

start_time0 = timer()
_catTuple = tuple(range(1,101))
# myPrint(_catTuple)


#_hatList = [0]*100
# myPrint(_hatList)

_ans_dict = {}
for i in range(0,100):
    k = _catTuple[i]
    #v = _hatList[i]
    _ans_dict[k] = 0

time = 1
while time <= 100:
    for i in range(1,101):
        if i//time >= 1 and i%time  == 0:
            if _ans_dict[i] == 0:
                _ans_dict[i] = 1
            else:
                _ans_dict[i] = 0
    #print(f"this is the {time}th time, \n {_ans_dict}")
    time += 1
    
# myPrint(_ans_dict)

for k, v in _ans_dict.items():
    if _ans_dict[k]:
        print(f"Cat {k} has a hat.")
    else:
        print(f"Cat {k} is hatless!")

end_time0 = timer()

# method 2
start_time1 = timer()

theCats = {}

for i in range(1, 101):
    theCats[i] = False

for i in range(1, 101):
    for cats, hats in theCats.items():
        if cats % i == 0:
            if theCats[cats]:
                theCats[cats] = False
            else:
                theCats[cats] = True

for cats, hats in theCats.items():
    if theCats[cats]:
        print(f"Cat {cats} has a hat.")
    else:
        print(f"Cat {cats} is hatless!")

end_time1 = timer()
print(f"elapsed time0 is {end_time0 - start_time0} seconds")
print(f"elapsed time1 is {end_time1 - start_time1} seconds")

