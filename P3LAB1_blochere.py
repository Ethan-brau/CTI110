import time


#----------------------------------------------------------------------------

print('\n \n')
print('░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░\n ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░ \n ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n  ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n ')
print("===\t=== Welcome to Fork! a text adventure. ===\t===")
print('\ntype "help" at any time for help!\n')

def main():
    print("You stand in front of an old house.")
    choice = input()
    if choice == "look":
        print('you look at your surroundings.')
        time.sleep(1.5)
        print('you are in front of the house.')
        time.sleep(1.5)
        print('The steps up to the porch lead to the "front door".')
        print('you could search the "bushes", but you really dont want to. who knows what is hiding in there.')
        time.sleep(0.75)
        print('around the back is the "back door", it seems to be shut, but its hard to tell with the screen loosely protecting the porch from a clear view.')
        print('there is also a "shed" out back, locked behind a sturdy, and alarmingly new looking padlock.')
        print('your car sits behind you in the street, prectically begging you to "leave".')
        main()
    elif choice == "help":
        help()
        print('\n \n \n')
        main()
    elif choice == "search":
        time.sleep(1.5)
        print('behind you, your car ticks from the heat it is emitting gently in the sharp, cold air. you feel a desire to "leave".')
        print('you are facing the front of the house, it is old, probably late 50s townhome. the white paint is peeling, revealing how cruel the years have been.')
        print('the address on the porch support reads "6 * 2", it is impossible to read the second number as it has fallen off.')
        print('vines and other foiage grow up the sides of the building, tearing between the wooden slat siding, shattered windows reveal other flora life, \n reching towards the light of the moon.')
        print('the door is ajar, the scene all together sends a light chill down your spine. goosebumps set in.')
        main()
    elif choice == "leave":
        print('You head back to your car. the interior now a bit more chilly than when you left it.')
        print('the car door slams shut. you are ready to get out of here.')
        time.sleep(1.0)
        print('the car takes a minute to warm up, but after the heat is kicked in, you place your hand on the shifter and pull into drive. \n taking one last look at the house before you depart, you notice that the front door, once ajar \n is now closed. your heart beats a little faster.')
        time.sleep(0.8)

        go_home()
    elif choice == "front door":
        front_door()
    elif choice == "go to front door":
        front_door()
    elif choice == "back door":
        back_door()
    elif choice == "go to back door":
        back_door()
    elif choice == "shed":
        shed_door()
    elif choice == "go to shed":
        shed_door()
    elif choice == "bushes":
        bushes()
    elif choice == "go to bushes":
        bushes()
    else:
        print('I dont know what that is')

#----------------------------------------------------------------------------

def back_door():
    print('you are at the back door.')
    #add details and options

#----------------------------------------------------------------------------

def shed_door():
    print('you are at the door of the shed.')
    print('\n what is the passcode?')
    #add details and code choice

    #----------------------------------------------------------------------------

def bushes():
    print('you decide to search the bushes...')
    time.sleep(1.2)
    #add details and hint to passcode

#----------------------------------------------------------------------------

def check_door():
        print("There is a man at the door... open?")
        # add options and stuff

#----------------------------------------------------------------------------

def help():
    print("press enter after every choice to submit!")
    print('type "look" to look around')
    print('try "search" in some rooms to check for clues, or objects')
    print('some items, or locations in "quotation marks" are interactable. try entering them or "go to ____" to interact')
    print('type "help" at any time to see these options again!')

#-----------------------------------------------------------------------------

def go_home():
    print('You end up deciding to go home...')
    print('this is probably for the best.')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^')
    print('!77777777777777777777777777777?77???777~')
    print('!77?7777777777777777777777777777777??!7~')
    print('!77?77777777777777!7777!!!!!!!!!!777?77~')
    print('!77?7777777777777777777!!!!!!!!!!777?77~')
    print('!77?7777777777777777777!!~~~~~~~!777?!7~')
    print('!77?7777777777777777777!~~~~~~~~!777?!7~')
    print('!77?7777777777777777777!~~^^^^^^!777?!7~')
    print('!77?7777777777777777777!^^^^^^^^!777?77~')
    print('!77?7777777777777777777!^^^^^:^^!777?!7~')
    print('!77?7777777777777777777~::::::^^!777?77~')
    print('!77?7777777777777777777~:^^^^^^^!777?77~')
    print('!77?7777777777777777777!:^^^^^^^!777?!7~')
    print('!77?7777777777777!77777!^^^^^^^^!777?!7~')
    print('!77?7777777777777!77777!^^^^^^^^!777?!7~')
    print('!77?7777777777777!!7777!^^^^^^^^!777?77~')
    print('!77?7777777777777!!7777!^^^^^^^^!777?77~')
    print('!77?7777777777777!!7777!^^^^^^^^!777?77~')
    print('!77?7777777777777!!7777!^^^^^^^~7777?77~')
    print('!77?77777777777777!7777!^^^^~???YPP??77~')
    print('!77?7777777777777!!7777!^^^^^^^^!??7?77~')
    print('!77?7777777777777!!7777!^^^^^^^^!777?77~')
    print('!77?77777777777777!7777!^^^^^^^^!777?77~')
    print('!77?77777777777777!7777!^^^^^^^^!777?77~')
    print('!77?7777777777777!!7777!^^^^^^^^!777?77~')
    print('!77?77777777777777!7777!^^^^^^^^!777?77~')
    print('!77?7777777777777!!7777!^^^^^^^^!777?77~')
    print('!77?7777777777777!!7777!^^^^^^^~!777?77~')
    print('!77?7777777777777!77777!^^^^^^^~!777?77~')
    print('!77?7777!77777777!77777!^^^^^^~~!777?77~')
    print('!77?7777!77777777!!7777!^^~~~~~~!777?77~')
    print('!77?7777!77777777!77777!~~~~~~~~!777?!7~')
    print('!77?7777!77777777!!7777!~~~~~~~~!777?!7~')
    print('!77?7777777777777!77777!~~~~~~~~!777?!7~')
    print('!77?7777777777777!77777!~~~~~!!!7777?77~')
    print('!77J7777777777777!77777!!!!!!!!!7777?77~')
    print('!7!?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7?!7~')
    print('........................................')
    time.sleep(0.9)

    print('\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0:::::::::::::::::::::::::::::::::.')
    print('.^~~~^^^::777777777777777777777777777777777^')   
    print('.7???????????~..........................!77^')   
    print('.!?7777??????^\t\t\t\t \t ~77^')   
    print('.!?7!!!??????^\t\t\t\t \t ~77^')   
    print('.7?7!!!??????^\t\t\t\t \t ~77^')   
    print('.7?7~~~7?????^\t\t\t\t \t ~77^')   
    print('.!?7^~~7?????^\t\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t\t \t ~77^')   
    print('.!?!^^^7?????^\t\t\t\t \t ~77^') 
    print(':7J?!^^7?????^\t\t\t\t \t ~77^')   
    print('.~JYJ7~^7?????^\t\t\t\t \t ~77^')   
    print('.7?!^^~7?????^\t\t\t\t \t ~77^')   
    print('.7?7^^~7?????^\t\t\t\t \t ~77^')   
    print('.7?7^~~7?????^\t\t\t\t \t ~77^')   
    print('.7?7^~~7?????^\t\t\t\t \t ~77^')   
    print('.7?7~~~7?????^\t\t\t\t \t ~77^')   
    print('.7?7~~~7?????^\t\t\t\t \t ~77^')   
    print('.7?7~~~??????^\t\t\t\t \t ~77^')   
    print('.7?7~~~??????^\t\t\t\t \t ~77^')   
    print('.7?7~~~??????^\t\t\t\t \t ~77^')   
    print('.7?7~~~??????^\t\t\t\t \t ~77^')   
    print('.7?7~~!??????^\t\t\t\t \t ~77^')   
    print('.7?7!!!??????^\t\t\t\t \t ~77^')   
    print('.7?7!!7??????^\t\t\t\t \t ~77^')   
    print('.7???????77!!:\t\t\t\t \t ^~~:')   
    print('.~~~^::..\t\t\t\t \t \t .')                                

    print("But should you get some food?\n")
    print("pizza.")
    print("chinese.\n")
    choice = input()
    if choice == "pizza":
        get_pizza()
    elif choice == "chinese":
        get_chinese()
    else:
        print('I dont know what that is')

#------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------

def dont_check():
    print("you sit and enjoy your pizza, prentending noone is home.")
    print("\nwait.")
    print("\nwhat was that noise?")
    time.sleep(2.5)
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

#------------------------------------------------------------------------------------------

def get_chinese():
    print("\nyou decide to run and get chinese...")
    print('')
#------------------------------------------------------------------------------------------

def livingroom():
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

#------------------------------------------------------------------------------------------

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

#-------------------------------------------------------------------------

def front_door():
    print('You are now at the front door.')
    choice = input()
    if choice == "look":
        print('front door branch choices')
        print('ex.')
    elif choice =="search":
        print('details about front door.')
    elif choice == "help":
        help()
        print('\n \n \n')
        hallway()

main()









#tab in for content of the "if" statement
# choice = input("front or back?")
# if choice =="front":
#   front door code
# elif choice =="back":
#   back door code
# else:
#   print("i don't know what this is")
