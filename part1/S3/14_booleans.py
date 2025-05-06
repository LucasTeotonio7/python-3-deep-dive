"""
Booleans
The bool class is used to represent boolean values.

The bool class inherits from the int class.
"""
print(issubclass(bool, int))  # True

print(type(True), id(True), int(True))
print(type(False), id(False), int(False))

print(3<4)
print(type(3 < 4))
print(id(3 < 4))

print((3 < 4) is True)
print((3 < 4) == True)

print(None is False)

print((1 == 2) == False)
print((1 == 2) is False)
print(1 == 2 == False) # False

print(1 + True)
print(100 * False)
print(True > False)
print((True + True + True) % 2)
print(-True)

print(bool(1))
print(bool(0))
print(int(True))
print(int(False))
print(bool(1.0))
print(bool(100))
print(bool(-2))
print(bool("Hello"))
