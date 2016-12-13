# -*- encoding: utf-8 -*-
# Module iaareaclose

from __future__ import absolute_import
from numpy import *
from .iasecross import iasecross

def iaareaclose(f, a, Bc=iasecross()):
    from .ianeg import ianeg
    from .iaareaopen import iaareaopen

    y = ianeg( iaareaopen( ianeg(f),a,Bc))
    return y

