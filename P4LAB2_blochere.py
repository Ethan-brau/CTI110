numchoice = 0

def main():
    print('Please type a positive number.')
    numchoice = int(input())
    # repeat if invalid
    while numchoice < 1:
        print('Please type a positive number.')
        numchoice = int(input())

    count = 1;
    while count < 12:
        # count upward from 1 to 12
        print(numchoice,"*",count,"=",numchoice * count)
        count += 1
    repeat()
    
def repeat():
    print('would you like to go again?')
    choice = input()
    if choice == "yes":
        main()
    elif choice == "no":
        exit()
    else:
        print('please say yes, or no.')
        repeat()
main()
