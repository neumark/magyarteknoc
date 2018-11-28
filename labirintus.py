#!/usr/bin/python
# -*- coding: utf-8 -*-

from google.cloud import firestore
from magyarteknoc import *


def get_blocks(drawing):
    # Add a new document
    db = firestore.Client()
    doc_ref = db.collection(u'drawings').document(drawing)
    return [[int(s) for s in k.split("_")] for k,v in doc_ref.get().to_dict().get(u"blocks").items() if v == u"yellow"]

scale = 6
rajzoló.rajzolj("minecraft")
[original_x, original_y, original_z] = rajzoló.hol_vagyok()
for read_x, read_z in get_blocks(u'-LSQ2P5FDuVHvpB0FKPp'):
    final_x = original_x + scale * read_x
    final_z = original_z + scale * read_z
    #print(final_x, final_z)
    rajzoló.ugorj(final_x, original_y, final_z)
    #rajzoló.menj_előre(1)
    #rajzoló.ugorj(final_x, final_y, original_z)
    #print(rajzoló.hol_vagyok())
    rajzoló.tégla(scale, scale, scale)

# x, y is not what we want