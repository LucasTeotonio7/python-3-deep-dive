# The For Loop

"""
This form of the for loop is simply a repetition, very similar to a while loop - 
in fact it is equivalent to what we could write in Python as follows:"""

i = 0
while i < 5:
    #code block
    print(i)
    i += 1
i = None

print("-----------")

"""
But that's NOT what the for statement does in Python - the for statement is a way to iterate over iterables, and has nothing to do with the for loop we just saw. 
The closest equivalent we have in Python is the while loop written as above.

To use the for loop in Python, we require an iterable object to work with.
A simple iterable object is generated via the range() function
"""
for i in range(5):
    print(i)

print("-----------")

# Many objects are iterable in Python:
for x in [1, 2, 3]:
    print(x)

print("-----------")

for x in "hello":
    print(x)

print("-----------")

for x in ('a', 'b', 'c'):
    print(x)

print("-----------")

# When we iterate over an iterable, each iteration returns the "next" value (or object) in the iterable:
for x in [(1,2), (3,4), (5,6)]:
    print(x)

print("-----------")

# We can even assign the individual tuple values to specific named variables:
for x,y in [(1,2), (3,4), (5,6)]:
    print("This is a first element of the tuple: {0}, and this a second: {1}".format(x,y))

print("-----------")

"""
We will cover iterables in a lot more detail later in this course.
The break and continue statements work just as well in for loops as they do in while loops:
"""
for i in range(5):
    if i == 3:
        continue
    print(i)

print("-----------")

for i in range(5):
    if i == 3:
        break
    print(i)

print("-----------")

"""
The for loop, like the while loop, also supports an else clause which is 
executed if and only if the loop terminates normally (i.e. did not exit because of a break statement)
"""
for i in range(1, 10):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 encountered')

# Similarly to the while loop, break and continue work just the same in the context of a try statement's finally clause.
for i in range(5):
    print('--------------------')
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always runs')
    print(i)

print("-----------")

# There are a number of standard techniques to iterate over iterables:
s = 'hello'
for c in s:
    print(c)

print("-----------")

# But sometimes, for indexable iterable types (e.g. sequences), we want to also know the index of the item in the loop:
s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1

print("-----------")

# Slightly better approach might be:
s = 'hello'
for i in range(len(s)):
    print(i, s[i])

print("-----------")

# or even better:
s = 'hello'
for i, c in enumerate(s):
    print(i, c)
