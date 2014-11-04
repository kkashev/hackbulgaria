from graph import Graph
import unittest


class TestGraph(unittest.TestCase):
    def test_add_edge(self):
        graph1 = Graph()
        graph1.add_edge('A', 'B')
        self.assertEqual({'A': ['B']}, graph1.graph)

    def test_get_neighbor(self):
        graph1 = Graph()
        graph1.add_edge('A', 'B')
        self.assertEqual(['B'], graph1.get_neighbors_for('A'))

    def test_get_zero_neighbor(self):
        graph1 = Graph()
        graph1.add_edge('A', 'B')

if __name__ == '__main__':
    unittest.main()
