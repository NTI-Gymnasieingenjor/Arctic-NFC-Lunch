import turtle
import tkinter as TK
import time
from typing import List


class UI():

    def __init__(self):
        # Gets the TKinter canvas and its upper window to be able to change TK window properties
        root = turtle.getturtle()._screen.getcanvas().winfo_toplevel()
        # Shows the window in fullscreen
        root.attributes('-fullscreen', True)
        # Shows the window
        turtle.getscreen()
        turtle.hideturtle()
        # The speed is set to 20,
        # to minimize delay between drawing texts
        turtle.speed(20)

    def clear(self):
        # Clears the window to not draw other screens over the current one
        turtle.clear()

    def idleScreen(self):
        self.clear()
        turtle.bgcolor("white")
        turtle.color("black")
        turtle.write("Vänligen skanna din tagg.", move=False, align="center", font=("Arial", 52, "bold"))
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

    def onTime(self):
        self.clear()
        turtle.bgcolor("green")
        turtle.color("white")
        turtle.write("Välkommen in!", move=False, align="center", font=("Arial", 52, "bold"))
        time.sleep(0.8)
        # Displays the idle screen after 0.8 seconds to be able to read the message
        self.idleScreen()

    def wrongTime(self, times: List[str]):
        print(times)
        self.clear()
        turtle.bgcolor("red")
        turtle.color("white")
        turtle.write("Du har inte lunch nu!", move=False, align="center", font=("Arial", 52, "bold"))
        turtle.penup()
        turtle.goto(0, -150)
        turtle.pendown()
        turtle.write("Din lunch är mellan: " + times[1] + "-" + times[2] +
                     ".", move=False, align="center", font=("Arial", 28, "bold"))
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        time.sleep(2)
        self.idleScreen()

    def invalidTag(self):
        self.clear()
        turtle.bgcolor("red")
        turtle.color("white")
        turtle.write("Din tagg är ogiltig, använd en giltig tagg!",
                     move=False, align="center", font=("Arial", 52, "bold"))
        turtle.penup()
        turtle.goto(0, -150)
        turtle.pendown()
        turtle.write("Se till att skanna taggen separat från andra läsbara kort.",
                     move=False, align="center", font=("Arial", 28, "bold"))
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        time.sleep(3.5)
        self.idleScreen()
