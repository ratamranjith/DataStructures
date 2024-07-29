"""
Graph DataStructure:
- Graph is a non-linear data structure consisting of nodes or vertices connected by edges.
- Each node can have multiple edges connected to it.
- Each edge can have a weight or label associated with it.
- Graphs can be directed or undirected, meaning edges can have direction or not.
- Graphs can be weighted or unweighted, meaning edges can have weights or not.(Weighted is not in this program. it will be given separately)
"""


class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, vertex1, vertex2, isDirectional=False):
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isDirectional:
            self.graph[vertex2].append(vertex1)

    def display(self):
        for vertex in self.graph:
            print(vertex, " -> ", self.graph[vertex])
        print("-----------")

    def removeVertex(self, vertex):

        if vertex in self.graph:
            del self.graph[vertex]

        for key, value in self.graph.items():
            if vertex in value:
                value.remove(vertex)

    def removeEdge(self, vertex1, vertex2, isDirectional=False):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
            if not isDirectional:
                self.graph[vertex2].remove(vertex1)


graph = Graph()
graph.addEdge("A", "B")
graph.addEdge("B", "C")
graph.addEdge("C", "A", True)
graph.display()  # Output: A -> ['B'], B -> ['A', 'C'],
graph.removeVertex("B")
graph.removeEdge("A", "B")
graph.removeEdge("A", "C")
graph.display()
