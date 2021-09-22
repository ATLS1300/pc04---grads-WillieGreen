"""
Created on Thu Sep 16 11:39:56 2021
PC04 start code
@author: William Green

********* HEY, READ THIS FIRST **********

this code generates 2 patters. The first are a random amount of rainbow circles rotating
around a central point. The secont is 6 curved lines that follow around the circles.

"""
#import libraries
import turtle
import random

turtle.colormode(255)
turtle.tracer(0)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 

#define variables and turtles
r = random.randint (15,45)
v = 360/r
flower = turtle.Turtle()
curves = turtle.Turtle()
colors  = ["red","green","blue","orange","purple","pink","yellow","red","green","blue","orange","purple","pink","yellow","red","green","blue","orange","purple","pink","yellow"]

#define first turtle pen
flower.width(5)
flower.pencolor("white")

#pattern 1
for x in range(int(v)):
    flower.fillcolor(colors[x])
    flower.begin_fill()
    flower.circle(100)
    flower.left(r)
    flower.end_fill()

#define and position turtle 2
curves.width(10)
curves.penup()
curves.color("white")
curves.goto(0,200)
curves.right(90)
curves.pendown()

#pattern 2
for y in range(int(v)):
    for z in range(120):
        curves.forward(2)
        curves.right(1)
    curves.left(180)
     

panel.update()
turtle.done()
