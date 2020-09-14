#Pythoncolor.py
import turtle
turtle.setup(500,400,400,400)
turtle.bgcolor("black")
turtle.pensize(2)
colors=["red","yellow","blue","green","orange","purple"]
for i in range(120):
    turtle.color(colors[i % 6])
    turtle.forward(i * 2)
    turtle.left(61)
turtle.done()

               
