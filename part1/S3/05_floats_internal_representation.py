"""
Floats - Internal Representation
The float class can be used to represent real numbers.
"""

print(float(10))
print(float(10.4))
print(float("10.089"))

# However, strings that represent fractions cannot be converted to floats, unlike the Fraction class we saw earlier.
try:
    print(float("22/7"))
except Exception as e:
    print(e)

# If you really want to get a float from a string such as '22/7', you could first create a Fraction, then create a float from that:
from fractions import Fraction
a = Fraction("22/7")
print(float(a))

# Floats do not always have an exact representation:
print(0.1)

# Although this looks like 0.1 exactly, we need to reveal more digits after the decimal point to see what's going on:
print(format(0.1, '.15f'))
print(format(0.1, '.25f'))

# However, certain numbers can be represented exactly in a binary fraction expansion:
print(format(0.125, '.25f'))

a = 0.1 + 0.1 + 0.1
b = 0.3
print(a, b)
print(a == b)
