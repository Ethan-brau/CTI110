# CTI - 110
# P2LAB1
# Ethan Blocher
# 10/10/2024

#__________Variables__________
amount = 0
price = 0
pre_tax = 0
tax = 0
real_total = 0

#__________Questions__________
print("Welcome to Ethan's shop assistant!\n\n")
item = input("What item are you buying?\n")
print("How many", item , "are you buying?\n")
amount = int(input())
price = float(input("for how much each?\n"))

#__________math+total__________
pre_tax = amount * price
tax = pre_tax * .1
total = pre_tax + tax

real_total = f"{total:.2f}"

#__________recipt__________
print(item, "\t\t----\t\t", price)
print(amount, "\t\t----\t\t", pre_tax)
print("tax(10%)\t----\t\t", tax)
print("total\t\t----\t\t", real_total)
print("______________________________________\n\n\n thanks for using Ethan's shop assistant today!")
















# name = input("what's your name?")
# print ("hey!", name)

#_____num_____
# word = input("What's the secret word?")
# number = int (input("Type in a number"))
# price = float (input("the cost is: $"))
