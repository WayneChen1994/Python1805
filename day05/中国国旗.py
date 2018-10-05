#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen

'''
使用turtle模块画一个中国国旗
'''
import turtle

turtle.begin_fill()
turtle.fillcolor("red")

for x in range(2):
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)

turtle.end_fill()

turtle.up()
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(20)
turtle.down()

turtle.begin_fill()
turtle.fillcolor("yellow")

for x in range(5):
    turtle.forward(20)
    turtle.left(72)
    turtle.forward(20)
    turtle.right(144)

turtle.end_fill()

turtle.up()
turtle.forward(60)
turtle.left(90)
turtle.forward(30)
turtle.right(144)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
for x in range(5):
    turtle.forward(7)
    turtle.left(72)
    turtle.forward(7)
    turtle.right(144)
turtle.end_fill()


turtle.up()
turtle.forward(25)
turtle.left(36)
turtle.down()

turtle.begin_fill()
turtle.fillcolor("yellow")
for x in range(5):
    turtle.forward(7)
    turtle.left(72)
    turtle.forward(7)
    turtle.right(144)
turtle.end_fill()

turtle.up()
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.down()

turtle.begin_fill()
turtle.fillcolor("yellow")
for x in range(5):
    turtle.forward(7)
    turtle.left(72)
    turtle.forward(7)
    turtle.right(144)
turtle.end_fill()

turtle.up()
turtle.right(90)
turtle.forward(10)
turtle.down()

turtle.begin_fill()
turtle.fillcolor("yellow")
for x in range(5):
    turtle.forward(7)
    turtle.left(72)
    turtle.forward(7)
    turtle.right(144)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
