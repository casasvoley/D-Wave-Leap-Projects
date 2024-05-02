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

def build_graph_from_nodes_and_edges(nodes, edges):

    # Set up graph.
    graph = networkx.Graph()
    if isinstance(nodes, dict):
        graph.add_nodes_from(nodes.keys())
    else:
        graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    return graph, nodes, edges

def build_graph_from_adjacency_matrix(adjacency_matrix):
    
    num_nodes = len(adjacency_matrix)
    nodes = list(range(num_nodes))
    
    numpy_matrix = numpy.matrix(adjacency_matrix)
    rows, cols = numpy.where(numpy_matrix == 1)
    edges = list(zip(rows.tolist(), cols.tolist()))
    
    graph, nodes, edges = build_graph_from_nodes_and_edges(nodes, edges)

    return graph, nodes, edges

def draw_graph(adjacency_matrix=None, nodes=None, edges=None, figure_width=15, figure_height=10,
               highlighted_nodes=[], highlighted_edges=[],
               highlighted_nodes_color='#fcba03', regular_nodes_color='#4287f5',
               highlighted_nodes_size=500, regular_nodes_size=100,
               highlighted_nodes_show_label=True, regular_nodes_show_label=False,
               highlighted_edges_color='#fcba03', regular_edges_color='#4287f5',
               highlighted_edges_width=5, regular_edges_width=1):

    if adjacency_matrix is not None:
        graph, nodes, edges = build_graph_from_adjacency_matrix(adjacency_matrix)
    else:
        graph, nodes, edges = build_graph_from_nodes_and_edges(nodes, edges)

    # Configure nodes and edges.
    node_color, node_size, node_labels = get_node_parameters(
        graph, highlighted_nodes,
        highlighted_nodes_color, regular_nodes_color,
        highlighted_nodes_size, regular_nodes_size,
        highlighted_nodes_show_label, regular_nodes_show_label
    )
    edge_color, edge_width = get_edge_parameters(
        graph, highlighted_edges,
        highlighted_edges_color, regular_edges_color,
        highlighted_edges_width, regular_edges_width
    )
        
    # Visualize graph.
    pyplot.figure(figsize=(figure_width, figure_height))
    if isinstance(nodes, dict):
        networkx.draw(
            graph,
            pos=nodes,
            node_color=node_color,
            node_size=node_size,
            labels=node_labels,
            edge_color=edge_color,
            width=edge_width
        )
    else:
        networkx.draw_circular(
            graph,
            node_color=node_color,
            node_size=node_size,
            labels=node_labels,
            edge_color=edge_color,
            width=edge_width
        )

    pyplot.show()

def get_node_parameters(graph, highlighted_nodes,
                        highlighted_nodes_color, regular_nodes_color,
                        highlighted_nodes_size, regular_nodes_size,
                        highlighted_nodes_show_label, regular_nodes_show_label):

    degrees = dict(graph.degree)

    node_color = [
        highlighted_nodes_color if node in highlighted_nodes else regular_nodes_color
        for node in graph.nodes()
    ]
    node_size = [
        highlighted_nodes_size * degrees[node] if node in highlighted_nodes
        else regular_nodes_size * degrees[node]
        for node in graph.nodes()
    ]
    node_labels = {
        node: node if (
            (highlighted_nodes_show_label and node in highlighted_nodes)
            or (regular_nodes_show_label and node not in highlighted_nodes)
        )
        else ''
        for node in graph.nodes()
    }

    return node_color, node_size, node_labels

def get_edge_parameters(graph, highlighted_edges,
                        highlighted_edges_color, regular_edges_color,
                        highlighted_edges_width, regular_edges_width):

    edge_color = [
        highlighted_edges_color if edge in highlighted_edges else regular_edges_color
        for edge in graph.edges()
    ]
    edge_width = [
        highlighted_edges_width if edge in highlighted_edges else regular_edges_width
        for edge in graph.edges()
    ]

    return edge_color, edge_width
