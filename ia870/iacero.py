# -*- encoding: utf-8 -*-
# Module iacero

from __future__ import absolute_import
from numpy import *
from .iasecross import iasecross
from six.moves import range

def iacero(f, g, b=iasecross(), n=1):
    from .iaunion import iaunion
    from .iaero import iaero
    from .iaisequal import iaisequal

    y = iaunion(f,g)
    for i in range(n):
        aux = y
        y = iaunion( iaero(y,b),g)
        if iaisequal(y,aux): break
    return y

