# CTI 110
# P2LAB2
# Blocher E
# 10/17

col_choice1 = ("red")
col_choice2 = ("red")
col_choice3 = ("red")
col_choice4 = ("red")
print ("choose color ONE!")
col_choice1 = input()
col_choice2 = input()
col_choice3 = input()
col_choice4 = input()

colors = [col_choice1, col_choice2, col_choice3, col_choice4]

import turtle
t = turtle.Turtle()
t.speed(7)
turtle.bgcolor("black")
t.pensize(1)


for steps in range(250):
    t. forward(steps + .1)
    t.right(45)
    t.left(1)
    # rotate between color in colors
    color = colors[steps % 4]

    t.pencolor(color)
t.mainloop()
