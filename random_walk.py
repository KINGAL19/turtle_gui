import turtle as t
import random

tim = t.Turtle()
tim.speed('fastest')
tim.pensize(15)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


for _ in range(200):
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
    tim.forward(50)

screen = t.Screen()
screen.exitonclick()
