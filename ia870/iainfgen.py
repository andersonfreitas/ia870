# -*- encoding: utf-8 -*-
# Module iainfgen

from __future__ import absolute_import
from numpy import *

def iainfgen(f, Iab):
    from .iaunion import iaunion
    from .iadil import iadil
    from .ianeg import ianeg


    A, Bc = Iab
    y = iaunion( iadil(f, A), iadil( ianeg(f), Bc))

    return y

