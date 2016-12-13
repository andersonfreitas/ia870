# -*- encoding: utf-8 -*-
# Module iacloserecth

from __future__ import absolute_import
from numpy import *
from .iasecross import iasecross

def iacloserecth(f, bdil=iasecross(), bc=iasecross()):
    from .iasubm import iasubm
    from .iacloserec import iacloserec

    y = iasubm( iacloserec(f,bdil,bc), f)
    return y

