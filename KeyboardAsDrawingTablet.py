import keyboard
import turtle
t = turtle.Turtle()
turtle.Screen().setup(1104, 408)
while True:
    if keyboard.is_pressed("esc"):
        break
    elif keyboard.is_pressed("up"):
        t.penup()
    elif keyboard.is_pressed("down"):
        t.pendown()
    elif keyboard.is_pressed("1"):
        t.goto(-500,100)
    elif keyboard.is_pressed("2"):
        t.goto(-400,100)
    elif keyboard.is_pressed("3"):
        t.goto(-300,100)
    elif keyboard.is_pressed("4"):
        t.goto(-200,100)
    elif keyboard.is_pressed("5"):
        t.goto(-100,100)
    elif keyboard.is_pressed("6"):
        t.goto(0,100)
    elif keyboard.is_pressed("7"):
        t.goto(100,100)
    elif keyboard.is_pressed("8"):
        t.goto(200,100)
    elif keyboard.is_pressed("9"):
        t.goto(300,100)
    elif keyboard.is_pressed("0"):
        t.goto(400,100)
