def func1(a, b, c):
    print(a, b, c)

func1(1, 2, 3)
func1(1, c=3, b=2)
func1(c=3, b=2, a=1)

def func1(a, b, *args):
    print(a, b, args)

func1(1, 2, 3, 4, 5)

def func1(a, b, *args, d):
    print(a, b, args, d)

func1(1, 2, 3, 4, d=5)

def func1(*args, d):
    print(args, d)

func1(1, 2, 3, d=1)
func1(d=1)
try:
    func1(1)
except Exception as e:
    print(e)

# The best practice is to place *args and kwargs at the end of a function's parameter list.
def func1(d, *args):
    print(d, args)

func1(1)

# Sometimes we want only keyword arguments, in which case we still have to exhaust the positional arguments first 
# - but we can use the following syntax if we do not want any positional parameters passed in:
def func1(*, d=1):
    print(d)

func1()
func1(d=200)
try:
    func1(0)
except Exception as e:
    print(e)

def func1(a, b, *, d=1):
    print(a, b, d)

func1(1, 2)
func1(a=1, b=2, d=30)
try:
    func1(0, 1, 9)
except Exception as e:
    print(e)

