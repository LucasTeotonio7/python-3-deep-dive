list_1 = [1, 8, 7, 9, 4, 2]
print(sorted(list_1))
print(list_1)
print(sorted("test with lambda 1"))

# letters (ascii)
print(ord('a'))
print(ord('A'))

print(sorted("aBbADcdC"))
print(sorted("aBbADcdC", key=lambda e: e.upper()))

d = {"def": 300, "abc": 100, "fff": 200}
print(sorted(d))
print(sorted(d, key=lambda e: d[e]))

def dist_sq(x):
    return f"{x} : [{(x.real) ** 2 + (x.imag) ** 2}]"

print(dist_sq(6))
print(dist_sq(1+1j))
print(dist_sq(5+9j))
print(dist_sq(3+4j))

list_2 = [1+1j, 5+9j, 3+4j]
# print(sorted(list_2)) -- TypeError: '<' not supported between instances of 'complex' and 'complex'
print(sorted(list_2, key=dist_sq))
print(sorted(list_2, key=lambda x: (x.real) ** 2 + (x.imag) ** 2))

# list strings
list_3 = ["banana", "apple", "pineapple", "orange", "lemon", "papaya"]
print(sorted(list_3))
# Ordered by last letter
print(sorted(list_3, key=lambda e: e[-1]))
list_3 = ["banana", "orange", "apple", "pineapple", "lemon", "papaya"]
print(sorted(list_3, key=lambda e: e[-1]))
