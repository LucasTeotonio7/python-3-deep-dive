"""
Integers - Constructors and Bases
Constructors
The int class has two constructors
"""

print(int(10))
print(int(10.9))
print(int(-10))
print(int(-10.09999999))

print(int(True))
print(int(False))

import fractions

a = fractions.Fraction(22, 7)
print(a)
print(float(a))

# We can use the second constructor to generate integers (base 10) from strings in any base.
print(int("10"))
print(type(int("10")))
print(int("10292"))
print(int("101", 2))
print(int("1010", base=2))

print(int("FF", 16))
print(int("ff", 16))

print(int("A", 11))

# Base Representations
# Built-ins
print("\n")
print(bin(10))
print(oct(10))
print(hex(10))

#Note the 0b, 0o and 0x prefixes
# You can use these in your own strings as well, and they correspond to prefixes used in integer literals as well.
a = int('1010', 2)
b = int('0b1010', 2)
c = 0b1010

print(a, b, c)
print(a+b+c)

a = int('f1a', 16)
b = int('0xf1a', 16)
c = 0xf1a

print(a, b, c)

"""
Custom Rebasing
Python only provides built-in function to rebase to base 2, 8 and 16.
For other bases, you have to provide your own algorithm (or leverage some 3rd party library of your choice)
"""
def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # which is the same as:
        n, m = divmod(n, b)
        digits.insert(0, m)
    # print(digits)
    return digits

from_base10(10, 2)
from_base10(255, 16)

# Next we may want to encode the digits into strings using different characters for each digit in the base
def encode(digits, digit_map):
    # we require that digit_map has at least as many
    # characters as the max number in digits
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")
    
    # we'll see this later, but the following would be better:
    encoding = ''.join([digit_map[d] for d in digits])
    # print(encoding)
    return encoding

encode([15, 15], '0123456789ABCDEF')
encode([1, 10, 11], '0123456789AB')

# And we can combine both functions into a single one for easier use:
def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    # we store the sign of number and make it positive
    # we'll re-insert the sign at the end
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

e = rebase_from10(10, 2)
print(e)
print(int(e, 2))

e = rebase_from10(3451, 16)
print(e)
print(int(e, 16))

e = rebase_from10(-10, 2)
print(e)
print(int(e, 2))
