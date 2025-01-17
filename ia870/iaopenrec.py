# -*- encoding: utf-8 -*-
# Module iaopenrec

from __future__ import absolute_import
from numpy import *
from .iasecross import iasecross

def iaopenrec(f, bero=iasecross(), bc=iasecross()):
    from .iainfrec import iainfrec
    from .iaero import iaero

    return iainfrec( iaero(f,bero),f,bc)

