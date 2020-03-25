import unittest
from external_functions import *

graph = read_graph("graph.txt")


class test_directed_graph(unittest.TestCase):
    def test_iterate_vertices(self):
        vertices = graph.iterate_vertices()
        index = 0
        for vertex in vertices:
            assert vertex == index
            index += 1

    def test_iterate_edges(self):
        edges = graph.iterate_edges()
        number_of_edges = 0
        list_of_edges = [(0, 0), (0, 1), (1, 2), (2, 1), (1, 3), (2, 3)]
        for edge in edges:
            assert edge in list_of_edges
            number_of_edges += 1
        assert number_of_edges == len(list_of_edges)

    def test_valid_vertex(self):
        assert graph.valid_vertex(1) and not graph.valid_vertex(10)

    def test_get_number_of_vertices(self):
        assert graph.get_number_of_vertices() == 5

    def test_get_number_of_edges(self):
        assert graph.get_number_of_edges() == 6

    def test_is_edge_between(self):
        assert graph.is_edge_between(0, 1) and not graph.is_edge_between(3, 3)
        try:
            graph.is_edge_between(55, 55)
            assert False
        except ValueError:
            assert True

    def test_get_in_degree(self):
        assert graph.get_in_degree(0) == 1
        try:
            graph.get_in_degree(100)
            assert False
        except ValueError:
            assert True

    def test_get_out_degree(self):
        assert graph.get_out_degree(0) == 2
        try:
            graph.get_out_degree(100)
            assert False
        except ValueError:
            assert True

    def test_add_edge(self):
        try:
            graph.add_edge(100, 100)
            assert False
        except ValueError:
            assert True
        graph.add_edge(4, 4, 4)
        assert graph.is_edge_between(4, 4)
        graph.remove_edge(4, 4)

    def test_remove_edge(self):
        try:
            graph.remove_edge(100, 100)
            assert False
        except ValueError:
            assert True
        try:
            graph.remove_edge(4, 4)
            assert False
        except ValueError:
            assert True
        graph.remove_edge(0, 0)
        assert not graph.is_edge_between(0, 0)
        graph.add_edge(0, 0, 1)

    def test_get_outbound_edges(self):
        edges = graph.get_outbound_edges(0)
        number_of_edges = 0
        for _ in edges:
            number_of_edges += 1
        assert number_of_edges == 2

    def test_get_cost(self):
        assert graph.get_cost(0, 0) == 1
        try:
            graph.get_cost(100, 100)
            assert False
        except ValueError:
            assert True

    def test_set_cost(self):
        try:
            graph.set_cost(100, 100, 100)
            assert False
        except ValueError:
            assert True
        try:
            graph.set_cost(4, 4, 100)
            assert False
        except ValueError:
            assert True
        graph.set_cost(0, 0, 100)
        assert graph.get_cost(0, 0) == 100
        graph.set_cost(0, 0, 1)

    def test_add_vertex(self):
        graph.add_vertex()
        assert graph.get_in_degree(graph.get_number_of_vertices() - 1) == 0 and graph.get_out_degree(graph.get_number_of_vertices() - 1) == 0
        graph.remove_vertex(graph.get_number_of_vertices() - 1)

    def test_remove_vertex(self):
        try:
            graph.remove_vertex(100)
            assert False
        except ValueError:
            assert True
        graph.add_vertex()
        graph.remove_vertex(5)
        assert not graph.valid_vertex(5)

