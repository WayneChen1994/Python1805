#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: WayneChen


import turtle

turtle.begin_fill()
turtle.fillcolor("green")
for x in range(3):
    turtle.forward(150)
    turtle.left(120)
turtle.end_fill()

turtle.left(180)
turtle.begin_fill()
turtle.fillcolor("red")
for x in range(5):
    turtle.forward(150)
    turtle.left(144)
turtle.end_fill()

turtle.done()
