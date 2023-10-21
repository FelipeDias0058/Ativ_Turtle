from turtle import *

speed(10)
color("Green")
pensize(14)

lados = 25
angulo = 360 / lados

for count in range(lados):
    forward(lados)
    left(angulo)
