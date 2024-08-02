"""
Graph DataStructures: Weighted

Explanation:
This code defines a WeightedGraph class that represents a weighted graph data structure. It includes methods for
adding edges, removing edges, getting the number of edges, getting the number of vertices, and checking
if a vertex is in the graph.

Steps:
1. Import the necessary modules.
2. Define the WeightedGraph class with an adjacency list representation.
3. Implement the add_edge method to add an edge to the graph.
4. Implement the remove_edge method to remove an edge from the graph.
5. Implement the get_num_edges method to get the number of edges in the graph.
6. Implement the get_num_vertices method to get the number of vertices in the graph.
7. Implement the has_vertex method to check if a vertex is in the graph.
"""


class WeightedGraph:

    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def addEdges(
        self, sourceLocation, destinationLocation, distance, isDirectional=False
    ):
        self.addVertex(sourceLocation)
        self.addVertex(destinationLocation)

        self.graph[sourceLocation][destinationLocation] = distance
        if not isDirectional:
            self.graph[destinationLocation][sourceLocation] = distance


weight = WeightedGraph()
weight.addEdges("Chennai", "Madurai", "350-km")
weight.addEdges("Chennai", "Banglore", "250-km")
print(weight.graph)
