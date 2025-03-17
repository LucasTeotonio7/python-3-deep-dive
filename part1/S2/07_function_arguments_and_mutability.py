"""
Function Arguments and Mutability
Consider a function that receives a string argument, and changes the argument in some way:
"""
def get_address(var):
    return hex(id(var))

def process(s):
    print(f"initial s # = {get_address(s)}")
    s = s + ' world'
    print(f"s after change # = {get_address(s)}")


my_var = 'hello'
print(f"my_var # = {get_address(my_var)}")

"""
Note that when s is received, it is referencing the same object as my_var.
After we "modify" s, s is pointing to a new memory address:
"""
process(my_var)

"""And our own variable my_var is still pointing to the original memory address:"""
print(f"my_var: '{my_var}' # = {get_address(my_var)}\n\n")

# Let's see how this works with mutable objects:
def modify_list(lst: list):
    print(f"initial lst # = {get_address(lst)}")
    lst.append(100)
    print(f"lst after change # = {get_address(lst)}")


my_list = [7, 6, 9]
print(f"my_list # = {get_address(my_list)}")
modify_list(my_list)
print(my_list)
print(f"my_list # = {get_address(my_list)}\n\n")

"""
As you can see, throughout all the code, the memory address referenced by my_list and items is always the same (shared) reference - 
we are simply modifying the contents (internal state) of the object at that memory address.

Now, even with immutable container objects we have to be careful, e.g. 
a tuple containing a list (the tuple is immutable, but the list element inside the tuple is mutable)
"""
def modify_tuple(t: tuple):
    print(f"initial t # = {get_address(t)}")
    t[0].append(100)
    print(f"t after change # = {get_address(t)}")

my_tuple = ([1, 2], 'a')
print(f"my_tuple # = {get_address(my_tuple)}")
modify_tuple(my_tuple)
print(my_tuple)
print(f"my_tuple # = {get_address(my_tuple)}\n\n")
