"""
Object Mutability
Certain Python built-in object types (aka data types) are mutable.

That is, the internal contents (state) of the object in memory can be modified.
"""

# immutable objects (numbers, strings, tuples, frozen sets, user-defined classes)
a = 10
print(id(a)) # id of a: 11758280

# assign a new value, the object 'a' points to other address
a = 20
print(id(a)) # id of a: 11758600

# mutable objects (lists, sets, dictionaries
my_list = [1, 2, 3]
print(my_list) # [1, 2, 3]
print(hex(id(my_list))) # 0x1cf6ab5b208

my_list.append(4)
print(my_list) # [1, 2, 3, 4]
print(hex(id(my_list))) # 0x1cf6ab5b208

"""
As you can see, the memory address of my_list has not changed.
But, the contents of my_list has changed from [1, 2, 3] to [1, 2, 3, 4].
On the other hand, consider this:
"""
my_list_1 = [1, 2, 3]
print(my_list_1)
print(hex(id(my_list_1)))

my_list_1 = my_list_1 + [4]
print(my_list_1)
print(hex(id(my_list_1)))

"""
Notice here that the memory address of my_list_1 did change.

This is because concatenating two lists objects my_list_1 and [4] did not modify the contents of 
my_list_1 - instead it created a new list object and re-assigned my_list_1 to reference this new object.

Similarly with dictionary objects that are also mutable types.
"""
my_dict = dict(key1='value 1')
print(my_dict)
print(hex(id(my_dict)))

my_dict['key1'] = 'modified value 1'
print(my_dict)
print(hex(id(my_dict)))

my_dict['key2'] = 'value 2'
print(my_dict)
print(hex(id(my_dict)))

"""
Once again we see that while we are modifying the contents of the dictionary, the memory address of my_dict has not changed.
Now consider the immutable sequence type: tuple
The tuple is immutable, so elements cannot be added, removed or replaced.
"""
t = (1, 2, 3)

print(f"Memory address of t: {hex(id(t))}")
print(f"Memory address of t[1]: {hex(id(t[0]))}")
print(f"Memory address of t[2]: {hex(id(t[1]))}")
print(f"Memory address of t[3]: {hex(id(t[2]))}")

"""
This tuple will never change at all. It has three elements, the integers 1, 2, and 3. 
This will remain the case as long as t's reference is not changed.
But, consider the following tuple:
"""
a = [1, 2]
b = [3, 4]
t = (a, b)
"""
Now, t is still immutable, i.e. it contains a reference to the object a and the object b.
That will never change as long as t's reference is not re-assigned.
However, the elements a and b are, themselves, mutable.
"""
a.append(3)
b.append(5)
print(t)
