from functools import partial

def my_func(a, b, c):
    print(a, b, c)

my_func(1, 2, 3)

def f(x, y):
    my_func(10, x, y)

f(20, 30)

f = lambda x, y: my_func(10, x, y)
f(200, 300)

f = partial(my_func, 10)
f(10, 20)


f = partial(my_func, 10, 20)
f(30)

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

my_func(10, 20, 100, 200, 300, 400, k1="a", k2="b", p="python")

def f(x, *vars, kw, **kwvars):
    my_func(10, x, *vars, k1="a", k2=kw, **kwvars)

f(500, 12, 13, 14, kw='pass', k4="d", p="python")

f = partial(my_func, 10, k1="777")
f(500, 12, 13, 14, k2='pass', k4="d", p="python")

def _pow(base, exponent):
    return base ** exponent

print(_pow(2, 3))

sq = partial(_pow, exponent=2)
print(sq(4))

cube = partial(_pow, exponent=3)
print(cube(3))

print(cube(base=3))

# overwrite partial ( warning !!! )
print(cube(base=3, exponent=2))

a = 2
sq = partial(_pow, exponent=a)

print(sq(5))
a = 3
print(sq(5))

def my_func(a, b):
    print(a, b)

a = [1, 2]

f = partial(my_func, a)

f(100)

a.append(3)
f(100)

origin = (0, 0)

l = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]

dist2 = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
print(dist2((1, 1), origin))

print(sorted(l))

f = partial(dist2, origin)
print(f((1, 1)))
print(sorted(l, key=f))

f = lambda x: dist2(x, origin)
print(sorted(l, key=f))
