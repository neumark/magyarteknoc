#!/usr/bin/python
# -*- coding: utf-8 -*-

class BaseBackend(object):

    def __init__(self):
        self.scale = 1
        self.width = 1

    def forward(self, length):
         raise NotImplementedError()

    def left(self, angle):
         raise NotImplementedError()

    def right(self, angle):
         raise NotImplementedError()

    def set_scale(self, scale):
        self.scale = scale

    def set_width(self, width):
        self.width = width

    def set_color(self, color):
        raise NotImplementedError()

    def goto(self, x, y):
        raise NotImplementedError()

    def get_position(self):
        raise NotImplementedError()


class MagyarTeknőc(object):

    SZÍNEK = {
        'fekete': 'black',
        'zöld': 'green'
    }

    def __init__(self, render_backends):
        self.render_backends = render_backends
        # init with default backend
        self.rajzolj()
        
    def rajzolj(self, ide='papír'):
        self.current_backend = self.render_backends[ide]

    def menj_előre(self, lépések_száma=1):
        self.current_backend.forward(lépések_száma)

    def ugorj(self, x, y, z=0):
        self.current_backend.goto(x,y,z)

    def fordulj_jobbra(self, fok=90):
        self.current_backend.right(fok)

    def fordulj_balra(self, fok=90):
        self.current_backend.left(fok)

    def nagyítás(self, nagyítás=1):
        self.current_backend.set_scale(nagyítás)

    def szélesség(self, szélesség=1):
        self.current_backend.set_width(szélesség)

    def tégla(self, szélesség=10, magasság=10, mélység=10):
        self.current_backend.brick(szélesség, magasság, mélység)

    def szín(self, szín='fekete'):
        self.current_backend.set_color(self.SZÍNEK.get(szín))

    def hol_vagyok(self):
        return self.current_backend.get_position()
