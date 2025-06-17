import turtle 
# Set background
bg = turtle.Screen()
bg.bgcolor("black")

# Bottom Line 1
turtle.penup()
turtle.goto(-170, -180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160, -150)
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150, -120)
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-100, -100)
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

# Candles
colors = ["red", "blue", "yellow", "green", "purple"]
x_positions = [-90, -60, -30, 0, 30]
for color, x in zip(colors, x_positions):
    turtle.penup()
    turtle.goto(x, 0)
    turtle.color(color)
    turtle.pendown()
    turtle.forward(20)

# Decoration
colors = ["red", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40, -50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

# Happy Birthday Message
turtle.penup()
turtle.goto(-150, 50)
turtle.color("pink")
turtle.pendown()
turtle.write("Happy Birthday!", font=("Arial", 24, "bold"))

# Finish
turtle.hideturtle()
turtle.done()
