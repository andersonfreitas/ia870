# -*- encoding: utf-8 -*-
# Module iacdil

from __future__ import absolute_import
from numpy import *
from .iasecross import iasecross
from six.moves import range

def iacdil(f, g, b=iasecross(), n=1):
    from .iaintersec import iaintersec
    from .iadil import iadil
    from .iaisequal import iaisequal

    y = iaintersec(f,g)
    for i in range(n):
        aux = y
        y = iaintersec( iadil(y,b),g)
        if iaisequal(y,aux): break
    return y

