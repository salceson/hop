#!/usr/bin/python
# -*- coding=utf-8 -*-
__author__ = 'Michał Ciołczyk'

from configuration import Configuration

output_filename = '../map.png'

dist_map = Configuration.distances_map()
vertices = dist_map.keys()
