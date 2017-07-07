from random import randint


list = []


for generator in range(1):
    a = randint(0,99)
    b = randint(0,99)
    if a + b == 99:
        list.append(a)
        list.append(b)
        print(a, "+", b, "== 99!")
    else:
        print(a, "+", b, "!= 99.")

'''
while True:
     do_something()
     if condition():
        break
'''
