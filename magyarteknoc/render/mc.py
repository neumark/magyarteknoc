#!/usr/bin/python
__all__ = ['MCRenderBackend']

from mineturtle import Turtle, block
from .. import api

class MyTurtle(Turtle):
    def __init__(self,mc=None):
        super(MyTurtle, self).__init__(mc)


class MCRenderBackend(api.BaseBackend):

    def __init__(self):
        self.t = MyTurtle()
        self.t.pendelay(0)
        self.scale = 1
        #self.t.angle(0)  # align to grid
        #self.t.mc.postToChat("most rajzolok!")
        #self.t.positionIn()
        #self.t.gridalign()
        #self.t.verticalangle(0)

    def get_position(self):
        return [self.t.position.x, self.t.position.y, self.t.position.z]

    def forward(self, length=1):
        self.t.go(length * self.scale)

    def goto(self, x, y, z):
        self.t.penup()
        self.t.goto(x, y, z)
        self.t.pendown()

    def right(self, angle):
        self.t.right(angle)

    def left(self, angle):
        self.t.left(angle)

    def set_scale(self, scale):
        super(MCRenderBackend, self).set_scale(scale)

    def set_width(self, width):
        super(MCRenderBackend, self).set_width(width)
        self.t.penwidth(width)

    def _rect(self, width, height, block_type):
        self.t.penblock(block_type)
        lengths = [width, height]
        self.t.startface()
        for i in range(4):
            self.t.go(lengths[i % 2])
            self.t.yaw(90)
        self.t.endface()

    def brick(self, width, height, depth):
        self.t.push()
        self._rect(depth, width, block.STONE_BRICK)
        self.t.roll(-90)
        self._rect(depth, height, block.STONE_BRICK)
        self.t.roll(90)
        self.t.pitch(90)
        self._rect(height, width, block.STONE_BRICK)
        self.t.pitch(-90)
        # back in original position

        self.t.penup()
        self.t.go(depth)
        self.t.yaw(90)
        self.t.go(width)
        self.t.pitch(90)
        self.t.go(height)
        self.t.pitch(-90)
        self.t.yaw(90)
        self.t.pitch(-90)

        self.t.pendown()
        self._rect(height, width, block.STONE_BRICK)
        self.t.roll(-90)
        self._rect(height, depth, block.STONE_BRICK)
        self.t.roll(90)
        self.t.pitch(90)
        self._rect(depth, width, block.STONE_BRICK)
        self.t.pop()

        #self._jump_ahead(depth)

    def _jump_ahead(self, block_count):
        self.t.penup()
        self.t.go(block_count)
        self.t.pendown()
