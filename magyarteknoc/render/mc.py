#!/usr/bin/python
__all__ = ['RenderBackend']

from mineturtle import Turtle
from .. import api

class MyTurtle(Turtle):
    def __init__(self,mc=None):
        super(MyTurtle, self).__init__(mc)


class RenderBackend(api.IRenderBackend):

    def __init__(self):
        self.t = MyTurtle()

    def forward(self, length=1):
        self.t.go(length)

    def right(self, angle):
        self.t.right(angle)

    def left(self, angle):
        self.t.left(angle)
