from read_graph import read_graph


class Ui():
    def __init__(self):
        self._graph = read_graph()

    def print_menu(self):
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

    def print_number_of_vertices(self):
        print('The number of vertices is ' + str(self._graph.get_number_of_vertices()))

    def iterate_set_of_vertices(self):
        vertices = self._graph.iterate_vertices()
        for v in vertices:
            print(v)

    def check_edges(self):
        start = input('Enter start vertex: ')
        start = int(start)
        end = input('Enter end vertex: ')
        end = int(end)
        if self._graph.is_edge_between(start, end):
            print('There is an edge from ' + str(start) + ' to ' + str(end))
        else:
            print('There is NO edge from ' + str(start) + ' to ' + str(end))

    def print_degree(self):
        vertex = input('enter vertex: ')
        vertex = int(vertex)
        in_degree = self._graph.get_in_degree(vertex)
        out_degree = self._graph.get_out_degree(vertex)
        print('The in degree of ' + str(vertex) + ' is ' + str(in_degree))
        print('The out degree of ' + str(vertex) + ' is ' + str(out_degree))

    def iterate_outbound_edges(self):
        vertex = input('enter vertex: ')
        vertex = int(vertex)
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
        vertex = input('enter vertex: ')
        vertex = int(vertex)
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
        start = int(input('start vertex: '))
        end = int(input('end vertex: '))
        cost = self._graph.get_cost(start, end)
        print('the cost of edge is ' + str(cost))

    def modify_cost_ui(self):
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

    def run(self):
        commands = {'1': self.print_number_of_vertices, '2': self.iterate_set_of_vertices, '3': self.check_edges,
                    '4': self.print_degree, '5': self.iterate_outbound_edges, '6':self.iterate_inbound_edges,
                    '7': self.print_cost, '8': self.modify_cost_ui, '9': self.add_edge_ui, '10':self.remove_edge_ui,
                    '11': self.add_vertex_ui, '12': self.remove_vertex_ui}
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
