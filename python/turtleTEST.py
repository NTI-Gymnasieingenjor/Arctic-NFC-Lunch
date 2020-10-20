import turtle
import tkinter as TK

turtle.getscreen()
turtle.hideturtle()

def onTime():
    turtle.bgcolor("green")
    turtle.color("white")
    turtle.write("Välkommen in!", move=False, align="center", font=("Arial", 52, "bold"))

def wrongTime():
    turtle.bgcolor("red")
    turtle.color("white")
    turtle.write("Du har inte lunch nu!", move=False, align="center", font=("Arial", 52, "bold"))
    turtle.penup()
    turtle.goto(0,-150)
    turtle.pendown()
    turtle.write("Din lunch är mellan: 12.10-12.30.", move=False, align="center", font=("Arial", 28, "bold"))

def invalidTag():
    turtle.bgcolor("red")
    turtle.color("white")
    turtle.write("Din tagg är ogiltig, använd en giltig tagg!", move=False, align="center", font=("Arial", 52, "bold"))
    turtle.penup()
    turtle.goto(0,-150)
    turtle.pendown()
    turtle.write("Se till att skanna taggen separat från andra läsbara kort.", move=False, align="center", font=("Arial", 28, "bold"))


TK.mainloop()