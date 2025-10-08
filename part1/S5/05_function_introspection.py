# type: ignore

# dummy code
i=10

# TODO: fix this function
def my_func(
    a: "mandatory positional", 
    b: "optional positional" = 1, 
    c=2, 
    *args: "add extra positional here", 
    kw1, 
    kw2=100, 
    kw3=200, 
    **kwargs: "provide extra kw-only here"
) -> "does nothing":
    
    """ this function does anythings """
    i = 10
    j = 20
    return j + i

print(my_func.__doc__)
print(my_func.__annotations__)

my_func.short_description = "This is a function that does nothing much"

print(my_func.short_description)
print(dir(my_func))
print(my_func.__name__)

def fnc_call(f):
    print(f.__name__)

fnc_call(my_func)
fnc_call(lambda x: x+1)

print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print(dir(my_func.__code__))
print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)


# inspect module
import inspect
from inspect import isfunction, ismethod, isroutine

a = 10
print(isfunction(a))

print(isfunction(my_func))
print(ismethod(my_func))
print(isroutine(my_func))
print("\n")

class MyClass:
    def f(self):
        pass

print(isfunction(MyClass.f))
print(ismethod(MyClass.f))
print(isroutine(MyClass.f))
print("\n")

obj = MyClass()

print(isfunction(obj.f))
print(ismethod(obj.f))
print(isroutine(obj.f))

print(inspect.getsource(my_func))
print(inspect.getmodule(my_func))
print(inspect.getmodule(print))

import math
print(inspect.getmodule(math.sin))

print(inspect.getcomments(my_func))
print(inspect.getcomments(i))
print(inspect.signature(my_func))
print(dir(inspect.signature(my_func)))
print("\n")
print(my_func.__annotations__)
print(inspect.signature(my_func).return_annotation)

sig = inspect.signature(my_func)
print(sig.parameters)

for k, param, in sig.parameters.items():
    print(f"Key: {k}")
    print(f"Name: {param.name}")
    print(f"Defaults: {param.default}")
    print(f"Annotation: {param.annotation}")
    print(f"Kind: {param.kind}")
    print("--------------------------")

print(divmod(4, 3))
print(divmod(9, 3))

for param in inspect.signature(divmod).parameters.values():
    print(param.kind)

