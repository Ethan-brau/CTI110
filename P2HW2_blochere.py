# CTI 110
# P2LAB2
# Blocher E
# 10/17

print ("\t\t\t---WELCOME to Ethan's grade assistant!---")

print ("please enter FOUR grades (ONE number at a time, then hit ENTER)")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

user_num = [num1, num2, num3, num4]
print("you entered:", user_num, "\n \n")
print("There are", len(user_num), "GRADES")
print("Smallest GRADE:", min(user_num))
print("Largest GRADE: ", max(user_num), "\n \n")

avg = sum(user_num) / len(user_num)
print("The average GRADE is", avg)
