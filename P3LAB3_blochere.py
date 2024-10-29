#CTI 110
#P3LAB3 - Letter grades
#blochere
#converting number grades to letter grades

num_grade = int(input('What is the grade? (0-100):'))
lettergrade = "nil"

if num_grade >= 90:
    lettergrade = "A"
elif num_grade >= 80:
    lettergrade = "B"
elif num_grade >= 70:
    lettergrade = "C"
elif num_grade >= 60:
    lettergrade = "D"
elif num_grade >= 1:
    lettergrade = "F"

print('your letter grade is:', lettergrade)
