import turtle
import random
turtle.colormode(255)
turtle.Screen().setup(950,730)
turtle.Screen().bgcolor(35,58,119)
#畫界線
pen=turtle.Turtle()
pen.color(255,212,31)
pen.pensize(10)
pen.penup()
pen.goto(0,-100)
pen.pendown()
pen.back(500)
pen.forward(1000)
pen.ht()
#星星
t=turtle.Turtle()
turtle.colormode(255)
t.color(255,215,0)
t.pensize(5)
t.ht()
t.penup()
t.goto(-200,200)
i=1
def draw_star():
    t.pendown()
    for i in range(1,6):
        t.forward(100)
        t.right(144)
    t.penup()
    t.goto(t.xcor()+200,t.ycor()+20)
    return
# 烏龜
toga=turtle.Turtle()
toga.shape('turtle')
toga.color(9,185,13)
toga.pencolor(0,128,0)
toga.turtlesize(3,3,3)
toga.penup()
toga.goto(0,-175)
toga.left(90)
for i in range (1,6):
    toga.forward(150)
    cloudy_night=random.choice([True,False])
    print(f"is it cloudy,today?{cloudy_night}")
    turtle.delay(30)
    if(cloudy_night !=True):
        draw_star()
    toga.right(180)
    toga.forward(150)
    turtle.delay(50)
    toga.right(180)
          
