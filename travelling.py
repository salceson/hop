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

# Direct
print "Path 1: direct park -> home"

pyhop(state, [('travel', 'me', 'park', 'home')], 3)

# Indirect - via intersections
print "Path 2: indirect park -> home (via intersections)"

pyhop(state, [('travel', 'me', 'park', 'intersection1'),
              ('travel', 'me', 'intersection1', 'intersection2'),
              ('travel', 'me', 'intersection2', 'intersection3'),
              ('travel', 'me', 'intersection3', 'home'),], 3)