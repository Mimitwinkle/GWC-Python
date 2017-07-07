x = input("Enter a number:")
y = input("Enter another number:")
def getBiggerNumber(x,y):

    if int(x) > int(y):
        print(int(x))
    if int(x) < int(y):
        print(int(y))

getBiggerNumber(x,y)
input("Press ENTER to exit.")
