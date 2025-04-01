"""
Integers - Operations
Addition, subtraction, multiplication and exponentiation of integers always result in an integer. 
(In the case of exponentiation this holds only for positive integer exponents.)
"""

print(-135//4)

import math
print(math.floor(3.14))
print(math.floor(1.9999999))
print(math.floor(2))
print(math.floor(-3.1))


print(type(2 + 3))
print(type(3 - 10))
print(type(3 * 7))
print(type(3 ** 4))

# But the standard division operator / always results in a float value:
print(type(2 / 3))
print(type(10 / 7))
a = 10/5
print(a)
print(type(a))

# The math.floor() method will return the floor of any number:
# For non-negative values (>= 0), the floor of the value is the same as the integer portion of the value (truncation)
print(math.floor(3.15))
print(math.floor(-3.15)) # -4
print(math.floor(-3.0000001)) # -4
print(math.floor(-3.0000000000000001)) # -3


import sys
print(sys.float_info)


"""
The Floor Division Operator
The floor division operator a//b is the floor of a / b

i.e. a // b = math.floor(a / b)

This is true whether a and b are positive or negative.
"""
a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))

"""For positive numbers, a//b is basically the same as truncating (taking the integer portion) of a / b.

But this is not the case for negative numbers."""
a = -33
b = 16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))
print("\n\n")
a = 33
b = -16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))
print("\n\n")

"""
The Modulo Operator
The modulo operator and the floor division operator will always satisfy the following equation:

a = b * (a // b) + a % b
"""
a = 13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

print("\n\n")
a = -13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

print("\n\n")
a = 13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

print("\n\n")
a = -13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)