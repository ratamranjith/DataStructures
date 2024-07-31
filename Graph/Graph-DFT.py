"""
Graph Data Structure: Depth First Traversal technique
"""


class Graph:

    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, vertex1, vertex2, isBidirectional=False):
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isBidirectional:
            self.graph[vertex2].append(vertex1)

    def removeVertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]

        for vertices, values in self.graph:
            if vertex in values:
                values.remove(vertex)

    def removeEdge(self, vertex1, vertex2, isBidirectional=False):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
            if not isBidirectional:
                self.graph[vertex2].remove(vertex1)

    def isEdge(self, vertex1, vertex2):
        if vertex1 in self.graph[vertex2] and vertex2 in self.graph[vertex1]:
            return True
        return False

    def display(self):
        """Prints the adjacency list representation of the graph."""
        if not self.graph:
            print("Graph is empty.")
            return

        for vertex, children in self.graph.items():
            print(f"{vertex} --> {', '.join(map(str, children))}")

    def dfs_traversal(self, start, alreadyVisited=set()):

        if start not in alreadyVisited:
            alreadyVisited.add(start)
            print(f"{start} ", end="")
        for childrenEdge in self.graph[start]:
            if childrenEdge not in alreadyVisited:
                self.dfs_traversal(childrenEdge, alreadyVisited)


graph = Graph()
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("B", "D")
graph.addEdge("B", "F")
graph.addEdge("D", "F")
graph.display()
graph.dfs_traversal("A")
