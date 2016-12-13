# -*- encoding: utf-8 -*-
# Module ialastero

from __future__ import absolute_import
from numpy import *
from .iasecross import iasecross

def ialastero(f, B=iasecross()):
    from .iaisbinary import iaisbinary
    from .iadist import iadist
    from .iaregmax import iaregmax

    assert iaisbinary(f),'Can only process binary images'
    dt = iadist(f,B)
    y = iaregmax(dt,B)
    return y

