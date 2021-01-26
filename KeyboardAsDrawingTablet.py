import keyboard
import turtle
t = turtle.Turtle()
turtle.Screen().setup(1104, 408)
while True:
    if keyboard.is_pressed("1"):
        t.goto(100,100)
    if keyboard.is_pressed("2"):
        t.goto(200,100)
    if keyboard.is_pressed("3"):
        t.goto(300,100)
    if keyboard.is_pressed("4"):
        t.goto(400,100)
    if keyboard.is_pressed("5"):
        t.goto(500,100)
    if keyboard.is_pressed("6"):
        t.goto(600,100)
    if keyboard.is_pressed("7"):
        t.goto(700,100)
    if keyboard.is_pressed("8"):
        t.goto(800,100)
    if keyboard.is_pressed("9"):
        t.goto(900,100)
    if keyboard.is_pressed("0"):
        t.goto(1000,100)