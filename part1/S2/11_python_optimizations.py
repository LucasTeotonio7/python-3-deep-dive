"""
Python Optimizations: Interning
Earlier, we saw shared references being created automatically by Python:
[-5, 256]
"""

def desc_var(name, value):
    print(f"\033[1m{name}\033[0m")
    print(f"type: {type(value)}")
    print(f"value: {value}")
    print(f"address: {hex(id(value))}\n")

a = 10
b = 10

desc_var('a', a)
desc_var('b', b)

a = 500
b = 500

desc_var('a', a)
desc_var('b', b)
print(a is b)

a = 256
b = 256

desc_var('a', a)
desc_var('b', b)
print(a is b)

"""
do have the same reference.
This is called interning: Python interns the integers in the range [-5, 256].
The integers in the range [-5, 256] are essentially singleton objects.
"""

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)
desc_var('a', a)
desc_var('b', b)
desc_var('c', c)
desc_var('d', d)
