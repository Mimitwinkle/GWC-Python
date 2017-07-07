import random



#---- Haiku Generator ----
three1 = ["Falling leaves", "Summer sunshine", "Rainbow skies", "Blue waters", "Falling rain"]
five = ["Refrigerator", "Beautiful landscape", "A leisurely stroll"]
three2 = ["Leafless tree", "This is life", "Natural art", "Ants at work"]

input("Press ENTER to generate a haiku.\n")
print(random.choice(three1))
print(random.choice(five))
print(random.choice(three2))

'''
#---- Name Generator ----
first = ["Billy", "Pal", "John", "Bob"]
last = ["Sparkles", "Sunshine", "Lollopop"]

input("Press ENTER to generate a name.\n")
print(random.choice(first),random.choice(last))

'''

'''
#---- Another way to generate haikus ----
def h(list1, list2, list3):

    line1 = (random.choice(list1))
    line2 = (random.choice(list2))
    line3 = (random.choice(list3))

    #haiku = [line1,line2,line3]
    haiku = []
    haiku.append(line1)
    haiku.append(line2)
    haiku.append(line3)
    print(haiku)
h(three1, five, three2)
'''
