a, b, *c = 10, 20, 'a', 'b'

print(a)
print(b)
print(c)


def func1(a, b, *args):
    print(a)
    print(b)
    print(args)

func1(a, b, *c)

func1(2,3)
func1(2,1, ['python', 2])


def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count

print(avg(10, 20))
print(avg(10, 20, 50, 35, 15))
print(avg())


def avg(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return count and total/count

print(avg(10, 20))
print(avg(10, 20, 50, 35, 15))
try:
    print(avg())
except Exception as e:
    print(e)

def func1(a, b, c):
    print(a)
    print(b)
    print(c)

l = [1,2,3]
func1(*l)
print("\n\n")
def func1(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    for arg in args:
        print(arg)

l = [1,2,3,4,5,6]
func1(*l)
