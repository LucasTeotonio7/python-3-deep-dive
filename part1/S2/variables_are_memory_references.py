"""
Variables are Memory References
We can find the memory address that a variable references, by using the id() function.

The id() function returns the memory address of its argument as a base-10 integer.

We can use the function hex() to convert the base-10 number to base-16.
"""

my_var = 10
print('my_var = {0}'.format(my_var)) # my_var = 10
print('memory address of my_var (decimal): {0}'.format(id(my_var))) # memory address of my_var (decimal): 140057347785232
print('memory address of my_var (hex): {0}'.format(hex(id(my_var)))) # memory address of my_var (hex): 0x7f61a4768210

greeting = 'hello'
print(greeting)
print(id(greeting))
print(hex(id(greeting)))
