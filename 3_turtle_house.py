from turtle import *
shape("turtle")
speed(10)

color("Black")
pensize(7)
right(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)
forward(50)


for count in range(3):
    color("Red")
    pensize(7)
    back(45)
    left(120)

penup()
back(45)
pendown()
right(180)

color("Red")
forward(110)
left(135)
forward(50)
left(45)
forward(90)

penup()
left(120)
forward(45)
right(30)
pendown()

for count in range(4):
    color("Black")
    pensize(7)
    forward(95)
    left(90)

done()
