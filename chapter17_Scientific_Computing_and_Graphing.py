from Common import _section_str as sec, _segment_str as seg, myPrint as sysout

print(f"""
{sec}
Chapter 17 
Scientiрc Computing and Graphing
{sec}
""")

print(f"""
{sec}
17.1 Use Numpy for Matrix Manipulation
{sec}
""")

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for l in matrix:
    for e in l:
        print(e,end='\t')
    print()

print("another way to print")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end='\t')
    print()

print("if you want to double each element, if using list comprehension without []")

matrix_by2 = [y*2 for x in matrix for y in x]

print(matrix_by2)

print("if you want to double each element, if using list comprehension with []")
matrix_by2 = [ [y*2 for y in x] for x in matrix ]

for l in matrix_by2:
    for e in l:
        print(e,end='\t')
    print()

print("\nor you can use 2 for loops")
matrix_by2 = [[0 for i in range(len(matrix))]]*len(matrix)
print("initialize matrix_by2:")
for l in matrix_by2:
    for e in l:
        print(e,end='\t')
    print()


print("times 2:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix_by2[i][j] = matrix[i][j]*2

for l in matrix_by2:
    for e in l:
        print(e,end='\t')
    print()


# you cannot use [[]*3]*3 to initialize a matrixe,
# this is only repeating line 1 3 times.
matrix_by2 = [[0]*3,[0]*3,[0]*3]
print("initialize matrix_by2:")
for l in matrix_by2:
    for e in l:
        print(e,end='\t')
    print()


print("times 2:")

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix_by2[i][j] = matrix[i][j]*2

for l in matrix_by2:
    for e in l:
        print(e,end='\t')
    print()

print(f"""
{seg}
Test out
{seg}
""")

def _update_print(matrix_by3):
    matrix_by3[1][2] = 10
    matrix_by3[0][1] = 3

    for l in matrix_by3:
        for e in l:
            print(e,end='\t')
        print()
    print("end\n")

print(r"""
when dealing with matrix, how you initialize the matrix matters
here are some examples:
""")

matrix_by3 = [[0 for i in range(len(matrix))]]*len(matrix)
print(f"""
id(matrix_by3) is {id(matrix_by3) }
id(matrix_by3[0][0]) == id(matrix_by3[1][0]) is {id(matrix_by3[0][0]) == id(matrix_by3[1][0])}
id(matrix_by3[2][0]) == id(matrix_by3[1][0]) is {id(matrix_by3[2][0]) == id(matrix_by3[1][0]) }
""")

_update_print(matrix_by3)

matrix_by3 = [[0 for i in range(len(matrix))]]*3
print(f"""
id(matrix_by3) is {id(matrix_by3) }
id(matrix_by3[0][0]) == id(matrix_by3[1][0]) is {id(matrix_by3[0][0]) == id(matrix_by3[1][0])}
id(matrix_by3[2][0]) == id(matrix_by3[1][0]) is {id(matrix_by3[2][0]) == id(matrix_by3[1][0]) }
""")

_update_print(matrix_by3)

matrix_by3 = [[0]*3]*3
print(f"""
id(matrix_by3) is {id(matrix_by3) }
id(matrix_by3[0][0]) == id(matrix_by3[1][0]) is {id(matrix_by3[0][0]) == id(matrix_by3[1][0])}
id(matrix_by3[2][0]) == id(matrix_by3[1][0]) is {id(matrix_by3[2][0]) == id(matrix_by3[1][0]) }
""")

_update_print(matrix_by3)

matrix_by3 = [[0] *3, [0] *3,[0] *3]
print(f"""
id(matrix_by3) is {id(matrix_by3) }
id(matrix_by3[0][0]) == id(matrix_by3[1][0]) is {id(matrix_by3[0][0]) == id(matrix_by3[1][0])}
id(matrix_by3[2][0]) == id(matrix_by3[1][0]) is {id(matrix_by3[2][0]) == id(matrix_by3[1][0]) }
""")

_update_print(matrix_by3)


print(f"""
{seg}
17.1 Use Numpy for Matrix Manipulation
Install NumPy
Create a NumPy array
{seg}


Matrices in NumPy are instances of the ndarray object,
which stands for “n-dimensional array.”

An n-dimensional array is an array with n dimensions.
For example, a 1-dimensional array is a list.
A 2-dimensional array is a matrix.
Arrays can also have 3, 4, or more dimensions.
""")

import numpy as np
nparray_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
sysout(nparray_matrix)
print(f"nparray_matrix is \n{nparray_matrix}")
print(f"\nwhile matrix is \n{matrix}")

print(r"""
Accessing individual elements of the array works just like accessing
elements in a list of lists:
>>> ndarray_matrix[1][2]
6
You can optionally access elements with just a single set of square
brackets by separating the indices with a comma:
>>> ndarray_matrix[1,2]
6
""")

print(f"""
{seg}
what is the major difference between list and numpy.ndarray?
{seg}
NumPy arrays can only hold objects of the same type (for instance, all numbers)
whereas Pythons lists can hold mixed types of objects.

it is generally a good idea to handle your type conversion before initializing
an array object.
""")


print(f"""
{seg}
Array Operations
{seg}""")

print("multiply each element in a matrix by 2 ")

nparray_matrix_2 = nparray_matrix*2
print(f"nparray_matrix is \n{nparray_matrix}\n")
print(f"nparray_matrix_2 is \n{nparray_matrix_2}")



print("matrix product")
nparray_matrix_a = np.array([[1,2],[3,4],[5,6]])
nparray_matrix_b = np.array([[1,2,3],[4,5,6]])

nparray_matrix_ab = nparray_matrix_a@nparray_matrix_b
print(f"nparray_matrix_a.shape is {nparray_matrix_a.shape}\n")
print(f"nparray_matrix_b.shape is {nparray_matrix_b.shape}\n")
print(f"nparray_matrix_ab.shape is {nparray_matrix_ab.shape}\n")
print(f"nparray_matrix_ab is \n{nparray_matrix_ab}\n")
print(f"nparray_matrix_ab.diagonal() is \n{nparray_matrix_ab.diagonal()}\n")
print(f"nparray_matrix_ab.flatten() is \n{nparray_matrix_ab.flatten()}\n")
print(f"nparray_matrix_ab.transpose() is \n{nparray_matrix_ab.transpose()}\n")
print(f"nparray_matrix_ab.min() is {nparray_matrix_ab.min()}\n")
print(f"nparray_matrix_ab.max() is {nparray_matrix_ab.max()}\n")
print(f"nparray_matrix_ab.mean() is {nparray_matrix_ab.mean()}\n")
print(f"nparray_matrix_ab.sum() is {nparray_matrix_ab.sum()}\n")

print(f"""
{seg}
Stacking and Shaping Arrays
{seg}

Two arrays can be stacked vertically using np.vstack() or horizontally
using np.hstack() if their axis sizes match:
""")

nparray_vstack = np.vstack([nparray_matrix,nparray_matrix_ab])
nparray_hstack = np.hstack([nparray_matrix,nparray_matrix_ab])
nparray_matrix_a_reshape = nparray_matrix_a.reshape(2,3)
nparray_matrix_b_reshape = nparray_matrix_b.reshape(1,6)
print(f"""
nparray_matrix is
{nparray_matrix}

nparray_matrix_ab is
{nparray_matrix_ab}

nparray_vstack is
{nparray_vstack}

nparray_hstack is
{nparray_hstack}

you can also reshape a matrix using reshape(rowNum, colNum)

nparray_matrix_a is
{nparray_matrix_a}
nparray_matrix_a.shape is {nparray_matrix_a.shape}
nparray_matrix_a_reshape is
{nparray_matrix_a_reshape}
nparray_matrix_a_reshape.shape is {nparray_matrix_a_reshape.shape}

nparray_matrix_b is
{nparray_matrix_b}
nparray_matrix_b.shape is {nparray_matrix_b.shape}
nparray_matrix_b_reshape is
{nparray_matrix_b_reshape}
nparray_matrix_b_reshape.shape is {nparray_matrix_b_reshape.shape}
""")


print(f"""
{sec}
17.2 Use matplotlib for Plotting Graphs
{sec}

The plt.plot() function creates a plot, but it does not display anything.
The plot.show() function must be called to display the plot.
""")
print(r"""
check
>>> help(plt.plot)
or
http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.plot
for more detail

""")

imagePath="E:/pythonProject/PythonTutorials/chapter17_Plots"



from matplotlib import pyplot as plt

plt.plot([1,2,3,4,5],'bo')

print("""Instead of displaying the graph, you can save it.
The show() function pauses execution of your code and closing
the display window destroys the graph,
so trying to save the figure after calling show() results in an empty file.
""")
plt.savefig(imagePath+"/linear_1.png")
# close is for avoiding taking this one to the next plot
plt.close()
# plt.show()

print("[1,2,3,4,5] has been plotted.")

print("""
When two arguments are provided
to plt.plot(), the first list specifies the x-values and the second list
specifies the y-values:
""")
xs = [1,2,3,4,5]
ys = [2,4,6,8,10]
plt.plot(xs,ys,"go--")
# plt.show()

plt.savefig(imagePath+"/linear_2.png")
# close is for avoiding taking this one to the next plot
plt.close()



print("use Line2D")
from matplotlib.lines import Line2D 
fig = plt.figure()
ax = fig.add_subplot(111)
line = Line2D(xs, ys)
ax.add_line(line)
ax.set_xlim(min(xs), max(xs))
ax.set_ylim(min(ys), max(ys))

#plt.show()
plt.savefig(imagePath+"/linear_Line2D.png")
# close is for avoiding taking this one to the next plot
plt.close()


print("""
There is an optional “formatting” argument that can be inserted into
plot() after specifying the points to be plotted.
This argument specifies the color and style of lines or points to draw.
""")
xs = [1, 2, 3, 4, 5]
ys = [3, -1, 4, 0, 6]
plt.plot(xs, ys,"g-o")

#plt.show()
plt.savefig(imagePath+"/linear_g_o.png")
# close is for avoiding taking this one to the next plot
plt.close()


xs = [1, 2, 3, 4, 5]
ys = [3, -1, 4, 0, 6]
zs = [2,4,6,8,10]
plt.plot(xs,ys,zs,ys)
# plt.show()
plt.savefig(imagePath+"/xs_ys_zs_ys.png")
# close is for avoiding taking this one to the next plot
plt.close()

print(f"""
{seg}
Plot Multiple Graphs in the Same Window
{seg}
If you need to plot multiple graphs in the same window, you can do
so a few different ways.
1. You can pass multiple pairs of x- and y-value lists:
""")

xs = [0, 1, 2, 3, 4]
y1 = [1, 2, 3, 4, 5]
y2 = [1, 2, 4, 8, 16]
plt.plot(xs, y1, xs, y2)
# plt.show()
# print("default settings up plotted")
plt.savefig(imagePath+"/xs_y1_xs_y2.png.png")
# close is for avoiding taking this one to the next plot
plt.close()

plt.plot(xs, y1, "g-o", xs, y2, "b-^")

# plt.show()
plt.savefig(imagePath+"/xs_y1_g_o_xs_y2_b_caret.png")
# close is for avoiding taking this one to the next plot
plt.close()

print("format strings to plot, or you can use this as well")
plt.plot([1, 2, 3, 4, 5], "g-o")
plt.plot([1, 2, 4, 8, 16], "b-^")
#plt.show()
plt.savefig(imagePath+"/xs_y1_g_o_xs_y2_b_caret_2.png")
# close is for avoiding taking this one to the next plot
plt.close()

print(f"""
{seg}
Plot Data From NumPy Arrays
{seg}
""")

array = np.arange(1, 6)
print(array)
plt.plot(array)

# plt.show()
plt.savefig(imagePath+"/np_arange_1_6.png")
# close is for avoiding taking this one to the next plot
plt.close()

data = np.arange(1, 21).reshape(5, 4)
print(data)
plt.plot(data)
# plt.show()
plt.savefig(imagePath+"/np_arange_1_21_reshape_5_4.png")
# close is for avoiding taking this one to the next plot
plt.close()


print("transpose")
plt.plot(data.transpose())
# plt.show()
plt.savefig(imagePath+"/np_arange_1_21_reshape_5_4_transpose.png")
# close is for avoiding taking this one to the next plot
plt.close()

print(f"""
{seg}
Format Your Plots to Perfection
{seg}
""")

days = np.arange(0, 21)
other_site = np.arange(0, 21)
real_python = other_site ** 2
plt.plot(days, other_site)
plt.plot(days, real_python)
# plt.show()
plt.savefig(imagePath+"/realPython_0.png")
# close is for avoiding taking this one to the next plot
plt.close()

print("adding xticks")
plt.plot(days, other_site)
plt.plot(days, real_python)
plt.xticks([0, 5, 10, 15, 20])
#plt.show()
plt.savefig(imagePath+"/realPython_1_xticks.png")
# close is for avoiding taking this one to the next plot
plt.close()

print("adding labels and title")
plt.plot(days, other_site)
plt.plot(days, real_python)
plt.xticks([0, 5, 10, 15, 20])
plt.xlabel("Days of Reading")
plt.ylabel("Amount of Python Learned")
plt.title("Python Learned Reading Real Python vs Other Site")
# plt.show()
plt.savefig(imagePath+"/realPython_2_labels_title.png")
# close is for avoiding taking this one to the next plot
plt.close()

print("but which is which? adding legends to specify which is which")
plt.plot(days, other_site)
plt.plot(days, real_python)
plt.xticks([0, 5, 10, 15, 20])
plt.xlabel("Days of Reading")
plt.ylabel("Amount of Python Learned")
plt.title("Python Learned Reading Real Python vs Other Site")
plt.legend(["Other Site", "Real Python"])
# plt.show()
plt.savefig(imagePath+"/realPython_3_legend.png")
# close is for avoiding taking this one to the next plot
plt.close()

print(f"""
Other types of plots
""")

print("bar plots")
xs = [1, 2, 3, 4, 5]
tops = [2, 4, 6, 8, 10]
plt.bar(xs, tops)
# plt.show()
plt.savefig(imagePath+"/bar_0.png")
# close is for avoiding taking this one to the next plot
plt.close()

nparray_xs = np.arange(1, 6)
nparray_tops = np.arange(2, 12, 2)
plt.bar(nparray_xs, nparray_tops)
# plt.show()
plt.savefig(imagePath+"/bar_xs_tops.png")
# close is for avoiding taking this one to the next plot
plt.close()

print(r"""
The bar() function is more flexible than it lets on. For example, the
first argument doesn’t need to be a list of numbers. It could be a list
of strings representing categories of data.
The names of the fruits are conveniently used as the tick labels along
the x-axis.
""")
fruits = {
"apples": 10,
"oranges": 16,
"bananas": 9,
"pears": 4,
}
plt.bar(fruits.keys(), fruits.values())
# plt.show()
plt.savefig(imagePath+"/bar_dict_fruits.png")
# close is for avoiding taking this one to the next plot
plt.close()


print("histogram")

from numpy import random
plt.hist(random.randn(10000), 20)
# plt.show()
plt.savefig(imagePath+"/histogram_0.png")
# close is for avoiding taking this one to the next plot
plt.close()

print(f"""
{seg}
Save Figures as Images
{seg}
To save your plot, use the plt.savefig() function. Pass the path to
where you would like to save your plot as a string.
""")

