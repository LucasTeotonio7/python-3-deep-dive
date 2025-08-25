def func(a, b, *args):
    print(a, b, args)

func(1, 2, 'x', 'y', 'z')


# SyntaxError: positional argument follows keyword argument
# func(a=1, b=2, 'x', 'y', 'z')

def func(a, b=2, c=3, *args):
    print(a, b, c, args)

func(1, 6, 3,  'x', 'y', 'z')
func(1, c=5)

def func(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)

func(10, 20, 'y', 'z', 'a', c=7, d=19)

def func(a, b, *args, c=10, d=10, **kwargs):
    print(a, b, args, c, d, kwargs)

func(1, 2, 'x', 'y', 'z', c=100, d=200, x=0.1, y=0.2)

# help(print)
# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.

print(1, 2, 3)

print(1, 2, 3, sep='-', end=' *** ')
print(4, 5, 6, sep='-')


def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo) / 2
    if log_to_console:
        print(f"high: {hi}, low: {lo}, avg: {avg}")
    return avg

print(calc_hi_lo_avg(2, 9, 3, 10))

calc_hi_lo_avg(10, 20, 30, 17, 12, 8, 7, 12, log_to_console=True)
calc_hi_lo_avg(log_to_console=True)
print(calc_hi_lo_avg())
