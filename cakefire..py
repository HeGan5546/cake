import turtle
import random
import time
from playsound import playsound
import threading

# Initialize turtle screen
screen = turtle.Screen()
screen.bgcolor("#000000")
screen.title("Happy Birthday")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("white")

# --- Function to play birthday song in background ---
def play_music():
    playsound("birthday_song.mp3")  # Place the file in the same folder

# --- Function to display animated text ---
def animated_text():
    pen.penup()
    pen.goto(0, 250)
    pen.color("gold")
    message = "Happy Birthday!"
    for char in message:
        pen.write(char, font=("Script", 40, "bold"), align="center")
        pen.forward(25)
        time.sleep(0.2)
    pen.goto(0, 210)
    pen.write("Wishing you joy and sparkle 🎉", align="center", font=("Arial", 16, "normal"))

# --- Function to draw one firework ---
def draw_firework(x, y):
    colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "pink"]
    fw = turtle.Turtle()
    fw.hideturtle()
    fw.speed(0)
    fw.penup()
    fw.goto(x, y)
    fw.pendown()
    for _ in range(20):
        fw.color(random.choice(colors))
        fw.forward(100)
        fw.backward(100)
        fw.left(18)
    fw.clear()

# --- Function to randomly trigger fireworks ---
def fireworks():
    for _ in range(10):
        x = random.randint(-250, 250)
        y = random.randint(0, 300)
        draw_firework(x, y)
        time.sleep(0.4)

# --- Your existing cake drawing function goes here ---
def draw_cake():
    cake = turtle.Turtle()
    cake.speed(0)
    cake.penup()
    cake.goto(-100, -150)
    cake.pendown()
    cake.color("chocolate", "bisque")
    cake.begin_fill()
    for _ in range(2):
        cake.forward(200)
        cake.left(90)
        cake.forward(100)
        cake.left(90)
    cake.end_fill()

    # Layers
    cake.penup()
    cake.goto(-100, -50)
    cake.color("brown", "pink")
    cake.begin_fill()
    cake.pendown()
    for _ in range(2):
        cake.forward(200)
        cake.left(90)
        cake.forward(50)
        cake.left(90)
    cake.end_fill()

    # Candle
    cake.penup()
    cake.goto(0, 0)
    cake.color("blue", "yellow")
    cake.begin_fill()
    cake.pendown()
    cake.left(90)
    cake.forward(40)
    cake.right(90)
    cake.forward(10)
    cake.right(90)
    cake.forward(40)
    cake.end_fill()

    # Flame
    cake.penup()
    cake.goto(5, 40)
    cake.color("orange")
    cake.begin_fill()
    cake.pendown()
    cake.circle(6)
    cake.end_fill()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Start music in background
    threading.Thread(target=play_music, daemon=True).start()

    # Draw cake
    draw_cake()

    # Show text with animation
    animated_text()

    # Launch fireworks
    fireworks()

    # Hold window open
    screen.mainloop()