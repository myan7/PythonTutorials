universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_stats(l):
    
    _list_of_students = []
    _list_of_tuition = []

    for e in l:
        _list_of_students.append(e[1])
        _list_of_tuition.append(e[2])

    return _list_of_students, _list_of_tuition
# yes, in python, you can return 2 objects, which will be saved in a tuple.

def __mean(l):
    return sum(l)/len(l)

def __median(l):
    l.sort()

    if(len(l)%2 == 1):
        return l[len(l)//2]
    else:
        return (l[len(l)//2] + l[len(l)//2+1])/2

_lists = enrollment_stats(universities)

##print(type(_lists))
##print(_lists)

print(f"""
Total number of students:  \t{sum(_lists[0])}
Totole number of tuitions: \t{sum(_lists[1])}
Student mean: \t{__mean(_lists[0]):.2f}
Student median:\t{__median(_lists[1]):.2f}
Tution mean: \t{__mean(_lists[0]):.2f}
Tution median: \t{__median(_lists[1]):.2f}
""")
