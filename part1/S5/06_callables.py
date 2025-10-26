print(callable(print))

result = print("Hello!")
print(result)

def my_func():
    pass

result = my_func()
print(result)
print(callable(my_func))

l = [1,2,3]
print(callable(l))
print(callable(l.append))

s = "my string"
print(callable(s))
print(callable(s.capitalize))

class MyClass:
    pass

object = MyClass()
print(object)
print(callable(object))
print(callable(object.__init__))
print(callable(MyClass))
print(type(MyClass))

