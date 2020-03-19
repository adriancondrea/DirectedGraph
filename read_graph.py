from directed_graph import DirectedGraph


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
    return graph