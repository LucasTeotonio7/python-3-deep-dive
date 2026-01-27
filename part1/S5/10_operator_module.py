import operator

class A:
    def __setattr__(self, name, value):
        print(value)
        super().__setattr__(name, value)

    def __getattr__(self, name):
        value = self.__dict__.get(name)
        print(value)
        return value

a = A()
a.sum = operator.add(1, 1)
a.mul = operator.mul(2, 3)
a.td = operator.truediv(3, 2)
a.floordiv = operator.floordiv(13, 2)
print(13 // 2)

from functools import reduce

a.ex1 = reduce(lambda x, y: x * y, [1, 2, 3, 4])
a.ex2 = reduce(operator.mul, [1, 2, 3, 4])

a.lt = operator.lt(10, 3)

from operator import is_
a.ex3 = is_('abc', 'def')
a.ex4 = is_('123', '123')
v1 = 10
v2 = v1
a.ex5 = is_(v1, v2)

a.truth1 = operator.truth([])
a.truth2 = operator.truth([1])
print("************************************")

my_list = [1, 2, 3, 4]
print(my_list[1])
print(operator.getitem(my_list, 1))

my_list[1] = 100
print(my_list)

del my_list[3]
print(my_list)

my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
print(my_list)

operator.delitem(my_list, 3)
print(my_list)

a.f = operator.itemgetter(2)
print(type(a.f))

my_list = [1, 2, 3, 4]
print(a.f(my_list))
print(a.f('python'))

a.f = operator.itemgetter(2, 3)
my_list = [1, 2, 3, 4]
print(a.f(my_list))
print(a.f('python'))

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    
    def test(self):
        print('test method running')

obj = MyClass()
print(obj.a)
print(obj.b)
print(obj.c)
obj.test()

prop_a = operator.attrgetter('a')
print(prop_a(obj))


my_var = 'b'
prot_b = operator.attrgetter(my_var)
print(prot_b(obj))
print(operator.attrgetter('a', 'b')(obj))

a, b, test = operator.attrgetter('a', 'b', 'test')(obj)
print(a)
print(b)
test()

f = lambda x: [x[2], x[3]]
x = [1, 2, 3, 4]
print(f(x))

a = 5 + 10j
print(a.real)

l = [5-10j, 3+3j, 2-100j]
f = lambda a: a.real
print(sorted(l, key=f))
print(sorted(l, key=operator.attrgetter('real')))

l = [(2, 3, 4), (1, 3, 5), (6, ), (4, 100)]
print(sorted(l, key=lambda x: x[0]))
print(sorted(l, key=operator.itemgetter(0)))
print(sorted(l, key=lambda x: sum(x)))

obj = MyClass()
f = operator.attrgetter('test')
f(obj)()

f = operator.methodcaller('test')
f(obj)

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def test(self, c):
        print(self.a, self.b, c)

obj = MyClass()
f = operator.methodcaller('test', 100)
f(obj)
