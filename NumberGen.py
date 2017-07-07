from random import randint


list = []

for g in range(1, 100):
    p = randint(10,99)
    if p % 5 == 0:
        list.append(p)
    elif p % 3 == 0:
        list.append(p)

print(list)
