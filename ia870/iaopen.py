# -*- encoding: utf-8 -*-
# Module iaopen

from __future__ import absolute_import
from numpy import *

def iaopen(f, b=None):
    from .iadil import iadil
    from .iaero import iaero
    from .iasecross import iasecross
    if b is None:
        b = iasecross()

    y = iadil( iaero(f,b),b)

    return y

