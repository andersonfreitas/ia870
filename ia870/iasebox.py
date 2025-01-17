# -*- encoding: utf-8 -*-
# Module iasebox

from __future__ import absolute_import
from numpy import *

def iasebox(r=1):
    from .iasesum import iasesum
    from .iabinary import iabinary


    B = iasesum( iabinary([[1,1,1],
                          [1,1,1],
                          [1,1,1]]),r)


    return B

