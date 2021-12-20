# Common.py
# this Module includes all common functions or variables
# common functions include myPrint
# common variables include _section_str =*, and _segment_str -* 
# used for other python scripts.


_section_str = "================================================================================"
_segment_str = "--------------------------------------------------------------------------------"


import inspect
import copy

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
    print(f"variable {names[0]}:\n{t}.")
    print()

from Common import myPrint as sysout

data_list = [13,44,55,66,78,12,33,22,1,2,34]

def _sort_(l):
    ans = []
    while l:
        minimum = l[0]
        for x in l:
            if x < minimum:
                minimum = x
        ans.append(minimum)
        l.remove(minimum)
    return ans

ans = _sort_(data_list)
sysout(ans)


data_list = [13,44,55,66,78,12,33,22,1,2,34]
# O(n^2)
def _bubleSort_(l):
    ans = copy.deepcopy(l)
    for i in range(len(ans)):
        for j in range(i,len(ans)):
            if ans[i] > ans[j]:
                temp = ans[i]
                ans[i] = ans[j]
                ans[j] = temp
    return ans
    
ans = _bubleSort_(data_list)
sysout(data_list)
sysout(ans)    

# O(n^2)
def _insertionSort_(l):
    ans = copy.deepcopy(l)
    for i in range(1,len(ans)):
        key = ans[i]
        j = i-1
        while (j >= 0 and ans[j] > key):
            ans[j+1] = ans[j]
            j = j-1
        ans[j+1] = key
    return ans

ans = _insertionSort_(data_list)
sysout(data_list)
sysout(ans)


