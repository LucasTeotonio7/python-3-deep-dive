def func(**kwargs):
    print(kwargs)

func(a=1, b=2, c=3)

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(2, a=1, b=2, c=3)
func(2, {"a":1, "b":2})
func(2, **{"a":1, "b":2})


def func(*, d, **kwargs):
    print(d)
    print(kwargs)

func(d=1, x=100, y=200)

try:
    func(1, x=100, y=200)
except Exception as e:
    print(e)
