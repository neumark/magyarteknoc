#!/usr/bin/python
# -*- coding: utf-8 -*-

from magyarteknoc import *

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

