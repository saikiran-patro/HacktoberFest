#google drive logo
import turtle
t=turtle.Turtle()
a=turtle.Turtle()
s=turtle.Screen()
t.hideturtle()
a.hideturtle()
turtle.title("GOOGLE DRIVE")
s.bgcolor("black")
def parallelogram(length,breadth):
    for i in range(2):
           t.forward(length)
           t.right(120)
           t.forward(breadth)
           t.right(60)         
    


a.color("white")
a.begin_fill()
a.circle(120)
a.end_fill()
t.left(90)
t.penup()
t.forward(50)
t.left(90)
t.backward(70)
t.pendown()
t.color("royal blue")
t.begin_fill()
parallelogram(150,40)
t.end_fill()
t.forward(150)
t.right(60)
t.color("sea green")
t.forward(40)
t.right(60)
t.begin_fill()
parallelogram(150,40)
t.end_fill()
t.forward(150)
t.right(60)
t.color("gold")
t.forward(40)
t.right(60)
t.begin_fill()
parallelogram(150,40)
t.end_fill()

turtle.exitonclick()
