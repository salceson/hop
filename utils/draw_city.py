#!/usr/bin/python
# -*- coding=utf-8 -*-

__author__ = 'Michał Ciołczyk'

from configuration import Configuration
from matplotlib.pyplot import savefig
import networkx as nx

output_filename = '../map.png'

dist_map = Configuration.distances_map()
vertices = dist_map.keys()

graph = nx.Graph()

for x in vertices:
    graph.add_node(x)

for x in vertices:
    for y in vertices:
        if dist_map[x].get(y) is not None:
            graph.add_edge(x, y)

edges_labels = dict(((u, v), dist_map[u][v]) for (u, v) in graph.edges())
nodes_labels = dict((x, x) for x in vertices)

pos = nx.spectral_layout(graph)
nx.draw(graph, pos, node_size=3500, font_size=16, font_color="white", font_weight="bold", labels=vertices)
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edges_labels, alpha=0.1)
nx.draw_networkx_labels(graph, pos, nodes_labels, font_size=10)
savefig(output_filename)