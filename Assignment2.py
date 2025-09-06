#ASSIGNMENT 2: ITERATION AND RANDOM NUMBERS

#1. TURTLE GRAPHICS
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")     #bg is for background

#stars
stars_num = int(input("Enter number of stars!: "))

#create the turtle
star = turtle.Turtle()     #our turtle that is going to draw for us
star.color("yellow")
star.pensize(35)
star.speed(2)
star.hideturtle()

def draw_star (x,y,size, color):
    star.penup()
    star.goto(x, y)
    star.setheading(0)
    star.pendown()
    star.color(color)
    for _ in range(5):      #draw five pointed star
        star.forward(size)
        star.right(144)

for i in range(1, stars_num + 1):
    x = random.randint(-300, 300)       # Random x (screen width)
    y = random.randint(0, 300)          # Only upper half (y > 0)
    size = random.randint(20, 70)       # Random size for fun








#for i in range (1,stars_num+1):
    #for x in range (5):     #draw five pointed star
        #star.forward(100)
        #star.right(144)











screen.exitonclick()        #keep window open until clicked
