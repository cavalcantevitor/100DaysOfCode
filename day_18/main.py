import turtle
import random

color_list = [(207, 165, 127), (164, 169, 38), (140, 48, 106), (244, 79, 57), (3, 144, 60),
              (241, 66, 140), (2, 142, 185), (162, 55, 52), (243, 101, 162), (53, 203, 226),
              (251, 228, 16), (22, 166, 128), (253, 230, 0), (27, 196, 219), (156, 186, 168),
              (236, 164, 192), (107, 45, 102), (142, 212, 224), (243, 171, 151), (160, 211, 180),
              (6, 116, 36), (191, 192, 194), (136, 42, 34)]

t = turtle.Turtle()
turtle.colormode(255)
y = 0

for _ in range(10):
    t.penup()
    t.goto(0, y)
    t.pendown()

    for _ in range(10):
        t.dot(15, random.choice(color_list))
        t.penup()
        t.forward(35)
        t.pendown()

    y += 35

screen = turtle.Screen()
screen.exitonclick()
