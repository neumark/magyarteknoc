#!/usr/bin/python
# -*- coding: utf-8 -*-

from magyarteknoc import *

for oldalhosszúság in range(1, 64, 4):

    rajzoló.nagyíts(6)
    rajzoló.menj_előre(oldalhosszúság)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(oldalhosszúság)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(oldalhosszúság)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(oldalhosszúság)
