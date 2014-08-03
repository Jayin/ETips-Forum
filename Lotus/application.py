# -*- coding: utf-8 -*-
version = '1.0.0'
author  = 'Jayin Ton'
#import every thing here

from .app import app, db

#in-order:M-V-C

from .model import user
from .controller import common

