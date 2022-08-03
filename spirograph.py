import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.pensize(1)


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_circle(c_size, times):
    a_move = 360 / times
    for i in range(times):
        tim.color(get_color())
        tim.circle(c_size)
        cur_heading = tim.heading() + a_move
        tim.setheading(cur_heading)


draw_circle(100, 36)

screen = t.Screen()
screen.exitonclick()
