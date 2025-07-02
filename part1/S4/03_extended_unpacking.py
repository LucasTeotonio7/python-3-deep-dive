l = [1, 2, 3, 4, 5, 6]

a = l[0]
b = l[1:]

print(a)
print(b)

a, b = l[0], l[1:]

print(a)
print(b)

a, *b = l

print(a)
print(b)

s = {1,2,4}
try:
    s[0]
    s[1:]
except Exception as e:
    print(e)

s = "python"
a, *b = s

print(a)
print(b)

t = ('a', 'b', 'c')
a, *b = t

print(a)
print(b)

[a, b, c] = "XYZ"

print(a)
print(b)
print(c)

a, b, *c = "python"

print(a)
print(b)
print(c)

a, b, *c, d = "python"

print(a)
print(b)
print(c)
print(d)
print("------")

s = "python"
a, b, c, d = s[0], s[1], s[2:-1], s[-1]

print(a)
print(b)
print(c)
print(d)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
l2 = {"x","y","z"}
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
l2 = [3, 3, 6]
l = [*l1, *l2]
print(l)


s1 = {1, 2, 3}
s2 = {3, 4, 5}

try:
    s1 + s2
except Exception as e:
    print(e)

print(s1.union(s2))

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
print(s1.union(s2).union(s3).union(s4))
print(s1.union(s2, s3, s4))


d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 3}
print([*d1, *d2])

d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 3}

print({**d1, **d2})


# Nested Unpacking
# Python even supports nested unpacking:

a, b, (c, d) = [1, 2, ['X', 'Y']]
print(a)
print(b)
print(c)
print(d)

