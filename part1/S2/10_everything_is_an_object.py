# Everything is an Object

def desc_var(name, value):
    print(f"\033[1m{name}\033[0m")
    print(f"type: {type(value)}")
    print(f"value: {value}")
    print(f"address: {hex(id(value))}\n")

a = 10
desc_var('a', a)
# If int is a class, we should be able to declare it using standard class instatiation:

b = int(10)
desc_var('b', b)

# We can even request the class documentation:
# help(int)

# As we see from the docs, we can even create an int using an overloaded constructor:
b = int()
desc_var('b', b)

# As we see from the docs, we can even create an int using an overloaded constructor:
b = int('1000', base=2)
desc_var('b', b)

""" Functions are Objects too """

def square(a):
    return a ** 2

desc_var("square", square)

f = square
desc_var("f", f)
print(f is square)

print(square(2))
print(f(2))

# A function can return a function
def cube(a):
    return a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    return cube

print('-----------------------')

f = select_function(1)
print(f is square)
print(f(2))

f = select_function(2)
print(f is cube)
print(f(2))

# A Function can be passed as an argument to another function
print(select_function(2)(3))

print("---------------")

def exec_function(fn, n):
    return fn(n)

print(exec_function(cube, 3))
print(exec_function(square, 3))
