# -*- encoding: utf-8 -*-
# Module iacloserec

from __future__ import absolute_import
from numpy import *
from .iasecross import iasecross

def iacloserec(f, bdil=iasecross(), bc=iasecross()):
    from .iasuprec import iasuprec
    from .iadil import iadil

    return iasuprec( iadil(f,bdil),f,bc)

