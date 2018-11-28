#!/usr/bin/python
__all__ = ['TurtleRenderBackend']

from .. import api
import turtle
from turtle import *

class TurtleRenderBackend(api.BaseBackend):

    def __init__(self):
        pass

    def forward(self, length):
        turtle.forward(length * self.scale)

    def right(self, angle):
        turtle.right(angle)

    def left(self, angle):
        turtle.left(angle)

    def set_color(self, color_value):
        color(color_value)

    def goto(self, x, y):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()

