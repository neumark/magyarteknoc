#!/usr/bin/python
# -*- coding: utf-8 -*-
__all__ = ['rajzoló']

from .api import MagyarTeknőc
from . import render

backends = {'papír': render.turtle_backend()}

if render.mc_backend is not None:
    backends['minecraft'] = render.mc_backend()


rajzoló = MagyarTeknőc(backends)
