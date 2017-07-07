start = input("What is the starting number?")
end = input("\nWhat is the ending number?")

list = []


def numgen(start, end):
    list = []
    for i in range(int(start), int(end)):
        list.append(i+1)

    print(list)

numgen(start, end)
input("Press ENTER to exit.")


'''
while true:
    list.append(int(start)+1)

print(list)
'''
