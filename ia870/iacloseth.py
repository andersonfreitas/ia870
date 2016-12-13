# -*- encoding: utf-8 -*-
# Module iacloseth

from __future__ import absolute_import
from numpy import *

def iacloseth(f, b=None):
    from .iasubm import iasubm
    from .iaclose import iaclose
    from .iasecross import iasecross
    if b is None:
        b = iasecross()

    y = iasubm( iaclose(f,b), f)
    return y

