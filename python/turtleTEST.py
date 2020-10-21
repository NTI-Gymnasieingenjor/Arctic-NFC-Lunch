import turtle
import tkinter as TK


class UI():

    def __init__(self):
        root = (turtle.getturtle()
            ._screen
            .getcanvas()
            .winfo_toplevel())
        root.attributes('-fullscreen', True)    
        turtle.getscreen()
        turtle.hideturtle() 
        turtle.speed(20)

    def idleScreen(self):
        turtle.bgcolor("white")
        turtle.color("black")
        turtle.write("Vänligen skanna din tagg.", move=False, align="center", font=("Arial", 52, "bold"))
        turtle.penup()
        turtle.goto(0,-350)
        turtle.pendown()
        turtle.showturtle()
        turtle.right(90)
        turtle.shapesize(16)

    def onTime(self):
        turtle.bgcolor("green")
        turtle.color("white")
        turtle.write("Välkommen in!", move=False, align="center", font=("Arial", 52, "bold"))

    def wrongTime(self):
        turtle.bgcolor("red")
        turtle.color("white")
        turtle.write("Du har inte lunch nu!", move=False, align="center", font=("Arial", 52, "bold"))
        turtle.penup()
        turtle.goto(0,-150)
        turtle.pendown()
        turtle.write("Din lunch är mellan: 12.10-12.30.", move=False, align="center", font=("Arial", 28, "bold"))

    def invalidTag(self):
        turtle.bgcolor("red")
        turtle.color("white")
        turtle.write("Din tagg är ogiltig, använd en giltig tagg!", move=False, align="center", font=("Arial", 52, "bold"))
        turtle.penup()
        turtle.goto(0,-150)
        turtle.pendown()
        turtle.write("Se till att skanna taggen separat från andra läsbara kort.", move=False, align="center", font=("Arial", 28, "bold"))

UI().idleScreen()

TK.mainloop()