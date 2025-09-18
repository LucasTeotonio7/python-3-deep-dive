# type: ignore
# help(print)
# help(int)

def my_func(a, b=1):
    """returns a * b
    Inputs:
        - a: int
        - b: int as default 1
    """
    return a * b

# help(my_func)

print(my_func.__doc__)

def my_func(
    a: 'annotation for a', 
    b: 'annotation for b'
) -> 'something':
    """documentation for my func"""
    return a * b

print(my_func.__doc__)
print(my_func.__annotations__)

x = 3
y = 5
def my_func(a: 'some character') -> 'character a repeated ' + str(max(x, y)) + " times":
    return a * max(x, y)

print(my_func('a'))
print(my_func.__annotations__)

def my_func(
    a: str,
    b: 'int > 0' = 1,
    *args: 'some extra positional args',
    k1: 'keyword-only arg 1',
    k2: 'keyword-only arg 2' = 100,
    **kwargs: 'some extra keyword-only args'
) -> 'something':
    print(a, b, args, k1, k2, kwargs)

# help(my_func)
print(my_func.__annotations__)
my_func(1,2,3,4,5, k1='a', k2='b', aj8='t', bh9=2+7j)
