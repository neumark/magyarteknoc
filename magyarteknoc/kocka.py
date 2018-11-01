# based on glasscube demo
# Code by Alexander Pruss and under the MIT license
#

from mineturtle import *

t = Turtle()
t.turtle(None)
t.pendelay(0)
t.angle(0) # align to grid
t.penblock(block.WOOD)

def face(edge_length):
  t.startface()
  for i in range(4):
    t.go(edge_length)
    t.yaw(90)
  t.endface()

def cube(edge_length):
    for i in range(2):
        face(edge_length)
        t.roll(-90)
        face(edge_length)
        t.roll(90)
        t.pitch(90)
        face(edge_length)
        t.pitch(-90)
        t.penup()
        t.go(edge_length)
        t.yaw(90)
        t.go(edge_length)
        t.pitch(90)
        t.go(edge_length)
        t.pitch(-90)
        t.yaw(90)
        t.pitch(-90)
        t.pendown()

def rect(width, height, block_type):
  t.penblock(block_type)
  lengths = [width, height]
  t.startface()
  for i in range(4):
    t.go(lengths[i % 2])
    t.yaw(90)
  t.endface()


def brick(width, height, depth):
        t.push()
        rect(depth, width, block.WOOL_ORANGE)
        t.roll(-90)
        rect(depth, height, block.WOOL_LIGHT_BLUE)
        t.roll(90)
        t.pitch(90)
        rect(height, width, block.WOOL_BLACK)
        t.pitch(-90)
        # back in original position

        t.penup()
        t.go(depth)
        t.yaw(90)
        t.go(width)
        t.pitch(90)
        t.go(height)
        t.pitch(-90)
        t.yaw(90)
        t.pitch(-90)

        t.pendown()
        rect(height, width, block.WOOL_RED)
        t.roll(-90)
        rect(height, depth, block.WOOL_GREEN)
        t.roll(90)
        t.pitch(90)
        rect(depth, width, block.WOOL_BROWN)
        t.pop()


def jump_ahead(block_count):
    t.penup()
    t.go(block_count)
    t.pendown()

brick(8, 8, 8)

jump_ahead(8)

brick(4, 4, 12)

jump_ahead(12)

brick(8, 8, 8)