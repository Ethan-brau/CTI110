# CTI 110
# P4HW1
# Blocher E
# 12/03

print ("\t\t\t---WELCOME to Ethan's grade assistant V2!---")

print ("please enter FOUR grades (ONE number at a time, then hit ENTER)")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
while num1 < 1:
    print('grade one is INVALID please enter new grade.')
    print ("please enter FOUR grades (ONE number at a time, then hit ENTER)")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

while num2 < 1:
    print('grade one is INVALID please enter new grade.')
    print ("please enter FOUR grades (ONE number at a time, then hit ENTER)")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

while num3 < 1:
    print('grade one is INVALID please enter new grade.')
    print ("please enter FOUR grades (ONE number at a time, then hit ENTER)")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

while num4 < 1:
    print('grade one is INVALID please enter new grade.')
    print ("please enter FOUR grades (ONE number at a time, then hit ENTER)")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

while num5 < 1:
    print('grade one is INVALID please enter new grade.')
    print ("please enter FOUR grades (ONE number at a time, then hit ENTER)")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

user_num = [num1, num2, num3, num4, num5]
print("you entered:", user_num, "\n \n")
print("There are", len(user_num), "GRADES")
print("Smallest GRADE:", min(user_num))
print("Largest GRADE: ", max(user_num), "\n \n")

avg = sum(user_num) / len(user_num)
print("The average GRADE is", avg)

while avg < 60:
    print('your letter grade is F')

while avg >= 60:
    print('your letter grade is D')

while avg >= 70:
    print('your letter grade is C')

while avg >= 80:
    print('your letter grade is B')

while avg >= 90:
    print('your letter grade is A')



