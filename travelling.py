#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyhop.pyhop import pyhop
from configuration import Configuration
from operators import initialize_methods, initialize_operators

__author__ = 'Michał Ciołczyk'

# States, methods, operators

initialize_operators()
initialize_methods()
state = Configuration.initialize_state()

# Execute pyhop
pyhop(state, None, 3)