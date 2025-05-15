"""
Booleans: Boolean Operators
The way the Boolean operators and, or actually work is a littel different in Python:

or
X or Y: If X is falsy, returns Y, otherwise evaluates and returns X
"""
print('a' or [1,2])
print('' or [1,2])
print(None or [1,2])

print(1 or 1/0)

try:
    print(0 or 2/0)
except Exception as e:
    print(e)

s1 = None
s2 = ""
s3 = "abc"

s1 = s1 or 'n/a'
s2 = s2 or 'n/a'
s3 = s3 or 'n/a'
print(s1, s2, s3)

print([] or [0])

"""
and
X and Y: If X is falsy, returns X, otherwise evaluates and returns Y

Once again, note that the truth value of Y is never considered when evaluating and, and that Y is only evaluated if it needs to be returned (short-circuiting)
"""

print(None and 100)
print([] and [0])

a = 2
b = 4
print(a/b)

print(b and a/b)

a = 2
b = 0

print(b and a/b)

s1 = None
s2 = ""
s3 = "abc"

print(s1 and s1[0])
print(s2 and s2[0])
print(s3 and s3[0])

print((s1 and s1[0]) or 'n/a')
print((s2 and s2[0]) or 'n/a')
print((s3 and s3[0]) or 'n/a')

print(not False)
print(not True)
print(bool(""))
print(bool(None))
print(bool(" "))
print(bool("abc"))
