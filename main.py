import colorgram
import turtle
from turtle import Screen
import random
#colors = colorgram.extract("Damien-Hirst.jpg",200)
# my_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_list.append((r,g,b))
color_list = [(8, 16, 67), (63, 8, 28), (192, 70, 22), (144, 11, 35), (248, 237, 242), (13, 45, 142), (30, 103, 175),
              (123, 162, 201),(8, 20, 67),(192, 102, 22)]
painter = turtle.Turtle()
Screen().colormode(255)
painter.speed("fastest")
painter.hideturtle()
i=0
painter.penup()
painter.setheading(225)
painter.pen()
painter.forward(300)
painter.setheading(0)


while i<10:
 j=0
 i += 1

 while j<10:
     painter.pendown()
     painter.dot(20,random.choice(color_list))
     painter.up()
     painter.forward(50)
     painter.down()
     j+=1
 painter.penup()
 painter.setheading(90)
 painter.forward(50)
 painter.setheading(180)
 painter.forward(500)
 painter.setheading(0)


screen = Screen()
screen.exitonclick()
