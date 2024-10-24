print('\n \n')
print("===\t=== Welcome to Fork! a text adventure. ===\t===")
print('\ntype "help" at any time for help!\n')

def main():
    print("Choose Your Own Adventure")
    go_home()

def check_door():
        print("There is a man at the door... open?")
        # add options and stuff

def help():
    print("press enter after every choice to submit!")
    print('type "look" to look around')
    print('try "search" in some rooms to check for clues, or objects')
    print('type "help" at any time to see these options again!')

def go_home():
    print("You decide to go home...")
    print("But should you get some food?\n")
    print("pizza.")
    print("chinese.\n")
    choice = input()
    if choice == "pizza":
        get_pizza()
    elif choice == "chinese":
        get_chinese()

def get_pizza():
    print("\nyou got pizza")
    print("the pizza was yummy")
    print('\n*knock knock*... "but the delivery guy already came..."')
    print("\n check it out?")
    choice = input()
    if choice == "yes":
        check_door()
    elif choice == "no":
        dont_check()

   

def dont_check():
    print("you sit and enjoy your pizza, prentending noone is home.")
    print("\nwait.")
    print("\nwhat was that noise?")
    print("(open world start...)")
    choice = input()
    if choice == "look":
        print("You are in the living room.")
        print('there is a door to the hallway. type "hallway" to enter.')
        livingroom()
    elif choice == "search":
        print('the TV is on, the volume is low...\n the dry warmth of your home brings contrast to the bitter chill outside and the cold touch your windows breathe.')
        print('the blinds are closed and you feel qite secure dispite the noises in the house. likely because of the lock on your livingroom door being dead-bolt.')
        print('your fireplace displays its ability to warm your house. it crackles, the occasional pop of the pine being changed from structure to ash occours.')
        print('your pizza steams, the top of the box reads "Junimos"... ')
        print('not much else of note.\n')
        livingroom()
    elif choice == "help":
        help()
        print('\n \n \n')
        livingroom()
    elif choice =="hallway":
        hallway()
    elif choice =="pizza":
        eat_pizza()
        print('\n')


def get_chinese():
    print("\nyou got chinese")

def livingroom()
    print('you are in the livingroom\n')
    choice = input()
    if choice == "look":
        print("You are in the livingroom.")
        print('there is a door to the hallway. type "hallway" to enter.\n')
        livingroom()
    elif choice == "search":
        print('the TV is on, the volume is low...\n the dry warmth of your home brings contrast to the bitter chill outside and the cold touch your windows breathe.')
        print('the blinds are closed and you feel qite secure dispite the noises in the house. likely because of the lock on your livingroom door being dead-bolt.')
        print('your fireplace displays its ability to warm your house. it crackles, the occasional pop of the pine being changed from structure to ash occours.')
        print('your pizza steams, the top of the box reads "Junimos"... ')
        print('not much else of note.\n')
        livingroom()
    elif choice == "help":
        help()
        print('\n \n \n')
        livingroom()
    elif choice =="hallway":
        hallway()

def hallway():
    print('You are now in the hallway.')
    choice = input()
    if choice == "look":
        print('You are in the hallway. there is the door to the livingroom, \na doorway to the kitchen, \na door to the bathroom and a door to the bedroom.')
        print('type "livingroom" for the livingroom. \n"kitchen" for the kitchen \n"bathroom" for bathroom and "bedroom" for bedroom.')
    elif choice =="search":
        print('details about hallway.')
    elif choice == "help":
        help()
        print('\n \n \n')
        hallway()

def eat_pizza():
    print('You take a slice, the pizza is delicious! \nthe crust is coated in a buttery garlic sauce, the cheese is a golden brown and the sauce has a sweet, \nbut subtly spicy bite on the tip of your tongue...')
    livingroom()

main()









#tab in for content of the "if" statement
# choice = input("front or back?")
# if choice =="front";
#   front door code
# elif choice =="back";
#   back door code
# else;
#   print("i don't know what this is")
