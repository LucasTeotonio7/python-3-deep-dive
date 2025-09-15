def add_item(name, quantity, unit, grocery_list):
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list

store1 = []
store2 = []

add_item("banana", 2, "units", store1)
add_item("milk", 1, "liter", store1)

print(store1)

add_item("python", 1, "medium-rare", store2)

print(store2)


def add_item(name, quantity, unit, grocery_list = []):
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list

del store1
del store2
print("\n ------------ ")

store1 = add_item("banana", 2, "units")
add_item("milk", 1, "liter", store1)

print(store1)

store2 = add_item("python", 1, "medium-rare")
print(store2)
print(store1)
print(store1 is store2)
print("\n ------------ ")

def add_item(name, quantity, unit, grocery_list = None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list

store1 = add_item("banana", 2, "units")
add_item("milk", 1, "liter", store1)

print(store1)

store2 = add_item("python", 1, "medium-rare")
print(store2)
print(store1 is store2)
print("\n ------------ ")

def factorial(n):
    print(f'Calculating {n}')
    return 1 if n < 1 else n * factorial(n-1)

print(factorial(4))
print(factorial(5))


cache = {}
def factorial(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f'Calculating {n}')
        result = n * factorial(n-1, cache=cache)
        cache[n] = result
        return result

print(factorial(3, cache=cache))
print(factorial(4, cache=cache))
print(factorial(4, cache=cache))
print(cache)
print(factorial(5, cache=cache))

def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f'Calculating {n}')
        result = n * factorial(n-1)
        cache[n] = result
        return result

print(factorial(3))
print(factorial(3))
print(factorial(4))