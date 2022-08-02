from turtle import Turtle, Screen
import random

color_list = ['light gray', 'gold', 'chartreuse', 'salmon', 'medium slate blue', 'firebrick', 'khaki', 'ivory',
              'cadet blue', 'lime green']

tim = Turtle()
side_num = 11
tim.speed('fastest')

def draw_shape(side_num):
    angle = 360 / side_num
    for side in range(side_num):
        tim.forward(100)
        tim.right(angle)

for i in range(3, side_num):
    tim.color(random.choice(color_list))
    draw_shape(i)


screen = Screen()
screen.exitonclick()