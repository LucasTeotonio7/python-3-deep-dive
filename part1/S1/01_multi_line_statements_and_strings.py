a = [1, 2, 3]

a = [1, 2,
     3, 4, 5]

a = [1, #item 1
     2, #item 2
     3, #item 3
]

print(a)


a = (1, # comment
     2, # comment
     3)

print(a)

a = {
    "key1": 1, #value key 1
    "key2": 2, #value key 2
}

print(a)

def my_func(
    a, #this comment used to indicate that...
    b,
    c
):
    print(a, b, c)

my_func(7,19,43)

my_func(12,
        41,
        69)

a = 10
b = 20
c = 30

if a > 5 \
    and b > 10 \
        and c > 20:
    print("yes")


a = '''this is a string'''

print(a)

a = '''this 
is a string'''

print(a)

a = '''this 
        is a string
            that is created over multiple lines'''

print(a)

a = '''Some items:
    1. item 1
    2. item 2'''

print(a)

def my_func():
    a = '''a multi-line string
    that is actually indented in the second line'''
    return a

print(my_func())

def my_func():
    a = '''a multi-line string
that is not indented in the second line'''
    return a

print(my_func())
