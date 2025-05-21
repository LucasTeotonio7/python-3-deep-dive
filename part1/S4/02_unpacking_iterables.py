# Unpacking Iterables

a = (1, 2, 3)
print(type(a))

a = 1, 2, 3
print(type(a))
print(a)

a = (1)
print(type(a))
print(a)

a = ('a')
print(type(a))
print(a)

a = (1, )
print(type(a))
print(a)

a = 100, 
print(type(a))
print(a)

a = ()
print(type(a))
print(a)

# Unpacking

a, b, c = [1, 'a', 3.14]
print(a, b, c)

(a, b, c) = [1, 2, 3]
print(a, b, c)

(a, b) = (12, 23)
print(a, b)

a, b ,c = 10, 20, 30
print(a, b, c)

a, b = 10, 20
print(a, b)

c = (id(a), id(b))
print(c)

a, b = b, a
print(a, b)

c = (id(a), id(b))
print(c)

for i in 'string':
    print(i)

a, b, c ="xyz"
print(a, b, c)

s = {'s', 't', 'r', 'i', 'n', 'g'}
print(s)

for i in s:
    print(i)

d = {'a': 1, 'b': 2, 'c': 3}
for i in d:
    print(i)

for value in d.values():
    print(value)

a, b, c = d.values()
print(a, b, c)

for key, value in d.items():
    print(key, value)
