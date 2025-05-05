"""
Complex Numbers
Python's built-in class provides support for complex numbers.

Complex numbers are defined in rectangular coordinates (real and imaginary parts) using either the constructor or a literal expression.

The complex number 1 + 2j can be defined in either of these ways:
"""

a = complex(1, 2)
b = 1+ 2j
print(a == b)
print(type(a))
print(type(b))

# Note that the real and imaginary parts are defined as floats, and can be retrieved as follows:
print(a.real, type(a.real))
print(a.imag, type(b.imag))

# The complex conjugate can be calculated as follows:
print(a.conjugate())

#The standard arithmetic operatots are polymorphic and defined for complex numbers
a = 1 + 2j
b = 10 + 8j
print(a+b)
print(a*b)
print(a/b)
print(a-b)

# The // and % operators, although also polymorphic, are not defined for complex numbers:
try:
    print(a // b)
except Exception as e:
    print(e)

try:
    print(a % b)
except Exception as e:
    print(e)

try:
    print(divmod(a, b))
except Exception as e:
    print(e)

a = 0.1j
print(format(a.imag, ".25f"))
print(a + a + a == 0.3j)

import math

print(math.sqrt(2))
print(math.pi)

import cmath

print(cmath.pi)
print(type(cmath.pi))

a = 1 + 2j
try:
    print(math.sqrt(a))
except Exception as e:
    print(e)

print(cmath.sqrt(a))

"""
Polar / Rectangular Conversions
The cmath.phase() function can be used to return the phase (or argument) of any complex number.

The standard abs() function supports complex numbers and will return the magnitude (euclidean norm) of the complex number.
"""

a = 1 + 1j
print(cmath.phase(a))
print(cmath.pi / 4)
print(abs(a))
print(
    cmath.rect(math.sqrt(2), math.pi/4)
)

"""
Euler's Identity and the isclose() function
e^iπ + 1 = 0
"""
RHS = cmath.exp(complex(0, math.pi)) + 1
print(RHS)
print(cmath.isclose(RHS, 0))
print(cmath.isclose(RHS, 0, abs_tol=0.00001))
