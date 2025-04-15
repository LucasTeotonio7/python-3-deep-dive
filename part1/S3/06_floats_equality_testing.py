"""
Floats - Equality Testing
Because not all real numbers have an exact float representation, equality testing can be tricky.
"""
x = 0.1
print(format(x, '.25f'))

x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y) # This is False because 0.1 and 0.3 do not have exact representations:

# 0.1 --> 0.1000000000000000055511151
# x --> 0.3000000000000000444089210
# y --> 0.2999999999999999888977698

# However, in some (limited) cases where all the numbers involved do have an exact representation, it will work:
x = 0.125 + 0.125 + 0.125
y = 0.375
print(x == y)

print('0.125 --> {0:.25f}'.format(0.125))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))

# One simple way to get around this is to round to a specific number of digits and then compare:
x = 0.1 + 0.1 + 0.1
y = 0.3
print(round(x, 5) == round(y, 5))

x = 1000.01
y = 1000.02
print(y/x)

x = 0.01
y = 0.02
print(y/x)

# We can also use a more flexible technique implemented by the isclose method in the math module
from math import isclose
x = 0.1 + 0.1 + 0.1
y = 0.3
print(isclose(x, y))
print(x == y)


x = 123456789.01
y = 123456789.02
print(isclose(x, y, rel_tol=0.01))

x = 0.01
y = 0.02
print(isclose(x, y, rel_tol=0.01))


print(isclose(x, y, rel_tol=0.01, abs_tol=0.01))


# In general, we can combine the use of both relative and absolute tolerances in this way:
x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print('x = y:', isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print('a = b:', isclose(a, b, abs_tol=0.0001, rel_tol=0.01))

print('x = y:', isclose(x, y, abs_tol=0.0001))
print('a = b:', isclose(a, b, abs_tol=0.0001))

print('x = y:', isclose(x, y, rel_tol=0.01))
print('a = b:', isclose(a, b, rel_tol=0.01))
