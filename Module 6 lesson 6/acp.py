import turtle

# Draw an equilateral triangle
def draw_triangle():
    turtle.fillcolor("lightblue")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

# Draw a rectangle
def draw_rectangle():
    turtle.fillcolor("lightgreen")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

# Drawing a hexagon
def draw_hexagon():
    turtle.fillcolor("lightcoral")
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(80)
        turtle.left(60)
    turtle.end_fill()

# Set up the screen
turtle.bgcolor("white")  
turtle.speed(1)  

# Draw the shapes
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
draw_triangle()

turtle.penup()
turtle.goto(50, 0)
turtle.pendown()
draw_rectangle()

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
draw_hexagon()

# Finish
turtle.hideturtle()  
turtle.done()