import turtle as t
import random

# import colorgram

# colors_list = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_list.append((r, g, b))
#
# print(colors_list)

colors_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)
tim = t.Turtle()
tim.speed(10)
tim.penup()
tim.goto(-100, -100)


def dot_line(dot, gap):
    dot_count = 0
    for i in range(10):
        tim.color(random.choice(colors_list))
        tim.dot(dot)
        dot_count += 1
        tim.forward(gap)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(gap)
            tim.setheading(180)
            tim.forward(200)
            tim.setheading(0)
for i in range(10):
    dot_line(10, 20)

tim.hideturtle()
screen = t.Screen()
screen.exitonclick()