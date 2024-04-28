#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2021 Rafael Martín-Cuevas Redondo - All Rights Reserved
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.

"""
Auxiliary methods.
"""

from matplotlib import pyplot
import networkx
import numpy

def build_networkx_graph(adjacency_matrix):
    
    numpy_matrix = numpy.matrix(adjacency_matrix)
    
    num_nodes = len(adjacency_matrix)
    nodes = list(range(num_nodes))
    
    rows, cols = numpy.where(numpy_matrix == 1)
    edges = list(zip(rows.tolist(), cols.tolist()))
    
    networkx_graph = networkx.Graph()
    networkx_graph.add_nodes_from(nodes)
    networkx_graph.add_edges_from(edges)

    return networkx_graph

def draw_graph_from_networkx(networkx_graph, path = []):
    
    edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)] \
        + [(path[i+1], path[i]) for i in range(len(path) - 1)]

    networkx.draw(
        networkx_graph,
        node_color=['#fcba03' if node in path else '#4287f5' for node in networkx_graph.nodes()],
        edge_color=['#fcba03' if edge in edges_in_path else '#4287f5' for edge in networkx_graph.edges()],
        width=[5 if edge in edges_in_path else 1 for edge in networkx_graph.edges()],
        with_labels=True
    )
    pyplot.show()


def draw_graph_from_adjacency_matrix(adjacency_matrix, path = []):
    draw_graph_from_networkx(
        build_networkx_graph(adjacency_matrix), path
    )
