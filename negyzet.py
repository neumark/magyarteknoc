#!/usr/bin/python
# -*- coding: utf-8 -*-

from magyarteknoc import *

rajzoló.nagyíts(6)

for oldalhosszúság in range(1, 64, 4):
    rajzoló.menj_előre(oldalhosszúság)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(oldalhosszúság)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(oldalhosszúság)
    rajzoló.fordulj_jobbra()
    rajzoló.menj_előre(oldalhosszúság)
