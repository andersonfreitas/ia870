# -*- encoding: utf-8 -*-
# Module iainterot

from __future__ import absolute_import
from numpy import *
from .upper import upper

def iainterot(Iab, theta=45, DIRECTION="CLOCKWISE"):
    from .iase2hmt import iase2hmt
    from .iaserot import iaserot


    DIRECTION = upper(DIRECTION)
    A,Bc = Iab
    if DIRECTION != 'CLOCKWISE':
        theta = 360 - theta
    Irot = iase2hmt( iaserot(A, theta),
                    iaserot(Bc,theta))


    return Irot

