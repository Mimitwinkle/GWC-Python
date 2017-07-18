sugarCookiesDict = {'Flour': '3 Cups', 'Baking Powder': '3/4 tsp', 'Salt': '1/4 tsp', 'Butter': '1 Cup', 'Sugar': '1 Cup', 'Egg': '1, beaten', 'Milk': '1 TBS', 'Powdered Sugar': 'For rolling dough'}
directions = ['\nStep 1: Sift together flour, baking powder, and salt. Set aside.' '\nStep 2: Place butter and sugar in large bowl of electric stand mixer and beat until light in color.' '\nStep 3: Add egg and milk and beat to combine.' '\nStep 4: Put mixer on low speed, gradually add flour, and beat until mixture pulls away from the side of the bowl.' '\nStep 5: Divide the dough in half, wrap in waxed paper, and refrigerate for 2 hours.' '\nStep 6: Preheat oven to 375 degrees F.' '\nStep 7: Sprinkle surface where you will roll out dough with powdered sugar.' '\nStep 8: Remove dough from refrigerator, sprinkle rolling pin with powdered sugar, and roll out dough to 1/4-inch thick.' '\nStep 9: Cut into desired shape, place at least 1-inch apart on greased baking sheet, parchment, or silicone baking mat, and bake for 7 to 9 minutes or until cookies are just beginning to turn brown around the edges, rotating cookie sheet halfway through baking time.']


def sugarCookies():
    print('\nSugar Cookies\n')

    for y in sugarCookiesDict:
        print (y,':',sugarCookiesDict[y])

    print(directions[len(directions)-1])


browniesdict = {'Soft butter': 'For greasing the pan', 'Flour': 'for dusting the buttered pan', 'Large eggs': '4', 'Sugar': '1 cup', 'Brown sugar': '1 cup', 'Melted butter': '8 ounces', 'Cocoa': '11/4 cups', 'Vanilla extract': '2 tsp', 'Flour':'1/2 cup', 'Kosher salt': '1/2 tsp'}

directionsbrownies = ['\nStep 1: Preheat the oven to 300 degrees F. Butter and flour an 8-inch square pan.' '\nStep 2: In a mixer fitted with a whisk attachment, beat the eggs at medium speed until fluffy and light yellow.' '\nStep 3: Add both sugars. Add remaining ingredients, and mix to combine. ' '\nStep 4: Pour the batter into a greased and floured 8-inch square pan and bake for 45 minutes. ' '\nStep 5: Check for doneness with the tried-and-true toothpick method: a toothpick inserted into the center of the pan should come out clean. ' '\nStep 6: When its done, remove to a rack to cool. Resist the temptation to cut into it until its mostly cool.']

def CocoaBrownies():
    print('\nCocoa Brownies\n')

    for y in browniesdict:
        print (y,':',browniesdict[y])

    print(directionsbrownies[len(directionsbrownies)-1])

CCCDict = {'Butter': '2/3 Cup', 'Sugar': '3/4 Cup', 'Brown Sugar': '1/4 Cup', 'Eggs': '1', 'Vanilla': '1 tsp', 'Flour': '1 3/4 Cups', 'Baking Soda': '1/2 tsp', 'Baking Soda': '1/2 tsp', 'Salt': '1/2 tsp', 'Chocolate Chips': '6-Ounces'}

CCCDirections = ['\nStep 1: Preheat the oven to 350 degrees F, positioning one of the oven racks in the middle of the oven.' '\nStep 2: Using an electric mixer, beat together the butter, granulated sugar, brown sugar, egg and vanilla on medium speed until smooth.' '\nStep 3: In a separate bowl, sift together the flour, baking soda and salt. Turn the electric mixer to low and slowly add the dry mixture to the wet mixture. Stir in the chocolate chips.' '\nStep 4: With a 1-ounce ice cream scoop, drop the batter about 2 inches apart on ungreased cookie sheets. Bake until lightly browned, 8 to 10 minutes.' '\nStep 5: Carefully remove the cookies to a wire rack to cool. Store in an airtight container.']

def ChocolateChipCookies():
    print('\nChocolate Chip Cookies\n')

    for y in CCCDict:
        print (y,':',CCCDict[y])

    print(CCCDirections[len(CCCDirections)-1])


yesno = input('Search for an ingredient?')
if yesno == "yes":
    ingredient = input('Are you in the mood for chocolate?')
    if ingredient == "yes":
        recipe = input("Do you want cocoa brownies or chocolate chip cookies?")
if yesno == "no":
    recipe = input("Pick your recipe:\nSugar Cookies\nCocoa Brownies\nChocolate Chip Cookies\n")


if recipe == "sugar cookies":
    sugarCookies()
if recipe == "cocoa brownies":
    CocoaBrownies()
if recipe == "chocolate chip cookies":
    ChocolateChipCookies()
