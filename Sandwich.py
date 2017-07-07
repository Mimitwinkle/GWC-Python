
def game():
    choice=input("You or your friend?")
    if choice == "me":
        wrong1()

    elif choice == "friend":
        wrong2()

    else:
        print("\nInvalid answer. Enter me or friend.")
        game()

def wrong1():
    print("\nYou make a sandwich for yourself.")
    sandwich = input("What sandwich would you like, pb&j or ham?")
    if sandwich == "pb&j":
        print("\nYou eat your sandwich, sad and alone.")
    elif sandwich == "ham":
        print("\nThe ham was bad. You die of food poisoning.")
    else:
        print("\nInvalid answer. Enter pb&j or ham.")
        wrong1()
def wrong2():
    print("\nYou make a sandwich for your friend.")
    fsandwich = input("What kind of sandwich, pb&j or ham?")
    if fsandwich == "pb&j":
        print("\nYou and your friend are friends for life.")
    elif fsandwich == "ham":
        print("\nYour friend hates ham and you!")
    else:
        print("\nInvalid answer. Enter pb&j or ham.")
        wrong2()

game()
replay=input("\nDo you want to play again?")
if replay == "yes":
    print("")
    game()
