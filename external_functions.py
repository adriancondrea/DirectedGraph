from directed_graph import DirectedGraph
from random import randint
from copy import deepcopy


def read_graph(filename='graph.txt'):
    file = open(filename, 'r')
    # read the first line containing the number of vertices and number of edges
    line = file.readline()
    # remove the newline from the end of the string and splitting its parameters
    line = line.strip('\n')
    line = line.split(' ')
    if len(line) != 2:
        raise ValueError('invalid number of vertices and edges')
    vertices = int(line[0])
    edges = int(line[1])
    # create a directed graph with given vertices
    graph = DirectedGraph(vertices)
    for i in range(edges):
        edge = file.readline()
        edge = edge.strip('\n')
        edge = edge.split(' ')
        if len(edge) != 3:
            raise ValueError('invalid line in file!')
        start_vertex = int(edge[0])
        end_vertex = int(edge[1])
        cost = int(edge[2])
        graph.add_edge(start_vertex, end_vertex, cost)
    file.close()
    return deepcopy(graph)


def write_graph(graph, filename):
    """
    writes the graph given as parameter to the file filename.
    prerequisites: graph must have vertices from 0 to n - 1, where n is the number of vertices.
    :param graph:
    :param filename:
    :return:
    """
    file = open(filename, "w")
    file.write(str(graph.get_number_of_vertices()) + ' ' + str(graph.get_number_of_edges()) + '\n')
    costs = graph.get_costs()
    for vertex1, vertex2 in costs:
        file.write(str(vertex1) + ' ' + str(vertex2) + ' ' + str(costs[(vertex1, vertex2)]) + '\n')
    file.close()


def create_random_graph(vertices, edges):
    """
    creates random graph with the number of vertices and edges given.
    :param vertices: number of vertices
    :param edges: number of edges
    :return:
    """
    graph = DirectedGraph(vertices)
    number_of_edges = 0
    while number_of_edges < edges:
        x = randint(0, vertices - 1)
        y = randint(0, vertices - 1)
        if not graph.is_edge_between(x, y):
            graph.add_edge(x, y, randint(0, 1000))
            number_of_edges += 1
    return deepcopy(graph)
