l = [12, 10 , 7, 28, 14]

_max = lambda x, y: x if x > y else y
print(_max(3, 4))

def max_sequence(l: list):
    result = l[0]
    for x in l[1:]:
        result = _max(result, x)
    
    return result

print(max_sequence(l))

_min = lambda x, y: x if x < y else y

def min_sequence(l: list):
    result = l[0]
    for x in l[1:]:
        result = _min(result, x)
    
    return result

print(min_sequence(l))


_add = lambda x, y: x + y

def add_sequence(l: list):
    result = l[0]
    for x in l[1:]:
        result = _add(result, x)
    
    return result

print(add_sequence(l))
print("---------------")

from typing import Callable

def _reduce(fn: Callable[[int, int], int], l: list):
    result = l[0]
    for x in l[1:]:
        result = fn(result, x)

    return result

print(_reduce(_max, l))
print(_reduce(_min, l))
print(_reduce(_add, l))
print("---------------")

from functools import reduce

print(reduce(_max, l))
print(reduce(_min, l))
print(reduce(_add, l))
print("---------------")

print(reduce(_max, {1, 2, 4, 7}))
print(min(l))
print(max(l))
print(sum(l))
print(max((1, 3, 5)))
print("---------------")

print(all([0, None, 1, False]))
print(all([1, True, 1, "python"]))

print(any([0, None, 1, False]))
print(any([0, None, "", False]))
print("---------------")


print(reduce(lambda a, b: bool(a) and bool(b), {False, True, ""}))

l = [5, 8, 6, 10, 9]
print(reduce(lambda x, y: x * y, l))
print("---------------")

print(list(range(1, 5)))

print(reduce(lambda a, b: a * b, range(1, 5)))

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

print(fact(5))

import time
start = time.perf_counter()
fact(900)
end = time.perf_counter()
print(f"{end-start}s")

start = time.perf_counter()
reduce(lambda a, b: a * b, range(1, 901))
end = time.perf_counter()
print(f"{end-start}s")

import math

start = time.perf_counter()
math.factorial(900)
end = time.perf_counter()
print(f"{end-start}s")
print("---------------")


def _reduce(fn: Callable[[int, int], int], l: list, initial: int = 0):
    result = initial
    for x in l:
        result = fn(result, x)

    return result

print(l)
print(_reduce(lambda a, b: a + b, l, 0))
print(_reduce(lambda a, b: a + b, {}, 1))
print(_reduce(lambda a, b: a + b, {}))
print(reduce(lambda a, b: a + b, {}, 10))
