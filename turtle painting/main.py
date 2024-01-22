import turtle as turtle_module
import random

turtle_module.colormode(255)
screen = turtle_module.Screen()
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(450)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(70)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(70)
        tim.setheading(180)
        tim.forward(700)
        tim.setheading(0)

tim.hideturtle()
screen.exitonclick()




