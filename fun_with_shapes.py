import turtle

screen = turtle.Screen()
screen.bgcolor("orange")

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(3)

side_length = 100

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(length)
        pen.left(angle)

pen.penup()
pen.goto(-150, 0)
pen.pendown()
pen.color("black")
draw_polygon(4, side_length)

pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("blue")
draw_polygon(3, side_length)

pen.penup()
pen.goto(150, 0)
pen.pendown()
pen.color("green")
draw_polygon(6, side_length)

pen.hideturtle()
turtle.done()
