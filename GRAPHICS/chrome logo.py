##chrome logo
import turtle
t=turtle.Turtle()
t.speed(100)
m=turtle.Turtle()
m.speed(100)
s=turtle.Screen()
s.bgcolor("black")
t.color("gold")
t.penup()
t.circle(100,340)
t.pendown()
t.begin_fill()
t.circle(100,120)
for i in range(2):
    t.left(77)
    t.forward(100)



t.forward(20)
t.end_fill()
t.left(86)
t.circle(100,120)
###red
t.begin_fill()
t.color("red")
t.circle(100,140)
t.left(77)
t.forward(100)
t.left(115)
t.forward(45)
t.right(78)
t.forward(100)
t.end_fill()
###
t.left(104)
t.circle(100,135)
t.right(2)
##green
t.color("green")
t.begin_fill()
t.circle(100,120)
t.left(90)
t.forward(100)
t.left(60)
t.forward(100)
t.end_fill()
#########
m.penup()
m.color("white")
m.left(90)
m.forward(45)
m.left(-90)
m.pendown()
m.begin_fill()
m.circle(50)
m.end_fill()
m.color("royal blue")
m.left(90)
m.penup()
m.forward(10)
m.pendown()
m.left(90)
m.begin_fill()
m.circle(-40)
m.end_fill()
#####
m.hideturtle()
t.hideturtle()
turtle.exitonclick()
