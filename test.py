import unittest
from graph import Graph
from pagerank import pagerank 
import math


class GraphTest(unittest.TestCase):

	def test_add_vertex(self):
		graph = Graph()
		graph.add_vertex(1)
		graph.add_vertex("a")
		graph.add_vertex(0.1)
		self.assertEqual(graph.number_of_vertices(), 3)

	def test_add_edges(self):
		graph = Graph()
		graph.add_vertex(1)
		graph.add_vertex("a")
		graph.add_vertex(0.1)
		graph.add_edge(1, "a")
		graph.add_edge(1, 0.1)
		graph.add_edge(0.1, "a")
		self.assertEqual(len(graph.incoming_vertices(1)), 0)
		self.assertEqual(len(graph.incoming_vertices("a")), 2)
		self.assertEqual(len(graph.incoming_vertices(0.1)), 1)

	def test_add_edge_and_vetex(self):
		graph = Graph()
		graph.add_edge(1, "a")
		graph.add_edge(1, 0.1)
		graph.add_edge(0.1, "a")
		self.assertEqual(len(graph.incoming_vertices(1)), 0)
		self.assertEqual(len(graph.incoming_vertices("a")), 2)
		self.assertEqual(len(graph.incoming_vertices(0.1)), 1)

	def test_remove_vertex(self):
		graph_dict = {"A": {},
					 "B": {"A":{}, "C":{}},
					 "C": {"A": {}},
					 "D": {"A":{}, "B":{}, "C":{}}
					 }		
		graph = Graph(graph_dict)
		graph.remove_vertex("B")

		self.assertEqual(graph.number_of_vertices(), 3)
		self.assertEqual(len(graph.incoming_vertices("A")), 2)
		self.assertEqual(len(graph.incoming_vertices("C")), 1)
		self.assertEqual(len(graph.incoming_vertices("D")), 0)

	def test_remove_non_existent_vertex(self):
		graph = Graph()
		self.assertRaises(KeyError, graph.remove_vertex, "B")

	def test_remove_edge(self):
		graph_dict = {"A": {},
					 "B": {"A":{}, "C":{}},
					 "C": {"A": {}},
					 "D": {"A":{}, "B":{}, "C":{}}
					 }			
		graph = Graph(graph_dict)
		graph.remove_edge("B","A")
		graph.remove_edge("B","C")
		self.assertEqual(graph.number_of_vertices(), 4)
		self.assertEqual(len(graph.incoming_vertices("A")), 2)
		self.assertEqual(len(graph.incoming_vertices("C")), 1)
		self.assertEqual(len(graph.incoming_vertices("D")), 0)		

	def test_remove_nonexistent_edge(self):
		graph = Graph()
		graph.add_vertex("A")
		graph.add_vertex("B")
		self.assertRaises(KeyError, graph.remove_edge, "A", "B")

	def test_in_degree(self):
		graph_dict = {"A": {},
					 "B": {"A":{}, "C":{}},
					 "C": {"A": {}},
					 "D": {"A":{}, "B":{}, "C":{}}
					 }			
		graph = Graph(graph_dict)
		self.assertEqual(graph.in_degree("A"), 3)
		self.assertEqual(graph.in_degree("B"), 1)
		self.assertEqual(graph.in_degree("C"), 2)
		self.assertEqual(graph.in_degree("D"), 0)

	def test_out_degree(self):
		graph_dict = {"A": {},
					 "B": {"A":{}, "C":{}},
					 "C": {"A": {}},
					 "D": {"A":{}, "B":{}, "C":{}}
					 }			
		graph = Graph(graph_dict)
		self.assertEqual(graph.out_degree("A"), 0)
		self.assertEqual(graph.out_degree("B"), 2)
		self.assertEqual(graph.out_degree("C"), 1)
		self.assertEqual(graph.out_degree("D"), 3)

	def test_undirected_add(self):
		graph = Graph(directed=False)
		graph.add_vertex("A")
		graph.add_vertex("B")
		graph.add_edge("A","B")

		self.assertEqual(graph.number_of_vertices(), 2)
		self.assertEqual(len(graph.incoming_vertices("A")), 1)
		self.assertEqual(len(graph.incoming_vertices("B")), 1)


	def test_undirected_remove(self):
		graph_dict = {"A": {"B":{}, "C":{}, "D": {}},
					 "B": {"A":{}, "C":{}, "D": {}},
					 "C": {"A": {}, "B": {}, "D": {}},
					 "D": {"A":{}, "B":{}, "C":{}}
					 }			
		graph = Graph(graph_dict, directed=False)
		graph.remove_edge("B", "A")
		graph.remove_edge("A", "D")
		self.assertEqual(graph.number_of_vertices(), 4)
		self.assertEqual(len(graph.incoming_vertices("A")), 1)
		self.assertEqual(len(graph.incoming_vertices("B")), 2)
		self.assertEqual(len(graph.incoming_vertices("C")), 3)
		self.assertEqual(len(graph.incoming_vertices("D")), 2)

	def test_graph_verify(self):
		graph_dict = {"A": {},
					 "B": {"A":{}, "C":{}},
					 "C": {"A": {}},
					 "D": {"A":{}, "B":{}, "C":{}}
					 }
		directed = Graph(graph_dict)
		self.assertRaises(ValueError, Graph, graph_dict, False)	


class PageRankTest(unittest.TestCase):

	def test_simple(self):
		graph_dict = {"A": {},
					 "B": {"A":{}, "C":{}},
					 "C": {"A": {}},
					 "D": {"A":{}, "B":{}, "C":{}}
					 }	
		graph = Graph(graph_dict)
		ranks = pagerank(graph, iterations=10)
		math.isclose(ranks["A"], 0.4583333)

	def test_with_iter_and_dampening(self):
		graph_dict = {"A": {},
					 "B": {"A":{}, "C":{}},
					 "C": {"A": {}},
					 "D": {"A":{}, "B":{}, "C":{}}
					 }			
		graph = Graph(graph_dict)
		ranks = pagerank(graph, iterations=0, d=1)
		math.isclose(ranks["A"], 0.50747)		
		math.isclose(ranks["B"], 0.27431)
		math.isclose(ranks["C"], 0.1925)
		math.isclose(ranks["D"], 0.15)


if __name__ == '__main__':
	unittest.main()

