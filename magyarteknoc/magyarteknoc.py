#!/usr/bin/python
# -*- coding: utf-8 -*-
__all__ = ['rajzoló']

import sys
from .api import MagyarTeknőc
from . import render

backends = {'papír': render.TurtleRenderBackend()}

if render.MCRenderBackend is not None:
    try:
        backends['minecraft'] = render.MCRenderBackend()
    except:
        e = sys.exc_info()[1]
        print("Nem tudtam a minecraft-hez kapcsolódni: %s" % str(e))



rajzoló = MagyarTeknőc(backends)
