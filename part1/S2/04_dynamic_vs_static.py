"""
Dynamic Typing
Python is dynamically typed.

This means that the type of a variable is simply the type of the object the variable name points to (references). The variable itself has no associated type.
"""
a = "hello"
print(type(a))

a = 10
print(type(a))

a = lambda x: x**2
print(type(a))

"""
As you can see from the above examples, the type of the variable a changed over time - 
in fact it was simply the type of the object a was referencing at that time. No type was ever attached to the variable name itself.
"""
