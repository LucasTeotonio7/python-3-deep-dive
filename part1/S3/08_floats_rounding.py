# round without ndigits return a int type
a = round(1.9)
print(a, type(a))

# round with ndigits return a float type
a = round(1.9, 0)
print(a, type(a))

# n > 0
print("n > 0")
print(round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0))

# n < 0
print("n < 0")
print(
    round(888.88, 1), round(888.88, 0), \
    round(888.88, -1), round(888.88, -2), \
    round(888.88, -3)
)

# Ties
print(round(1.25, 1))
print(round(1.35, 1))
print(round(1.34, 1))

# similarly with n negative.
print(round(-1.25, 1))
print(round(-1.35, 1))
print(round(15, -1))
print(round(25, -1))

# To do this type of rounding (to nearest 1) 
# we can add (for positive numbers) or subtract (for negative numbers) 0.5 
# and then truncate the resulting number.

def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))

print(round(1.5), _round(1.5))
print(round(2.5), _round(2.5))

print(round(-1.5), _round(-1.5))
print(round(-2.5), _round(-2.5))
