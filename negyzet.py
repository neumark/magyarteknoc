#!/usr/bin/python
# -*- coding: utf-8 -*-

from magyarteknoc import *

rajzoló.nagyíts(6)


def egy_ismetles():
    rajzoló.menj_előre(1)
    rajzoló.fordulj_balra()
    rajzoló.menj_előre(4)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(4)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(3)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(2)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(1)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(1)
    rajzoló.fordulj_balra()
    rajzoló.menj_előre(1)
    rajzoló.fordulj_balra()
    rajzoló.menj_előre(2)
    rajzoló.fordulj_balra()
    rajzoló.menj_előre(3)
    rajzoló.fordulj_balra()
    rajzoló.menj_előre(3)


for oldalhossz in range(0,10):
    for oldal in range(0, oldalhossz):
        egy_ismetles()
    rajzoló.fordulj_jobbra()


while True:
    pass

