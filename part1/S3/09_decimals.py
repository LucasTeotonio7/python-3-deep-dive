# Decimals
import decimal
from decimal import Decimal

print(Decimal(10))

# global context
g_ctx = decimal.getcontext()

print(g_ctx)
print(g_ctx.prec)
print(g_ctx.rounding)

g_ctx.prec = 6
print(g_ctx.prec)
print(g_ctx)
print(type(g_ctx))

g_ctx.rounding = decimal.ROUND_HALF_UP

print(decimal.getcontext())

g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN
print(decimal.getcontext())
print("\n")

print(decimal.localcontext())
print("-----------------")

"""
Local Context
The localcontext() function will return a context manager that we can use with a with statement:
"""

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print(decimal.getcontext())
    print(id(ctx) == id(decimal.getcontext()))

print(decimal.getcontext())
print("----------------")

# Rounding
x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1))
    print(round(y, 1))

print(round(x, 1))
print(round(y, 1))
