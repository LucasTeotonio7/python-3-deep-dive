# Booleans: Precedence and Short-Circuiting
# Precedence order: not -> and -> or

print(True or True and False)
print(True or (True and False))
print((True or True) and False)

# Short-Circuiting
# True or Y -> True
# False and Y -> False

a = 10
b = 2

if a/b > 2:
    print('a is at least twice b')


# wrong way
try:
    a = 10
    b = 0

    if a/b > 2:
        print('a is at least twice b')
except Exception as e:
    print(e)

# correct form
a = 10
b = 0

if b and a/b > 2:
    print('a is at least twice b')

# Can also be useful to deal with null or empty strings in a database:
import string

a = 'c'
print(a in string.ascii_uppercase)
print(string.digits)
print(string.ascii_letters)

name = "Bob"
if name[0] in string.digits:
    print("Name cannot star with a digit.")

name = "1Bob"
if name[0] in string.digits:
    print("Name cannot star with a digit.")

name = ""
if name and name[0] in string.digits:
    print("Name cannot star with a digit.")
