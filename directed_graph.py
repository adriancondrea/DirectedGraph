class DirectedGraph:
    """
    Repreents a directed graph with costs, storing the list of incoming and outgoing vertices for each vertex, and a
    list of costs
    """
    def __init__(self, n=0):
        """
        creates a graph with n vertices, from 0 to n - 1
        :param n: number of vertices
        implicitly n = 0 -> creates an empty graph
        """
        # for each vertex v, we create a set of incoming nodes (nodes that have an edge ending in v) and a list for
        # outgoing nodes (nodes that have an edge starting in v).
        self._inbound = {}
        self._outbound = {}
        # creating a dictionary for storing costs. For each tuple (a, b) where a and b are vertices in our graph, we
        # associate an integer
        self._costs = {}
        # initialize the keys from 0 to n - 1, representing the vertices, with empty lists, in both incoming and
        # outgoing dictionaries
        for i in range(n):
            self._inbound[i] = []
            self._outbound[i] = []

    def iterate_vertices(self):
        """Returns a generator that parses the vertices"""
        for vertex in self._outbound.keys():
            yield vertex

    def valid_vertex(self, vertex):
        """
        checks if a vertex is valid (it is in the list of vertices)
        :return: True if it is valid, False otherwise
        """
        return vertex in self._inbound.keys()

    def get_number_of_vertices(self):
        """
        :return: the number of vertices of the graph
        """
        return len(self._outbound.keys())

    
    def is_edge_between(self, start, end):
        """
        checks if there is an edge between start and end, checking if start and end are valid vertices. If they are
        not valid, we raise a ValueError
        :param start:
        :param end:
        :return:
        """
        if not self.valid_vertex(start) or not self.valid_vertex(end):
            raise ValueError('invalid start / end')
        return end in self._outbound[start]

    def get_in_degree(self, vertex):
        """
        returns the in degree of given vertex. If the vertex is not valid, we raise ValueError
        :param vertex: given vertex
        :return: the in degree of vertex
        """
        if not self.valid_vertex(vertex):
            raise ValueError('invalid vertex!')
        return len(self._inbound[vertex])

    def get_out_degree(self, vertex):
        """
        returns the out degree of given vertex. If the vertex is not valid, we raise ValueError
        :param vertex: given vertex
        :return: the out degree of given vertex
        """
        if not self.valid_vertex(vertex):
            raise ValueError('invalid vertex!')
        return len(self._outbound[vertex])

    def add_edge(self, start, end, cost):
        """
        adds an edge between start and end with given cost. If start and and are not valid vertices, we raise a
        valueError. If the edge already exists, we raise a ValueError
        :param start:
        :param end:
        :param cost:
        :return:
        """
        if not self.valid_vertex(start) or not self.valid_vertex(end):
            raise ValueError('invalid vertices!')
        if (start, end) in self._costs.keys():
            raise ValueError('edge already exists!')
        self._outbound[start].append(end)
        self._inbound[end].append(start)
        self._costs[(start, end)] = cost

    def remove_edge(self, start, end):
        """
        removes the edge between start and end. If start and end are not valid vertices, raise ValueError. If the
        edge does not exist, raise ValueError
        :param start:
        :param end:
        :return:
        """
        if not self.valid_vertex(start) or not self.valid_vertex(end):
            raise ValueError('invalid vertices!')
        if (start, end) not in self._costs.keys():
            raise ValueError('edge does not exist!')
        # delete the key from the dictionary
        del self._costs[(start, end)]
        # delete start from the incoming list of end and end from the outgoing list of start
        self._inbound[end].remove(start)
        self._outbound[start].remove(end)

    def get_outbound_edges(self, vertex):
        """
        returns a generator that parses the outbound edges for vertex. If vertex is not in the
        list of vertices, it raises a ValueError
        :param vertex:
        :return:
        """
        if not self.valid_vertex(vertex):
            raise ValueError('invalid vertex!')
        if len(self._outbound[vertex]) == 0:
            raise ValueError('no outbound edges!')
        for v in self._outbound[vertex]:
            yield v

    def get_inbound_edges(self, vertex):
        """
        returns a generator that parses the inbound edges for vertex. If vertex is not valid, raise
        ValueError
        :param vertex:
        :return:
        """
        if not self.valid_vertex(vertex):
            raise ValueError('invalid vertex!')
        if len(self._inbound[vertex]) == 0:
            raise ValueError('no inbound edges!')
        for v in self._inbound[vertex]:
            yield v

    def get_cost(self, start, end):
        """
        returns the cost of the edge starting from start and ending at end. If start and end are not valid vertices, we
        raise ValueError. If the edge does not exist, we also raise ValueError
        :param start:
        :param end:
        :return:
        """
        if not self.valid_vertex(start) or not self.valid_vertex(end):
            raise ValueError('invalid start or end vertex')
        if (start, end) not in self._costs.keys():
            raise ValueError('Edge does not exist!')
        return self._costs[(start, end)]

    def set_cost(self, start, end, value):
        """
        sets the cost of the edge (start, end) to value. If the edge does not exist, or start and end are not valid
        vertices, raises ValueError
        :param start:
        :param end:
        :param value:
        :return:
        """
        if not self.valid_vertex(start) or not self.valid_vertex(end):
            raise ValueError('invalid start or end vertex')
        if (start, end) not in self._costs.keys():
            raise ValueError('Edge does not exist!')
        self._costs[(start, end)] = value

    def add_vertex(self):
        """
        adds another vertex to the graph. Its index will be the length of the list of keys of incoming vertices, because
        vertices are indexed from 0.
        :return: updates the graph
        """
        vertex = len(self._inbound.keys())
        self._inbound[vertex] = []
        self._outbound[vertex] = []

    def remove_vertex(self, vertex):
        """
        CAN BE OPTIMAL - parse the list of incoming 
        removes given vector from graph and all its instances. Raises ValueError if the vertex does not exist.
        :param vertex:
        :return:
        """
        if not self.valid_vertex(vertex):
            raise ValueError('vertex does not exist!')
        # if it exists, delete the vertex from the list of outbound neighbours of its inbound neighbours and also delete
        # it from the list of inbound neighbours of its outbound neighbours
        for neighbour in self._inbound[vertex]:
            self._outbound[neighbour].remove(vertex)
        for neighbour in self._outbound[vertex]:
            self._inbound[neighbour].remove(vertex)
        # delete the lists of inbound and outbound edges for that vector
        del self._inbound[vertex]
        del self._outbound[vertex]
        keys_to_remove = []
        for i in self._costs.keys():
            if vertex in i:
                keys_to_remove.append(i)

        for k in keys_to_remove:
            del self._costs[k]