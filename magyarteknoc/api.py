#!/usr/bin/python
# -*- coding: utf-8 -*-

class IRenderBackend(object):

    def forward(self, length):
         raise NotImplementedError()

    def left(self, angle):
         raise NotImplementedError()

    def right(self, angle):
         raise NotImplementedError()

class MagyarTeknőc(object):
    def __init__(self, render_backends):
        self.render_backends = render_backends
        self.rajzolj()
        
    def rajzolj(self, ide='papír'):
        self.current_backend = self.render_backends[ide]

    def menj_előre(self, hány_lépést=1):
        self.current_backend.forward(hány_lépést)

    def fordulj_jobbra(self, fok=90):
        self.current_backend.right(fok)

    def fordulj_balra(self, fok=90):
        self.current_backend.left(fok)
