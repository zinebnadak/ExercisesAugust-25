#ASSIGNMENT 2: ITERATION AND RANDOM NUMBERS

#1. TURTLE GRAPHICS
import turtle
import random

#screen and background
screen = turtle.Screen()
screen.colormode(255)       # Set color mode to accept 0–255 RGB values. HEX number do not need this!
screen.bgcolor((25,24,84))     #bg stands for background, HEX number (#191854)

#stars
stars_num = int(input("Enter number of stars!: "))

#create the turtle for star
star = turtle.Turtle()     #our turtle that is going to draw stars for us
star.color((240,201,5))
star.pensize(5)
star.speed(2)
star.hideturtle()


for i in range (1,stars_num+1):
    for x in range (5):     #draw five pointed star
        star.forward(50)    #determines star size
        star.right(144)

turtle.done()

#i want the users desired number of stars to be printed randomly  on upper half of sheet








screen.exitonclick()        #keep window open until clicked
