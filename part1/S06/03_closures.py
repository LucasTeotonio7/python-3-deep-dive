def outer():
    x = "python"
    def inner():
        print(x)
    return inner

fn = outer()
fn()

print(fn.__code__.co_freevars)
print(fn.__closure__)

def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        y = x
        print(hex(id(y)))
    return inner

fn = outer()
fn()

def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(fn())
print(fn.__closure__)


def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2

fn1, fn2 = outer()
print(fn1.__code__.co_freevars)
print(fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)

print(fn1())
print(fn2())
print(fn1())
print(fn2())

def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(2)
print(square.__closure__)
print(square(5))

cube = pow(3)
print(cube.__closure__)
print(cube(5))


def adder(n):
    def inner(x):
        return x + n
    return inner

adder_1 =  adder(1)
result = adder_1(1)
print(id(result))
print(id(2))
print(adder_1(2))

adder_2 =  adder(2)
adder_3 =  adder(3)

print(adder_1.__closure__)
print(adder_2.__closure__)
print(adder_3.__closure__)

print(adder_1(10))
print(adder_2(10))
print(adder_3(10))

adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)


print(adders)
print(adders[0].__closure__)
print(adders[0](10))

def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders

adders = create_adders()
print(adders[0](10))
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)

def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x, y=n: x + y)
    return adders

adders = create_adders()
print(adders)

print(adders[0].__closure__)
print(adders[0](10))
print(adders[0](10, 5))

