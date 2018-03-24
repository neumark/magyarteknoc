#!/usr/bin/python
__all__ = ['RenderBackend']

from .. import api
import turtle

class RenderBackend(api.IRenderBackend):

    def __init__(self):
        pass

    def forward(self, length):
        turtle.forward(length)

    def right(self, angle):
        turtle.right(angle)

    def left(self, angle):
        turtle.left(angle)
