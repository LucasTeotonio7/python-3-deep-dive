# NOTE: Conditionals


a = 5

if a < 5:
    print('a < 5')
else:
    print('a >= 5')


a = 15

if a < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a < 10')
    else:
        print('a >= 10')


a = 9
if a < 5:
    print('a < 5')
elif a < 10:
    print('5 <= a < 10')
else:
    print('a >= 10')


# NOTE: X if (condition is True) else Y

a = 5
res = 'a < 10' if a < 10 else 'a >= 10'
print(res)

