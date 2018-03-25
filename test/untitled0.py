# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:53:40 2018

@author: 带心情去旅行
"""
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(40)
turtle.pencolor("blue")
turtle.seth(-40)
for i in range(6):
    turtle.circle(40, 80)
    turtle.circle(-10, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
