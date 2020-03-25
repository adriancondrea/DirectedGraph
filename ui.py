from external_functions import read_graph, write_graph, create_random_graph, DirectedGraph
from copy import deepcopy

class Ui:
    def __init__(self):
        """
        initializes an empty graph (no nodes, no edges) and an empty list that stores graph copies
        """
        self._graph = DirectedGraph()
        self._graph_copies = []

    @staticmethod
    def print_menu():
        print('1. Get the number of vertices')
        print('2. Iterate the set of vertices')
        print('3. Check if there is an edge from a given vertex to another')
        print('4. Get the in degree and out degree of a specified vertex')
        print('5. Iterate the set of outbound edges of a specified vertex')
        print('6. Iterate the set of inbound edges of a specified vertex')
        print('7. Get the cost of a given edge')
        print('8. Modify the cost of a given edge')
        print('9. Add an edge')
        print('10.Remove an edge')
        print('11.Add a vertex')
        print('12.Remove a vertex')
        print('13.Create a copy of the graph')
        print('14.Restore a copy of the graph')
        print('15.Read graph from a text file')
        print('16.Write graph to a text file')
        print('17.Create random graph with given number of vertices and edges')
        print('18.Iterate all edges')

    def print_number_of_vertices(self):
        print('The number of vertices is ' + str(self._graph.get_number_of_vertices()))

    def iterate_set_of_vertices(self):
        vertices = self._graph.iterate_vertices()
        for v in vertices:
            print(v)

    def check_edges(self):
        """
        checks if there is an edge between two vertices read from keyboard.
        :return:
        """
        start = int(input('Enter start vertex: '))
        end = int(input('Enter end vertex: '))
        if self._graph.is_edge_between(start, end):
            print('There is an edge from ' + str(start) + ' to ' + str(end))
        else:
            print('There is NO edge from ' + str(start) + ' to ' + str(end))

    def print_degree(self):
        """
        prints the degree of a vertex read from keyboard
        :return:
        """
        vertex = int(input('enter vertex: '))
        in_degree = self._graph.get_in_degree(vertex)
        out_degree = self._graph.get_out_degree(vertex)
        print('The in degree of ' + str(vertex) + ' is ' + str(in_degree))
        print('The out degree of ' + str(vertex) + ' is ' + str(out_degree))

    def iterate_all_edges(self):
        edges = self._graph.iterate_edges()
        for edge in edges:
            print(edge)

    def iterate_outbound_edges(self):
        """
        iterates all outbound edges of vertex read from keyboard. prints them and their cost
        :return:
        """
        vertex = int(input('enter vertex: '))
        try:
            vertices = self._graph.get_outbound_edges(vertex)
        except ValueError as ve:
            print(ve)
            return
        print('Outbound edges from ' + str(vertex) + ':')
        for v in vertices:
            cost = self._graph.get_cost(vertex, v)
            print('Edge from ' + str(vertex) + ' to ' + str(v) + ' with cost ' + str(cost))

    def iterate_inbound_edges(self):
        """
        iterates all inbound edges of vertex read from keyboard, prints them and their cost.
        :return:
        """
        vertex = int(input('enter vertex: '))
        try:
            vertices = self._graph.get_inbound_edges(vertex)
        except ValueError as ve:
            print(ve)
            return
        print('Inbound edges from ' + str(vertex) + ':')
        for v in vertices:
            cost = self._graph.get_cost(v, vertex)
            print('Edge from ' + str(v) + ' to ' + str(vertex) + ' with cost ' + str(cost))

    def print_cost(self):
        """
        prints the cost of an edge between two vertices read from keyboard, if the edge exist.
        If the edge does not exist, or vertices are not valid, raise ValueError
        :return:
        the cost of edge, if vertices are valid and the edge exists
        """
        start = int(input('start vertex: '))
        end = int(input('end vertex: '))
        cost = self._graph.get_cost(start, end)
        print('the cost of edge is ' + str(cost))

    def modify_cost_ui(self):
        """
        modify the cost of the edge between two given vertices read from keyboard. If the edge
        does not exist or the vertices are not valid, raise ValueError
        :return:
        """
        start = int(input('start vertex: '))
        end = int(input('end vertex: '))
        new_cost = int(input('new cost:'))
        self._graph.set_cost(start, end, new_cost)

    def add_edge_ui(self):
        start = int(input('start vertex: '))
        end = int(input('end vertex: '))
        cost = int(input('cost:'))
        self._graph.add_edge(start, end, cost)

    def remove_edge_ui(self):
        start = int(input('start vertex: '))
        end = int(input('end vertex: '))
        self._graph.remove_edge(start, end)

    def add_vertex_ui(self):
        self._graph.add_vertex()

    def remove_vertex_ui(self):
        vertex = int(input('vertex: '))
        self._graph.remove_vertex(vertex)

    def copy_graph_ui(self):
        """
        saves a deepcopy of the graph in the list of graph copies
        :return:
        """
        self._graph_copies.append(deepcopy(self._graph))

    def restore_graph_ui(self):
        """
        restores the state of the graph from a previous copy made. If there is at least one copy to restore
        from
        :return:
        """
        if len(self._graph_copies) == 0:
            print('No copies to restore!')
            return
        # the last made copy is restored in graph
        self._graph = self._graph_copies.pop(-1)

    def read_graph_ui(self):
        """
        reads graph from a file whose name is given from keyboard.
        """
        filename = input('enter filename: ')
        try:
            self._graph = read_graph(filename)
        except FileNotFoundError:
            print('invalid filename! ')


    def write_graph_ui(self):
        """
        writes the current state of the graph into a file
        :return:
        """
        filename = input('enter name of the file to save to: ')
        write_graph(self._graph, filename)


    def create_random_graph_ui(self):
        vertices = int(input('number of vertices: '))
        edges = int(input('number of edges: '))
        self._graph = create_random_graph(vertices, edges)

    def run(self):
        commands = {'1': self.print_number_of_vertices, '2': self.iterate_set_of_vertices, '3': self.check_edges,
                    '4': self.print_degree, '5': self.iterate_outbound_edges, '6': self.iterate_inbound_edges,
                    '7': self.print_cost, '8': self.modify_cost_ui, '9': self.add_edge_ui, '10': self.remove_edge_ui,
                    '11': self.add_vertex_ui, '12': self.remove_vertex_ui, '13': self.copy_graph_ui,
                    '14': self.restore_graph_ui, '15': self.read_graph_ui, '16': self.write_graph_ui,
                    '17': self.create_random_graph_ui, '18': self.iterate_all_edges}
        while True:
            self.print_menu()
            command = input('> ')
            if command in commands:
                try:
                    commands[command]()
                except ValueError as ve:
                    print(ve)
            else:
                print('invalid command!')
