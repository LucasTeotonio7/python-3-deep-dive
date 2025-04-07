from fractions import Fraction

# help(Fraction)

# Use integers
def repr(object: object):
    print(object.__repr__())


repr(Fraction(1))
repr(Fraction(1, 1))
repr(Fraction(1, 2))

x = Fraction(2, 3)
y = Fraction(3, 4)
# 2/3 / 3/4 --> 2/3 * 4/3 --> 8/9
repr(x + y)
repr(Fraction(x, y))

repr(Fraction(0.125))

# Fractions are automatically reduced:
repr(Fraction(8, 16)) # -> 1/2

# Negative numbers
repr(Fraction(1, -4))
repr(Fraction(-1, 4))

x = Fraction(-1, 4)
print(x.numerator)
print(x.denominator)

# Using strings:
repr(Fraction('10.5'))
repr(Fraction('22/7'))

# Since floats have finite precision, any float can be converted to a rational number:
import math
x = Fraction(math.pi)
repr(x)
print(float(x))


x = Fraction(math.sqrt(2))
repr(x)
print(float(x))

a = 0.125
print(a)
b = 0.3
print(b)

repr(Fraction(a))
repr(Fraction(b))

print(format(b, '0.5f'))
print(format(b, '0.15f'))
print(format(b, '0.25f'))

x = Fraction(b)
print(x.limit_denominator(10))

x = Fraction(math.pi)
repr(x)
print(x)
print(x.limit_denominator(10))
print(x.limit_denominator(100))
print(x.limit_denominator(10000))