"""
Decimals: Constructors and Contexts
The Decimal constructor can handle a variety of data types
"""

import decimal
from decimal import Decimal

class DebugDecimal(Decimal):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        print(repr(instance))
        return instance

# Integers
DebugDecimal(10)

# Strings
DebugDecimal('10.1')
DebugDecimal('-3.1415')

# Tuples
t = (0, (3,1,4,1,5), -4)
DebugDecimal(t)

# But don't use Floats
print(format(0.1, '.25f'))
DebugDecimal(0.1)
DebugDecimal('0.1')
print(Decimal('0.1') == Decimal(0.1))
print(Decimal('10') == Decimal(10))


"""
Context Precision and the Constructor
The context precision does nto affect the precision used when creating a Decimal object - those are independent of each other.
"""
print(decimal.getcontext())
# Let's set our global (default) context to a precision of 2
decimal.getcontext().prec = 2

# Now we can create decimal numbers of higher precision than that:
a = DebugDecimal('0.12345')
b = DebugDecimal('0.12345')
print(a+b)

decimal.getcontext().prec = 4
print(a+b)

# Local and Global Contexts are Independent
decimal.getcontext().prec = 6

a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print(f'c within local context: {c}')

print(f'c within global context: {c}')
