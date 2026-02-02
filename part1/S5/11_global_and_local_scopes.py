a = 10

def my_func(n):
    c = n ** 2
    return c

def my_func(n):
    print(f"Global a: {a}")
    c = a ** n
    return c

result = my_func(2)
print(result)

a = 8
result = my_func(2)
print(result)

def my_func(n):
    global a
    a = 20
    print(f"Global a: {a}")
    c = a ** n
    return c

result = my_func(2)
print(result)

def my_func():
    global var
    var = 'hello world!'
    return

try:
    print(var)
except Exception as e:
    print(e)

my_func()
print(var)

a = 10
def my_func():
    global a
    a = 'Hello'
    print(f"Global a: {a}")

my_func()

a = 10
f = lambda n: print(a**n)
f(2)

for i in range(10):
    x = 2 * i

print(x)
