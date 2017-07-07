import math

'''#Finds the corresponding number in the fibonacci sequence
fibonacci_numbers = [0, 1]
for i in range(2,100):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

num = input("Pick a number:")

print(fibonacci_numbers[int(num)])
'''
#Computes the factorial of a number

def factorial():
    num = input("\nPick a number:")
    fact=1
    if int(num) >= 1:
        for i in range(1,int(num)+1):
            fact=fact*i
        print(fact)

    elif int(num) <= 0:
        print("\nNumber must be positive.")
        factorial()

    else:
        print("\nThat is nonsense.")
        factorial()

factorial()
