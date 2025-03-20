"""
Shared References and Mutability
The following sets up a shared reference between the variables my_var_1 and my_var_2
"""
a = 'hello'
b = a
print(a)
print(b)
print(id(a))
print(id(b))

a = 'hello'
b = 'hello'
# a and b have the same address in memory
print(id(a)) 
print(id(b))

b = "hello world" # the address in memory
print(id(a))
print(id(b))
print("\n")

# Now, we can use the shared reference with the mutable variables
a = [1, 2, 3]
b = a

# a and b have the same address in memory
print(id(a))
print(id(b))
print("\n")

b.append(100)
print(a)
print(b)
print(id(a))
print(id(b))
print("\n")

# now, in this case, a and b have the same address in memory
a = 10
b = 10
print(a)
print(b)
print(id(a))
print(id(b))
print("\n")

a = 500
b = 500
print(a)
print(b)
print(id(a))
print(id(b))
print("\n")
