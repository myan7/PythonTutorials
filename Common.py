# Common.py
# this Module includes all common functions or variables
# common functions include myPrint
# common variables include _section_str =*, and _segment_str -* 
# used for other python scripts.


_section_str = "================================================================================"
_segment_str = "--------------------------------------------------------------------------------"


import inspect

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
    #print(f"length of {names[0]} is {len(t)}.")
    print(f"variable {names[0]}: {t}.")
    print()
