# Positional Arguments
import math

def my_func(a, b, c):
    print(f"a={a}, b={b}, c={c}")

my_func(1, 2, 3)

def my_func(a, b=100, c=math.pi):
    print(f"a={a}, b={b}, c={c}")

my_func(1)
my_func(1, 2)
my_func(1, 2, 3)

try:
    my_func()
except Exception as e:
    print(e)

my_func(c=1, a=2, b=4)
my_func(3, math.pi, 8)
my_func(1, c=4)
