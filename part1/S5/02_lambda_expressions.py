def sq(x):
    return x**2

print(type(sq))
print(sq)

sq = lambda x: x**2

print(type(sq))
print(sq)
print(sq(2))

func_1 = lambda x, y: x + y
print(func_1(2, 4))

g = lambda x, y=10: x + y
print(g(3, 5))
print(g(0))

f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(f(1, 'k1', 'k2', 'kn', y=2, z=3, msg="test lambda"))

def cube(num):
    return num ** 3

def apply_func(x, fn):
    result = fn(x)
    print(f"{fn} ({type(fn)}): {result}")
    return result

apply_func(3, cube)
apply_func(3, lambda x: x ** 3)


def apply_func(fn, *args, **kwargs):
    result = fn(*args, **kwargs)
    print(f"{fn} ({type(fn)}): {result}")
    return result

apply_func(cube, 4)
apply_func(lambda x, y: x + y, 1, 2)
apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5)
apply_func(sum, (1, 2, 3, 4, 5))