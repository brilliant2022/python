import turtle
import random
turtle_stamp=turtle.Turtle()
turtle_stamp.shape('turtle')
turtle_stamp.color('green')
turtle.colormode(255)
turtle_stamp.penup()
#turtle_stamp.forward(100)
turtle_stamp.stamp()
paces=5
random_red =50
random_green=50
random_blue=50
i=0
for i in range(50):
    random_red=random.randint(0,255)
    random_green=random.randint(0,255)
    random_blue=random.randint(0,255)
    turtle_stamp.color(random_red,random_green,random_blue)
    turtle_stamp.stamp()
    paces +=3
    turtle_stamp.forward(paces)
    turtle_stamp.right(25)
pen=turtle.Turtle()
pen.write("Turtle's home!",font=("OpenSans",15,"normal"))
