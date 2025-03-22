"""
Variable Equality
From the previous lecture we know that a and b will have a shared reference:
"""
def desc_var(name, value):
    print(f"\033[1m{name}\033[0m")
    print(f"type: {type(value)}")
    print(f"value: {value}")
    print(f"address: {hex(id(value))}\n")

def compare_vars(a, b):
    desc_var("a", a)
    desc_var("b", b)
    print(f"a is b: {a is b}")
    print(f"a == b: {a == b}\n")

a = 10
b = 10

compare_vars(a, b)

a = 500
desc_var("a", a)

b = 500
desc_var("b", b)

compare_vars(a, b)

# now, with lists

a = [1, 2, 3]
b = [1, 2, 3]

compare_vars(a, b)

# with numbers
a = 10
b = 10.0

compare_vars(a, b)

a = 10 + 0j
print(type(a))
compare_vars(a, b)

# None type
desc_var("None", None)

a = None
b = None
compare_vars(a, b)
