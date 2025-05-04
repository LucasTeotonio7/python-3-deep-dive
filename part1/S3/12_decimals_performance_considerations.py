"""
Decimals: Performance Considerations
Memory Footprint
Decimals take up a lot more memory than floats.
"""
from decimal import Decimal
import sys

a = 3.1415
b = Decimal("3.1415")

print(sys.getsizeof(a))
print(sys.getsizeof(b))

# create objects (in time)
import time

def run_float(n=1):
    for i in range(n):
        a = 3.1415

def run_decimal(n=1):
    for i in range(n):
        b = Decimal("3.1415")

n = 10000000 # ten million

# with float
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print(f"float: {end-start}s")

# with decimal
start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print(f"Decimal: {end-start}s")

# with math operations
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a

def run_decimal(n=1):
    b = Decimal("3.1415")
    for i in range(n):
        b + b

# with float
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print(f"float: {end-start}s")

# with decimal
start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print(f"Decimal: {end-start}s")


import math

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)

def run_decimal(n=1):
    b = Decimal("3.1415")
    for i in range(n):
        b.sqrt()

# with float
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print(f"float: {end-start}s")

# with decimal
start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print(f"Decimal: {end-start}s")
