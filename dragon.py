# https://en.wikipedia.org/wiki/Dragon_curve
import turtle

RADIUS = 6
ARC_DEGREES = 90

def draw(turn_left):
    turtle.circle((-1 if turn_left else 1) * RADIUS, ARC_DEGREES)

turtle.speed(0)
for i in range(0, 10000):
    turn_left = (((i & -i) << 1) & i) != 0
    draw(turn_left)
