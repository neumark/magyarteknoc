#!/usr/bin/python
# -*- coding: utf-8 -*-

from magyarteknoc import *

rajzoló.rajzolj("minecraft")

for i in range(4):
    rajzoló.tégla(10, 10, 10)
    rajzoló.tégla(10, 4, 20)
    rajzoló.tégla(10, 10, 10)
    rajzoló.tégla(10, 4, 20)
    rajzoló.tégla(10, 10, 10)
    rajzoló.fordulj_jobbra()

def betu():
    rajzoló.szélesség(10)
    rajzoló.nagyítás(15)
    rajzoló.menj_előre(12)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(5)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre()
    rajzoló.fordulj_balra()
    rajzoló.menj_előre()
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(4)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre()
    rajzoló.fordulj_balra()
    rajzoló.menj_előre()
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(5)

# hogy ne tűnjön el az ablak... erre kell majd valami kultúráltabb megoldás...
#import turtle
#turtle.exitonclick()
