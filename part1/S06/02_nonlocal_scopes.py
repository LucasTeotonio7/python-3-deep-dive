def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()

outer_func()

def outer_func():
    x = 'hello'
    def inner_1():
        def inner_2():
            print(x)
        inner_2()
    inner_1()

outer_func()

def outer_func():
    x = 'hello'
    def inner():
        x = 'python'
        print(f"Inner: {x}")
    inner()
    print(f"outer: {x}")

outer_func()

def outer_func():
    x = 'hello'
    print(f"outer(before): {x}")
    def inner():
        nonlocal x
        x = 'python'
        print(f"Inner: {x}")
    inner()
    print(f"outer(after): {x}")

outer_func()

print("--------------")

def outer_func():
    x = 'hello'
    def inner_1():
        def inner_2():
            nonlocal x
            x = 'python'
        inner_2()
    inner_1()
    print(x)

outer_func()

def outer_func():
    x = "bola"
    def inner_1():
        nonlocal x
        x = "quadrado"
        def inner_2():
            nonlocal x
            x = 'triângulo'
        inner_2()
    inner_1()
    print(x)

outer_func()

print("--------------")
x = "python"
print(x)

def outer():
    x = "monty"

    def inner():
        nonlocal x
        x = "help"
    inner()
    print(x)

outer()
print(x)
