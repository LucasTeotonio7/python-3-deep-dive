"""
Functions
Python has many built-in functions and methods we can use

Some are available by default:
"""
s = [1, 2, 3]
size = len(s)
print(size)

# While some need to be imported:
from math import sqrt
res = sqrt(4)
print(res)

import math
print(math.pi)
print(math.exp(1))


# We can define our own functions:
def func_1():
    print("running func_1")

func_1()

"""
Note that to "call" or "invoke" a function we need to use the ().
Simply using the function name without the () refers to the function, but does not call it:
"""
print(func_1)
# <function __main__.func_1>


"""
Note that a and b can be any type
But the function will fail to run if a and b are types that are not "compatible" with the ***** operator:
"""

def func_2(a, b):
    return a * b

res = func_2(3, 2)
print(res)

res = func_2('a', 3)
print(res)
#output: 'aaa'

res = func_2([1, 2, 3], 2)
print(res)

try:
    func_2('a', 'b')
except Exception as e:
    print(e)


# It is possible to use type annotations:
def func_3(a: int, b:int):
    return a * b

res = func_3(2, 3)
print(res)


"""
The def keyword is an executable piece of code that creates the function (an instance of the function class) and essentially assigns it to a variable name (the function name).
Note that the function is defined when def is reached, but the code inside it is not evaluated until the function is called.

This is why we can define functions that call other functions defined later - as long as we don't call them before all the necessary functions are defined.

For example, the following will work:
"""


def fn_1():
    fn_2()
    
def fn_2():
    print('Hello')

# it's ok, because fn_2 is define after the calling fn_1
fn_1()


def fn_3():
    fn_4()

# it is wrong, because the fn_4 does not exists (yet)
try:
    fn_3()
except Exception as e:
    print(e)

def fn_4():
    print('Hello')


print(type(fn_4))

"""
We also have the lambda keyword, that also creates a new function, 
but does not assign it to any specific name - instead it just returns the function object - 
which we can, if we wish, assign to a variable ourselves:
"""

func_5 = lambda x, y: x**y
print(func_5)
print(func_5(4, 3))
