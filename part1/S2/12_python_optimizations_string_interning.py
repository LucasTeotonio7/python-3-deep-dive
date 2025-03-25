"""
Python Optimizations: String Interning
Python will automatically intern certain strings.

In particular all the identifiers (variable names, function names, class names, etc) are interned (singleton objects created).
Python will also intern string literals that look like identifiers.

For example:
"""
a = 'hello'
b = 'hello'
print(id(a))
print(id(b))

# But not the following:

a = 'hello, world!'
b = 'hello, world!'
print(id(a))
print(id(b))

print(a == b)
print(a is b)

print("\n")

a = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
b = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
print(id(a))
print(id(b))

print("\n")

import sys

a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'
print(id(a))
print(id(b))
print(id(c))

print('a==b:', a==b)
print('a is b:', a is b)

print("\n")
"""
So, does interning really make a big speed difference?
Yes, but only if you are performing a lot of comparisons.
Let's run some quick and dirty benchmarks:
"""
def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass


import time

start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()

print('equality: ', end-start)

print("\n")
start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()

print('identity: ', end-start)
