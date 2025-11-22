#Activity-1
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().steup(300,400)
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0/(num_sides)
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()

#Activity-2
turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
board.forward(100)

board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(90)
board.forward(100)

board.right(12)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()

##Activity-3
my_wn = turtle.Screen()
my_wn.bgcolor("lightgreen")
my_wn.title("Hello.")
my_pen = turtle.Turtle()
size=0
while True:
    for i in range(4):
        my_pen.fd(size+1)
        my_pen.left(90)
        size= size-5
       size= size+1
