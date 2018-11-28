#!/usr/bin/python
# -*- coding: utf-8 -*-

from magyarteknoc import *

rajzoló.nagyítás(5)
rajzoló.szín('zöld')


def egy_ismétlés():
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


for hányadik_oldal in range(3, 30):
    for hányadik_szakasz in range(0, hányadik_oldal):
        print("'hányadik oldal' doboz: %s, 'hányadik szakasz' doboz: %s" % (hányadik_oldal, hányadik_szakasz))
        egy_ismétlés()
    rajzoló.fordulj_jobbra()


while True:
    pass
