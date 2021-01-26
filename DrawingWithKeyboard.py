import keyboard
import turtle
t = turtle.Turtle()
turtle.getscreen()
while True:
    if keyboard.is_pressed("q"):
        break
    if keyboard.is_pressed("w"):
        t.forward(10)
    if keyboard.is_pressed("a"):
        t.left(10)
    if keyboard.is_pressed("s"):
        t.backward(10)
    if keyboard.is_pressed("d"):
        t.right(10)
        
