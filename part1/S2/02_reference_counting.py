"""
Reference Counting
Method that returns the reference count for a given variable's memory address:
"""

import sys

a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a))

# get reference count with ctypes
import ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

b = a
c = b
print(ref_count(id(a))) # the reference count is 3 here

c = 10
print(ref_count(id(a))) # the reference count is 2 beacause 'c' points to another value in memory
 
b = None
print(ref_count(id(a))) # the reference count is 1 beacause 'b' points to another value in memory

a_id = id(a)
print(a_id)
a = None

import time
time.sleep(60)
print(ref_count(a_id))
