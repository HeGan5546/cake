# Importing required libraries
import turtle
import random

# Creating turtle and screen
my_turtle_cursor = turtle.Turtle()
my_turtle_screen = turtle.Screen()
my_turtle_screen.bgcolor("#FFFDD0")  # Light cream background

# Starting Y-coordinate for cake base
y_coordinate = -125

# Function to draw a candle
def draw_candle_for_cake(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    for _ in range(2):
        my_turtle_cursor.forward(25)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(60)
        my_turtle_cursor.left(90)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

# Function to draw stick (flame holder) on the candle
def draw_stick_on_candle(fill_color, x, y, cursor_size):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.setheading(-90)
    my_turtle_cursor.pendown()
    my_turtle_cursor.forward(12)
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

# Function to draw decorative toppings
def draw_toppings_on_cake(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.forward(10)
    my_turtle_cursor.left(90)
    my_turtle_cursor.circle(radius, extent=180)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

# Function to draw a layer of the cake
def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    my_turtle_cursor.hideturtle()
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.color(border_color)
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()
    for _ in range(2):
        my_turtle_cursor.forward(width)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(height)
        my_turtle_cursor.left(90)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

# Function to write the full message centered
def write_birthday_message(text_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.color(text_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.write("🎉 Happy Birthday Ashim JeeNa 🎉", align="center", font=("Arial", 24, "bold"))
    my_turtle_cursor.getscreen().update()

# UPDATED: Function to draw multicolor firework at once
def draw_firework(x, y, colors):
    for color in colors:
        f = turtle.Turtle()
        f.speed(0)
        f.hideturtle()
        f.penup()
        f.goto(x, y)
        f.pendown()
        f.pensize(2)
        f.color(color)
        for _ in range(12):
            f.forward(50)
            f.backward(50)
            f.left(30)

# Draw cake plate
draw_layer_of_the_cake("#FFC0CB", "#000000", 3, -220, y_coordinate - 70, 400, 10)

# Cake layers: [fill, border, pen size, height]
parts_of_cake = [
    ["#A020F0", "#000000", 3, 30],
    ["#55FF55", "#000000", 3, 20],
    ["#B87333", "#000000", 3, 60]
]

# Draw cake layers
for part in parts_of_cake:
    draw_layer_of_the_cake(part[0], part[1], part[2], -135, y_coordinate - 60, 240, part[3])
    y_coordinate += part[3]

# Draw toppings
toppings = [
    ("#C20067", "#000000", -120, y_coordinate - 60),
    ("#FFFF00", "#000000", -80, y_coordinate - 60),
    ("#FF0000", "#000000", 25, y_coordinate - 60),
    ("#0000FF", "#000000", 59, y_coordinate - 60),
    ("#FFA500", "#000000", -135, y_coordinate - 80),
    ("#E4E6EB", "#000000", -135, y_coordinate - 100),
    ("#FFA500", "#000000", -135, y_coordinate - 120),
    ("#181A18", "#000000", -80, y_coordinate - 80),
    ("#0000FF", "#000000", -65, y_coordinate - 110),
    ("#FFD700", "#000000", -95, y_coordinate - 140),
    ("#181A18", "#000000", 10, y_coordinate - 80),
    ("#E4E6EB", "#000000", -20, y_coordinate - 110),
    ("#181418", "#000000", 35, y_coordinate - 140),
    ("#FFA500", "#000000", 75, y_coordinate - 80),
    ("#E4E6EB", "#000000", 75, y_coordinate - 110),
    ("#FFD700", "#000000", 75, y_coordinate - 140)
]

for fill, border, x, y in toppings:
    draw_toppings_on_cake(fill, border, x, y, 10)

# Draw candle and stick
draw_candle_for_cake("#FFF44F", "#000000", -40, y_coordinate - 60)
draw_stick_on_candle("#000000", -26, y_coordinate + 15, 7)

# Draw centered birthday message
write_birthday_message("#B87333", 0, 100)

# Draw fireworks with all colors at once
firework_colors = ["red", "blue", "pink", "orange", "white", "purple", "cyan"]
draw_firework(-100, 220, firework_colors)
draw_firework(100, 220, firework_colors)
draw_firework(0, 250, firework_colors)

# Keep window open
my_turtle_screen.mainloop()