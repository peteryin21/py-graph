"""PageRank Algorithm"""


def pagerank(graph, iterations=10, d=0.85):
	""" Calculate PageRank of vertices in a graph

	Paramters
	----------
	graph : Graph 
		Graph object on which to perform PageRank analysis
	iterations : int
		Number of iterations in PageRank calculation
	d : float
		Dampening factor in PageRank algorithm

	Returns
	-------
	pagerank: dictionary
		Dictionary of vertices with PageRank values

	"""

	num_v = graph.number_of_vertices()
	# Initialize ranks to 1/N
	ranks = dict.fromkeys(graph.graph_dict, 1.0/float(num_v))
	for _ in range(iterations):
		for vertex, edges in graph.graph_dict.items():
			incoming = graph.incoming_vertices(vertex)
			weighted_ranks = [ranks[v]/len(graph.graph_dict[v]) for v in incoming]
			ranks[vertex] = (1-d) + d*sum(weighted_ranks)
	return ranks

