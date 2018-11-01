#!/usr/bin/python
# -*- coding: utf-8 -*-

from magyarteknoc import *

<<<<<<< HEAD
rajzoló.rajzolj("papír")
rajzoló.nagyítás(10)



def egy_szakasz(szakasz_hossz=1):
    for ismétlés in range(1, szakasz_hossz):
        rajzoló.menj_előre(1)
        rajzoló.fordulj_balra()
        rajzoló.menj_előre(1)
        rajzoló.fordulj_jobbra()
        rajzoló.menj_előre()
        rajzoló.fordulj_jobbra()
        rajzoló.menj_előre(1)
        rajzoló.fordulj_balra()

for oldal_hosszúság in range(4,40,2):
    print("oldal hosszúság %s" % oldal_hosszúság)
    egy_szakasz(oldal_hosszúság)
    rajzoló.fordulj_jobbra()

while True:
    pass
=======
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

>>>>>>> 92bde9a5d3f1cdc5b265e538412a4e5e1f6b2a89
