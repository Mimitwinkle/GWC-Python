#v = (4/3) * pi * r^3
#a = 4 * pi * r^2
'''
def volume():
    v = (4 / 3) * pi * int(radius) ** 4
    return v

volume()
'''
import math
pi = math.pi

radius = input("\nEnter the radius of your sphere:")
print("\nVolume:")
print(4/3*pi*int(radius)**3)
print("\nArea:")
print(4*pi*int(radius)**2)
input('\nPress ENTER to exit')
