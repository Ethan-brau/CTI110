import time
import random

key_status_haunt = ('none')
key_status = ('none')
#----------------------------------------------------------------------------

print('\n \n')
print('░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░\n ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░ \n ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n  ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░\n ')
time.sleep(2.5)
print("===\t=== Welcome to Fork! a text adventure. ===\t===")
print('\ngame by Windyworks.\n')
print('\ntype "help" at any time for help!\n')

def main():
    print("You stand in front of an old house.")
    choice = input()
    if choice == "look":
        print('you look at your surroundings.')
        time.sleep(1.5)
        print('you are in front of the house.')
        print('\u00A0 \u00A0 \u00A0_|=|__________')
        print('\u00A0 \u00A0 /              \ ')
        print('\u00A0 \u00A0/                \ ')
        print('\u00A0 /__________________\ ')
        print('\u00A0 \u00A0||  || /--\ ||  ||')
        print('\u00A0 \u00A0||[]|| | .| ||[]||')
        print(' ()||__||_|__|_||__||()')
        print('( )|-|-|-|====|-|-|-|( )') 
        print('^^^^^^^^^^====^^^^^^^^^^^')
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
        print('the address on the porch support reads "6 - -", it is impossible to read the second or third numbers as they have fallen off.')
        print('vines and other foiage grow up the sides of the building, tearing between the wooden slat siding, shattered windows reveal other flora life, \n reching towards the light of the moon.')
        print('the door is ajar, the scene all together sends a light chill down your spine. goosebumps set in.')
        main()
    elif choice == "leave":
        print('You head back to your car. the interior now a bit more chilly than when you left it.')
        print('the car door slams shut. you are ready to get out of here.')
        time.sleep(1.0)
        print('the car takes a minute to warm up, but after the heat is kicked in, you place your hand on the shifter and pull into drive. \n taking one last look at the house before you depart, you notice that the front door, once ajar \n is now closed. your heart beats a little faster.')
        print('on the drive home, there is not much of note. pulling into your driveway, everything feels a little better.')
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
        main()

#----------------------------------------------------------------------------

def back_door():
    print('you are at the back door.')
    choice = input()
    if choice == "help":
        help()
        print('\n \n \n')
        back_door()
    elif choice == "look":
        print('at the back door, you could go back around to the "front" yard or go "inside"')
        back_door()
    elif choice == "search":
        print('the paint on the back porch is basically non-existent. vines and flora of all sort climb up the back of the house, the screen door is torn open, the door rotten. it seems like it is unlocked.')
        print('the smell of decayed wood fills the air of the back porch.\n')
        back_door()
    elif choice == "inside":
        dining_room_haunt()
    elif choice == "go inside":
        dining_room_haunt()
    else:
        print('I dont know what that is')
        back_door()
#----------------------------------------------------------------------------

def shed_door():
    print('you are at the door of the shed.')
    print('\n what is the passcode?')
    time.sleep(1.5)
    
    choice = input()
    if choice == "647":
        in_shed()
    elif choice == "I dont know":
        print('then figure it out.')
        shed_door()
    elif choice == "look":
        print('like the house, the paint is faded, and chipping. to your "back" is the path you took to get to the shed.')
        print('____________________')
        print('____________░░░░░░░░___')
        print('_________░░░░░░░░████▒▒__')
        print('________░░░░░░░░░░░░▒▒██▒▒_')
        print('_______░░░░▒▒______░░▓▓▒▒░░__')
        print('_____░░░░░░__________░░██__░░')
        print('_____░░░░░░____________░░▓▓____')
        print('_____░░░░░░____________░░▓▓__▒▒')
        print('_____░░░░░░______________░░▓▓▒▒')
        print('_____░░░░░░______________░░▓▓▓▓')
        print('_____░░░░░░______________░░░░░░')
        print('_____░░░░░░______________░░░░░░')
        print('_____░░░░░░______________░░░░░░')
        print('_____░░░░░░______________░░░░░░')
        print('_____░░░░░░______________░░░░░░')
        print('_____░░░░░░______________░░░░░░')
        print('_____░░░░░░______________░░░░░░')
        print('_____░░░░▒▒░░░░░░________░░░░░░')
        print('___░░▒▒▓▓▓▓▓▓▒▒▒▒░░░░____░░░░░░_')
        print('__░░░░▒▒▒▒██▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░_')
        print('__░░░░░░▒▒░░▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░_____')
        print('_░░░░░░░░▒▒░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░__')
        print('_░░░░░░░░▒▒░░▒▒░░░░░░░░░░░░▓▓▒▒░░▒▒░░░░░░')
        print('_░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓░░░░░░__')
        print('_░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░_')
        print('░░░░░░░░░░░░░░▒▒░░░░▒▒░░░░░░░░░░░░░░__░░░░░░')
        print('_░░░░░░░░░░▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░')
        print('_░░░░░░░░░░▒▒▒▒▒▒░░▓▓▒▒░░░░░░░░__░░░░░░░░░░')
        print('_░░░░░░░░░░▒▒▓▓▒▒░░▒▒▓▓░░░░░░░░░░____░░░░░░')
        print('_░░▒▒░░░░░░░░▓▓▓▓░░▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░')
        print('_░░░░░░░░░░░░░░▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░')
        print('_░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░')
        print('_░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░')
        print('_░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print('_░░░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░░░░░____░░░░░░░░')
        print('_░░░░░░▓▓▒▒░░░░▒▒▓▓░░▒▒▓▓▒▒░░░░░░░░________░░')
        print('_░░░░░░▒▒░░▒▒░░░░██▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░')
        print('_░░░░░░▓▓░░▓▓░░░░░░▒▒▒▒░░░░▓▓▒▒__░░▒▒▒▒▓▓░░░░')
        print('_░░░░░░▓▓▒▒░░░░░░░░░░▒▒░░░░▒▒▓▓__░░▒▒▓▓▓▓░░░░░░')
        print('_░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒░░░░░░▒▒▓▓▒▒░░░░__')
        print('_░░░░░░░░░░▓▓░░░░▓▓▒▒░░░░▓▓▓▓░░░░░░░░░░░░░░░░░░')
        print('_░░░░░░▓▓▒▒▒▒░░░░▓▓▒▒▒▒▒▒▓▓██▒▒░░░░░░░░░░░░░░')
        print('_░░░░░░▒▒▓▓▓▓░░░░██▒▒░░▒▒▓▓▒▒░░░░░░░░░░░░░░░░__')
        print('_░░░░░░██▓▓░░░░░░░░▒▒░░▒▒▓▓░░░░▒▒▒▒░░░░▓▓░░░░░░')
        print('_░░░░░░▓▓▒▒▒▒░░░░░░░░░░▒▒░░░░░░▒▒▒▒░░░░▓▓░░░░░░')
        print('_░░░░░░▒▒░░▒▒░░░░░░░░░░░░▓▓░░░░░░▒▒▒▒▓▓░░░░░░░░')
        print('_░░░░░░▓▓░░▓▓░░░░▓▓▒▒░░░░▓▓▓▓░░░░░░░░░░░░░░░░')
        print('_░░░░░░▒▒▒▒▒▒░░░░▓▓▒▒▒▒▒▒▓▓██▒▒░░░░░░░░░░░░░░')
        print('_░░░░░░▒▒▒▒▓▓░░░░▓▓▒▒░░▒▒▓▓▓▓░░░░░░░░░░░░░░░░')
        print('_░░░░░░▓▓▓▓▒▒░░░░░░▒▒░░▒▒▓▓░░░░▒▒▒▒░░░░▒▒░░░░')
        print('_░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░░░░░▒▒▒▒░░░░▓▓░░░░')
        print('_░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░░░░░▒▒░░▓▓░░░░░░')
        print('__░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print('___░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print('____░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░')
        print('______░░▒▒░░░░░░░░░░░░░░')
        print('__________░░░░░░░░░')
        shed_door()
    elif choice == "help":
        help()
        print('\n \n \n')
        shed_door()
    elif choice == "back":
        main()
    else:
        print('wrong')
        shed_door()

    #----------------------------------------------------------------------------

def bushes():
    print('you decide to search the bushes...')
    diechance_bush = random.randint (1, 6)
    if diechance_bush == 1:
        print('there was a man in the bush.')
        death()
    else:
        time.sleep(1.2)
        print('There is a number off of the address post. the number reads "4"')
        time.sleep(1.2)
        main()

#----------------------------------------------------------------------------

def check_door():
        print("There is a man at the door... open?\n")
        choice = input()
        if choice == "yes":
            print('you open the door, the man, dressed entirely in black with his face covered by shade provided from his brimmed hat. you only have a couple of seconds\nto look at his face before you meet your end. he cuts into your belly, you suffocate on your own blood.\n\n\n')
            death()
        elif choice == "no":
            print('you look through the peephole, it is a man covered in black clothing, a trench coat and hat are the most distinguishable features. his presence is threatening. you return to the living room.')
            livingroom()
        elif choice == "help":
            help()
            print('\n \n \n')
            check_door()
        else:
            print('I dont know what that is')
            check_door()

#----------------------------------------------------------------------------

def help():
    print("press enter after every choice to submit!")
    print('type "look" to look around')
    print('try "search" in some rooms to check for clues, or objects')
    print('some items, or locations in "quotation marks" are interactable. try entering them or "go to ____" to interact')
    print('type "help" at any time to see these options again!')

#-----------------------------------------------------------------------------

def go_home():
    print('You walk up to the door, you fumble with your keys before pressing your hand to the tarnished, brass handle.\n')
    time.sleep(4.5)
    print('click.\n')
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
    time.sleep(1.75)
    print('\n\n\n')
    time.sleep(0.9)
    print('\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0:::::::::::::::::::::::::::::::::.')
    print('.^~~~^^^::777777777777777777777777777777777^')   
    print('.7???????????~..........................!77^')   
    print('.!?7777??????^\t\t\t \t ~77^')   
    print('.!?7!!!??????^\t\t\t \t ~77^')   
    print('.7?7!!!??????^\t\t\t \t ~77^')   
    print('.7?7~~~7?????^\t\t\t \t ~77^')   
    print('.!?7^~~7?????^\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t \t ~77^')   
    print('.7?!^^^7?????^\t\t\t \t ~77^')   
    print('.!?!^^^7?????^\t\t\t \t ~77^') 
    print(':7J?!^^7?????^\t\t\t \t ~77^')   
    print('.~JYJ7~^7?????^\t\t\t \t ~77^')   
    print('.7?!^^~7?????^\t\t\t \t ~77^')   
    print('.7?7^^~7?????^\t\t\t \t ~77^')   
    print('.7?7^~~7?????^\t\t\t \t ~77^')   
    print('.7?7^~~7?????^\t\t\t \t ~77^')   
    print('.7?7~~~7?????^\t\t\t \t ~77^')   
    print('.7?7~~~7?????^\t\t\t \t ~77^')   
    print('.7?7~~~??????^\t\t\t \t ~77^')   
    print('.7?7~~~??????^\t\t\t \t ~77^')   
    print('.7?7~~~??????^\t\t\t \t ~77^')   
    print('.7?7~~~??????^\t\t\t \t ~77^')   
    print('.7?7~~!??????^\t\t\t \t ~77^')   
    print('.7?7!!!??????^\t\t\t \t ~77^')   
    print('.7?7!!7??????^\t\t\t \t ~77^')   
    print('.7???????77!!:\t\t\t \t ^~~:')   
    print('.~~~^::..\t\t\t \t \t .')                                
    print('\n\n\n')
    time.sleep(1.2)
    print('you step inside your home, the dry warmth of your home hits your face in a violent contrast to the cold, outisde air.\n')
    time.sleep(2.0)
    print('your stomach growls.\n')
    time.sleep(1.0)
    print("Should you get some food then? what are you feeling...\n")
    print("pizza.")
    print("chinese.\n")
    choice = input()
    if choice == "pizza":
        get_pizza()
    elif choice == "chinese":
        get_chinese()
    else:
        print('I dont know what that is')
        go_home()

#------------------------------------------------------------------------------

def get_pizza():
    print('you call your go-to, favorite pizza place, Junimos. they will be here shortly.')
    time.sleep(3.0)
    print("\nthe pizza man is at the door, you tip $5 and sit inside, turning on the tv.\n")
    time.sleep(0.5)
    print("you take a bite, the pizza was yummy!\n")
    time.sleep(0.5)
    print('\n*knock knock*... "but the delivery guy already came..."')
    print("\n check it out?")
    choice = input()
    if choice == "yes":
        check_door()
    elif choice == "no":
        dont_check()
    else:
        print('I dont know what that is')
        get_pizza()
#--------------------------------------------------------------------------------

def dont_check():
    print("you sit and enjoy your pizza, prentending noone is home.")
    print("\nwait.")
    time.sleep(1.0)
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
        print('your fireplace displays its ability to warm your house. it crackles, the occasional pop of the pine being changed from earth to ash occours.')
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
    else:
        print('I dont know what that is')
        livingroom()
#------------------------------------------------------------------------------------------

def get_chinese():
    print("\nyou decide to run and get chinese...")
    time.sleep(2.5)
    print('on the way out, you notice a van across the street. youve never seen it in the neighborhood before, so you double check to make sure youve locked your front door\nand get a move on. why has today been so creepy?...')
    time.sleep(1.0)
    print('the ride to your favorite chinese place, Mr. Lus, goes smooth. You order the typical seasame chicken and go home.')
    time.sleep(1.0)
    print('the aroma of the chicken is tempting on the ride home, but you wait with urgence. when you finally get home, you see that your front door has been opened with great force\nsplintered wood decorates the doorframe. you take a cruise to the police station as you do not have your mobile phone.')
    print('\nthe police found evidence of a break in during your absence to get food.\n it appears that there was up to 5 people in the home at the same time. maybe by a miracle, you were gone.\n\nmysteriously, there were no fingerprints found at the scene of the crime. but instead a note.')
    print('\n"we will get you next time."\n')
    print('you decide to stay at a friends house tonight. maybe tomorrow you could figure out a long term solution.')
    win()

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
        print('your fireplace displays its ability to warm your house. it crackles, the occasional pop of the pine being changed from earth to ash occours.')
        print('your pizza steams, the top of the box reads "Junimos"... ')
        print('not much else of note.\n')
        livingroom()
    elif choice == "help":
        help()
        print('\n \n \n')
        livingroom()
    elif choice =="hallway":
        hallway()
    else:
        print('I dont know what that is')
        livingroom()
#------------------------------------------------------------------------------------------

def hallway():
    print('You are now in the hallway.')
    choice = input()
    if choice == "look":
        print('You are in the hallway. there is the door to the livingroom, \na doorway to the kitchen, \na door to the bathroom and a door to the bedroom.')
        print('type "livingroom" for the livingroom. \n"kitchen" for the kitchen \n"bathroom" for bathroom and "bedroom" for bedroom.')
        hallway()
    elif choice =="search":
        print('details about hallway.')
        hallway()
    elif choice == "help":
        help()
        print('\n \n \n')
        hallway()
    else:
        print('I dont know what that is')
        hallway()

#-------------------------------------------------------------------------

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
    else:
        print('I dont know what that is')

#------------------------------------------------------------

def death():
    print('░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░') 
    print('░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░') 
    print('░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░') 
    print('\u00A0░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░') 
    print('\u00A0\u00A0\u00A0░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░') 
    print('\u00A0\u00A0\u00A0\u00A0░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░') 
    print('\u00A0\u00A0\u00A0░▒▓█▓▒░    ░▒▓██████▓▒░ ░▒▓██████▓▒░       ░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░')
    print('\n\n\n type restart to try again.')
    choice = input()
    if choice == "restart":
        main()
    if choice == "quit":
        exit()
    else:
        print('please choose "restart" or "quit".\n')
        death()
    
#------------------------------------------------------------

def in_shed():
    print('you are in the shed.')

#-------------------------------------------------------------

def win():
    print('░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░ ') 
    print('░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░') 
    print('░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░') 
    print('░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░') 
    print('░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░') 
    print('░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░')
    print(' ░▒▓█████████████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░')
    print('\n\n\n congrats! type restart to try another route!')
    print('\n\nCoding by: Ethan Blocher\n')
    choice = input()
    if choice == "restart":
        main()
    if choice == "quit":
        exit()
    else:
        print('please choose "restart" or "quit".\n')
        win()

#-------------------------------------------------------------

def dining_room_haunt():
    print('you are in the old house')
    choice = input()
    if choice == "look":
        print('when you walked in, you notice the overwhelming stench of decay. in front of you is a "doorway". to your right is what you assume are the "attic" steps.')
        print('\nsomething about this place bothers you.')
        dining_room_haunt()
    elif choice == "search":
        print('the stench is almost unbearable. its a smell of decaying wood, dirt, dead animals and a subtle smell of candles.')
        print('the appearance of this room is abyssmal, its almost too dark to see in here without your lighter.')
        print('\nthe table in the center of the room has a pot in the center, it is covered in mold. the table looks like it would break if you breathed on it too hard.')
        print('the small holes in the floor make walking around here a minefield, forget running if you need to leave in a pinch.')
        dining_room_haunt()
    elif choice == "doorway":
        livingroom_haunt()
    elif choice == "back door":
        print('\n\n you decide to leave out the back door.')
        print('this has proven to be fatal')
        print('you were ambushed on your way out. two people, you couldnt even describe a single feature it happened so fast. they chased you back into the house as you tried to leave, you tripped and fell on one of the holes\n in the floor. you were knocked out on impact.\nand never woke up.\n both you, and noone will ever know what happened to you other than your pursuers.')
        death()
    elif choice == "attic steps":
        attic()
    elif choice == "basement":
        basement()
    elif choice == "help":
        help()
        print('\n \n \n')
        dining_room_haunt()
    else:
        print('I dont know what that is.')
        dining_room_haunt()

#--------------------------------------------------------------

def livingroom_haunt():
    print('you are now in another room of the house.')
    choice = input()
    if choice == "help":
        help()
        print('\n \n \n')
        livingroom_haunt()
    elif choice == "look":
        print('there is a doorway to the "hallway", there is the "front door", the "kitchen" is next to this room and another "doorway".')
        livingroom_haunt()
    elif choice == "search":
        print('this room looks like an old livingroom. a really old 8-track player is decorated with a carpet of dust and a couch covered in mildew and a giant hole in the middle of the room.\n there is a moldy, rancid stench in this room.')
        print('there is a note that reads...\n"basement... diningroom..."\n\nominous.')
        livingroom_haunt()
    elif choice == "hallway":
        hallway_haunt()
    elif choice == "front door":
        front_door()
    elif choice == "kitchen":
        kitchen_haunt()
    elif choice == "doorway":
        dining_room_haunt()
    else:
        print('I dont know what this is.')
        livingroom_haunt()
#--------------------------------------------------------------

def attic():
    global key_status_haunt
    print('you are in the attic of the house.')
    choice = input()
    if choice == "help":
        help()
        print('\n \n \n')
        attic()
    elif choice == "look":
        print('there are the "steps" back down to the other room. in front of you is a locked "box".')
        attic()
    elif choice == "search":
        print('The attic is in relatively good shape in comparison to the rest of the house. There is a leather box on the ground in front of you, the top reads "Rellik". huh. sounds russian.\nthere is a heavy, but breathable dust in the air, there is also a warmth to the attic that the rest of the house\ndoes not exhibit. there are also an assortment of glass bottles in the corner.\nall empty.')
        attic()
    elif choice == "box":
        if key_status_haunt == ('key'):
            print('you open the box. inside is another number off the side of the house, it reads "7".')
            attic()
        else:
            print('you need a key to open this')
            attic()
    else:
        print('I dont know what this is.')
        attic()
#--------------------------------------------------------------

def basement():
    print('you are in the basement of the house.')
    print('\nit is so dark in here. if you stay. You are likely be eaten by a grue.')
    choice = input()
    if choice == "back":
        dining_room_haunt()
    elif choice == "help":
        print('You have been eaten by a grue.')
        death()
    elif choice == "look":
        print('You have been eaten by a grue.')
        death()
    elif choice == "search":
        print('You have been eaten by a grue.')
        death()
    else:
        print('I dont know what this is.')
        basement()
#-----------------------------------------------------------------

def bedroom_haunt():
    print('you are in a room in the house.')

#-----------------------------------------------------------------

def kitchen_haunt():
    print('you are in a room in the house.')

#-------------------------------------------------------------------

def bathroom_haunt():
    print('you are in a weird bathroom.')
    choice = input()
    if choice == "help":
       help()
       print('\n \n \n')
       bathroom_haunt()
    elif choice == "look":
        print('there is one door in, and out. this door goes back to the "hallway".')
        bathroom_haunt()
    elif choice == "search":
        print('DETAILS')
        bathroom_haunt()
    else:
        print('I dont know what this is.')
        bathroom_haunt()
#------------------------------------------------------------------

def hallway_haunt():
    print('you are in the hallway of the house.')
    choice = input()
    if choice == "help":
        help()
        print('\n \n \n')
        hallway_haunt()
    elif choice == "look":
        print('in the hallway, there is a "doorway" to the livingroom, a doorway to a weird "bathroom", maybe, and two more doors, one to a "bedroom" and the "other" is splintered.')
        hallway_haunt()
    elif choice == "search":
        print('a plain hallway, very stuffy, the air is thick and there is no ventilation. it feels like if you are in this hallway any longer you might pass out.')
        hallway_haunt()
    elif choice == "doorway":
        livingroom_haunt()
    elif choice == "bathroom":
        bathroom_haunt()
    elif choice == "bedroom":
        bedroom_haunt()
    elif choice == "other":
        time.sleep(1.2)
        print('the old door is splintered. between the cracks you can see a bed, some debris on the ground and a giant hole in the wall and where the ceiling was supposed to be.\n\nthere is a mass of plants and other damp organic matter hanging in the way of everything. \nthis room is totally inaccessable.')
        hallway_haunt()
    else:
        print('I dont know what this is.')
        hallway_haunt()

#--------------------------------------------------------------------

main()









#format (literally the same as below, just copy/paste)
#choice = input()
#   if choice == "help":
#       help()
#       print('\n \n \n')
#       ()
#   elif choice == "":
#
#   elif choice == "":
#
#   else:
#       print('I dont know what this is.')


#tab in for content of the "if" statement
# choice = input("front or back?")
# if choice =="front":
#   front door code
# elif choice =="back":
#   back door code
# else:
#   print("i don't know what this is")

#some notes: 
#the haunted house is almost, but not quite finished. The "home" path needs a lot of work.