# -*- encoding: utf-8 -*-
# Module iasetrans

from __future__ import absolute_import
from numpy import *

def iasetrans(Bi, t):
    from .iamat2set import iamat2set
    from .iaset2mat import iaset2mat


    x,v=iamat2set(Bi)
    Bo = iaset2mat((x+t,v))
    Bo = Bo.astype(Bi.dtype)

    return Bo

