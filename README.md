# Python Graph Library + PageRank 

A simple graph library that provides essential graph creation, manipulation and analysis tools, including the PageRank algorithm.

This implementation has support for directed and undirected graphs, as well as generic nodes that can support arbitrary (hashable) data. 

## Example usage

```
>>> graph = Graph()
>>> graph.add_vertex("A")
>>> graph.add_vertex(1)
>>> graph.add_vertex(2.4)
>>> graph.add_edge("A", 1)
>>> graph.add_edge(2.4,1)
>>> graph.add_edge(1, 2.4)
>>> pagerank(graph)
{1: 1.419611292896683, 2.4: 1.3566695989621804, 'A': 0.15000000000000002}
```

## Run unit tests
```
python3 test.py
```
