"""
Coercing Floats to Integers
Truncation
"""
from math import trunc

print(trunc(10.1))
print(trunc(10.5))
print(trunc(10.9))
print(trunc(10.9))
print(trunc(10.9999))

# The int constructor uses truncation when a float is passed in:
print(int(10.001))
print(int(10.1))
print(int(10.4))
print(int(10.49))
print(int(10.5))
print(int(10.9))
print(int(10.9999))
print("\n")

# Floor
from math import floor
print(floor(10.1))
print(floor(10.5))
print(floor(10.9))
print(floor(10.9))
print(floor(10.9999))

print(trunc(-10.9))
print(trunc(-10.3))
print(trunc(-10.1))

print(floor(-10.9))
print(floor(-10.3))
print(floor(-10.1))

# Ceiling
from math import ceil
print(ceil(10.1))
print(ceil(10.5))
print(ceil(10.9))
print(ceil(10.9))
print(ceil(10.9999))

print(ceil(-10.9))
print(ceil(-10.3))
print(ceil(-10.1))
