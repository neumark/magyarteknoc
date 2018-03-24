#!/usr/bin/python
# -*- coding: utf-8 -*-
__all__ = ['rajzoló']

from .api import MagyarTeknőc
from . import render

rajzoló = MagyarTeknőc({
    'papír': render.turtle_backend(),
    'minecraft': render.mc_backend()
    })
