#!/usr/bin/python
# -*- coding: utf-8 -*-

from mineturtle import Turtle
global t
t = Turtle()
t.angle(0)

def menj_előre(hány_lépést=1):
    t.go(hány_lépést)

def fordulj_jobbra(hányszor=1):
    for i in range(0, hányszor):
        t.right(90)

def fordulj_balra(hányszor=1):
    for i in range(0, hányszor):
        t.left(90)

def parancsok():
    return dir()
