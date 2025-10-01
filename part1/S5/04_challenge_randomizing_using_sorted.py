import random

print(random.random())

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list[random.randint(0, len(list)-1)])

# shuffle
print(sorted(list, key=lambda x: random.random()))

# DESC
print(sorted(list, key=lambda x: x, reverse=True))