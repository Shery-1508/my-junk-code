from shutil import move
import turtle

PEPERONI_POSITIONS = [ 
    [35,35],
    [70,80],
    [-35,0],
    [-20,-25],
    [15,-5],
    [-30,115],
    [10,110]

]

scren = turtle.Screen()
scren.bgcolor("grey")
scren.title("Pizza try")

mypen = turtle.Turtle()
mypen.shape("circle")
mypen.pensize(5)

def movepen(x,y):
    mypen.penup()
    mypen.goto(x,y)
    mypen.pendown()


def drawcircle(radius,stroke_color,fill_color):
    mypen.color(stroke_color)
    mypen.fillcolor(fill_color)
    mypen.begin_fill()
    mypen.circle(radius)
    mypen.end_fill()


movepen(0,-80)
drawcircle(150,"#C59142","#dba24a")
movepen(0,-50)
drawcircle(120,"#e12301","#e1d800")

for location in PEPERONI_POSITIONS:
    movepen(location[0],location[1])
    drawcircle(10,"#900000","#ce0000")


movepen(0,70)
mypen.color("grey")

for x in range(0,4):
    mypen.penup()
    mypen.forward(150)
    mypen.pendown()
    mypen.backward(300)
    mypen.penup()
    mypen.forward(150)
    mypen.left(45)


turtle.done()

# import turtle
# from matplotlib.ft2font import BOLD

# from numpy import True_

# ss = int(turtle.textinput("msg","Value"))

# laptopshery = 205.02751384 
# Sherymob = 223.59863104

# doge = ss*0.02076412

# turtle.write(f"DOGE : {doge}",font=("Times New Roman",20,"bold"),align="right")

# turtle.done()