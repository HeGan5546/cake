import turtle
import random

# Sets background
bg = turtle.Screen()
bg.bgcolor("black")

# Bottom Line 1
turtle.penup()
turtle.goto(-170, -180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid line 2
turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()
turtle.forward(300)

# First line 3
turtle.penup()
turtle.goto(-120, -120)
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-80, -80)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Icing
turtle.penup()
turtle.goto(-100, -5)
turtle.color("pink")
turtle.pendown()
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

# Candles
colors = ["red", "blue", "yellow", "green", "purple"]
height = 30
for color in colors:
    turtle.penup()
    turtle.goto(-50 + height, 45)
    turtle.color(color)
    turtle.pendown()
    turtle.goto(-50 + height, 85)
    height += 20

# Fireworks

# Function to draw a single firework explosion
def explode(x, y):
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "cyan"]
    for _ in range(36):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random.choice(colors))
        turtle.speed(0)
        turtle.setheading(random.randint(0, 360))
        length = random.randint(10, 200)
        turtle.forward(length)
        turtle.penup()
        turtle.backward(length)

# Function to launch a firework
def launch_firework():
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    explode(x, y)

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40, -50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

# Happy Birthday message
turtle.penup()
turtle.goto(-180, 100)
turtle.color("pink")
turtle.pendown()
turtle.write("Happy Birthday Ashim!", font=("Arial", 24, "bold"))
turtle.color("black")

turtle.done()
