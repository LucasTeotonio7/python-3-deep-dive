"""Garbage Collection"""

import ctypes
import gc

"""
We use the same function that we used in the lesson on reference counting to 
calculate the number of references to a specified object (using its memory address to avoid creating an extra reference)
"""
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

"""We create a function that will search the objects in the GC for a 
specified id and tell us if the object was found or not:
"""
def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "object exists"
    return "object not found"

"""
Next we define two classes that we will use to create a circular reference
Class A's constructor will create an instance of class B and pass itself to class B's 
constructor that will then store that reference in some instance variable.
"""
class A:
    def __init__(self):
        self.b = B(self)

        hex_a = hex(id(self))
        hex_b = hex(id(self.b))
        print(f"A: self: {hex_a}, b: {hex_b}")

class B:
    def __init__(self, a):
        self.a = a

        hex_b = hex(id(self))
        hex_a = hex(id(self.a))
        print(f"B: self: {hex_b}, a: {hex_a}")

"""
We turn off the GC so we can see how reference counts are affected 
when the GC does not run and when it does (by running it manually).
"""
gc.disable()


"""
Now we create an instance of A, which will, in turn, create an instance of 
B which will store a reference to the calling A instance.
"""
my_var = A()

"""
As we can see A and B's constructors ran, and we also see from the memory addresses that we have a circular reference.
In fact my_var is also a reference to the same A instance:
"""
print(hex(id(my_var)))

# Another way to see this:
print(f"a: {hex(id(my_var))}")
print(f"a.b: {hex(id(my_var.b))}")
print(f"b.a: {hex(id(my_var.b.a))}")

a_id = id(my_var)
b_id = id(my_var.b)

# We can see how many references we have for a and b:
print(f"ref_count(a): {ref_count(a_id)}")
print(f"ref_count(b): {ref_count(b_id)}")
print(f"a: {object_by_id(a_id)}")
print(f"b: {object_by_id(b_id)} \n\n")

"""
As we can see the A instance has two references (one from my_var, the other from the instance variable b in the B instance)
The B instance has one reference (from the A instance variable a)
Now, let's remove the reference to the A instance that is being held by my_var:
"""
my_var = None

print(f"ref_count(a): {ref_count(a_id)}")
print(f"ref_count(b): {ref_count(b_id)}")
print(f"a: {object_by_id(a_id)}")
print(f"b: {object_by_id(b_id)} \n\n")

"""
As we can see, the reference counts are now both equal to 1 (a pure circular reference), 
and reference counting alone did not destroy the A and B instances - they're still around. 
If no garbage collection is performed this would result in a memory leak.
Let's run the GC manually and re-check whether the objects still exist:
"""
count = gc.collect()
print(count)

print(f"ref_count(a): {ref_count(a_id)}")
print(f"ref_count(b): {ref_count(b_id)}")
print(f"a: {object_by_id(a_id)}")
print(f"b: {object_by_id(b_id)}")
