# CTI 110
# P1LAB2
# Blocher
# 10/1/2024


# Burgers and fries

print("P1Lab2 \n \n ")
print("Start! \n \n")

num_burgers = 0
num_fries = 0
burger_cost = 6.99
fry_cost = 2.99

print("Can I take your order?")

num_burgers = int(input("How many burgers?"))
print("you ordered", num_burgers , "burgers \n \n")

num_fries = int(input("Great! now how many fries?"))
print("you ordered", num_fries , "fries \n \n")

print("order placed of", num_burgers , "burgers, and", num_fries, "fries, is this correct? (yes or no)")
answer = input()
if answer.lower() == "yes":
    print("okay, yes, \n great!")
elif answer.lower() == "no":
    print("no")
else:
    print("yes or no please...")

burger_total = num_burgers * burger_cost
fry_total = num_fries * fry_cost
print("-" * 35)
print(num_burgers, "burger(s) \t \t \t$", format(burger_total,  ".2f"))
print(num_fries, "fries \t \t \t$", format(fry_total, ".2f") )
print("-" * 35)
print("\t \t$", format(fry_total + burger_total, ".2f") )
