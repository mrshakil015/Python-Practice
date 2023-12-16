from turtle import Turtle, Screen
import random

shape = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen","wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        shape.forward(70)
        shape.right(angle)

for shape_side_n in range(3,11):
    shape.color(random.choice(colours))
    draw_shape(shape_side_n)

screen= Screen()
screen.exitonclick()