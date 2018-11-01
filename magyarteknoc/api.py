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

class MagyarTeknőc(object):
    def __init__(self, render_backends):
        self.render_backends = render_backends
        # init with default backend
        self.rajzolj()
        
    def rajzolj(self, ide='papír'):
        self.current_backend = self.render_backends[ide]

    def menj_előre(self, lépések_száma=1):
        self.current_backend.forward(lépések_száma)

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
