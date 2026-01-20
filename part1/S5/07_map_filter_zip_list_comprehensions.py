# map function

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

print(fact(3))
print(fact(5))

results = map(fact, range(6))

print(results)
for x in results:
    print(x)

print("-----------")

print(results)
for x in results:
    print(x)

print("-----------")
results = list(map(fact, range(6)))
print(results)
print("-----------")

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = [100, 200, 300, 400]

results = list(map(lambda x, y, z: x+y+z, l1, l2, l3))
print(results)
print("-----------")

results = map(lambda x, y: x+y, l1, l2, l3)
try:
    print(list(results))
    print("-----------")
except Exception as e:
    print(e)

# filter function
x = range(25)
print(list(x))
print("-----------")

results = filter(lambda num: num % 3 == 0, x)
print(list(results))

print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))
print("-----------")

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = "python"

# zip function
results = zip(l1, l2, l3)
print(list(results))
print(list(results))
print("-----------")

r = zip(range(10000), 'python')
print(list(r))

l = range(10)
print(list(l))

print(list(map(fact, l)))

results = [fact(n) for n in l]
print(results)

results = (fact(n) for n in l)
print(results)
print(map(fact, l))
print(list(results))
print(list(results))
print("-----------")

l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]

print(list(map(lambda x, y: x+y, l1, l2)))
print([x+y for x, y in zip(l1, l2)])

func1 = lambda x: x%2==0
func2 = lambda x, y: x+y
print(
    list(
        filter(func1, map(func2, l1, l2))
    )
)
l = [x + y for x, y in zip(l1, l2) if (x+y) % 2 == 0]
print(l)
