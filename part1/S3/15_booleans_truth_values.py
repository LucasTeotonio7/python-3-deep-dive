"""
Booleans: Truth Values
All objects in Python have an associated truth value, or truthyness

We saw in a previous lecture that integers have an inherent truth value:
"""

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(100))

print(100 != 0)
print(bool(100))

# Python is actually calling 100.bool() and returning that:
print((100).__bool__())
print("\n")


# Sequence Types
# An empty sequence type object is Falsy, a non-empty one is truthy:
print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool('abc'))
print(bool(1j))
print(bool([]))
print("\n")

# Numeric Types
# Any non-zero numeric value is truthy. Any zero numeric value is falsy:
from fractions import Fraction
from decimal import Decimal
print(bool(10))
print(bool(1.5))
print(bool(Fraction(3, 4)))
print(bool(Decimal('10.5')))
print("\n")

print(bool([]))
print(bool(()))
print(bool(''))
print("\n")

a = {}
b = set()
print(a,b)

print(bool(a))
print(bool(b))

a = {"a": 1}
b = {1, 2, 3}
print(a,b)

print(bool(a))
print(bool(b))
print(bool(None))
print("\n")


"""
One Application of Truth Values
"""

a = [1, 2, 3]
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('a is None, or a is empty')

a = [1, 2, 3]
if a:
    print(a[0])
else:
    print('nothing to see here')

