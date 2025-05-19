# Comparison Operators

print(0.1 is (3+4j))
print(3 is 3)
print([1,2] is [1,2])


print('a' in 'this is a test')
print(3 in [1,2,3])
print(3 not in [1,2,3])

print('key1' in {'key1': 1})
print(1 in {'key1': 1})

try:
    1 + 1j < 3 +4j
except Exception as e:
    print(e)

from decimal import Decimal
from fractions import Fraction

print(Decimal('0.1') == Fraction(1, 10))
print(4 == 4+4j)
print(4 == 4+0j)

# Ordering Comparisons
print(1 < 2 < 3)
print(1 < 2 and 2 < 3)

print(3 < 2 < 1/0)
print(3 < 2 and 2 < 1/0)

print(1 < 2 > -5)
print(1 < 2 > -5 == Decimal(-5.0))

import string

print('A' < 'a' and 'z' > 'Z')
print(string.ascii_letters)

print('A' < 'a' and 'z' > 'Z' in string.ascii_letters)

min = 0
max = 100
age = 34
print(min < age < max)
