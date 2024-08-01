"""
Graph Data Structure: Breadth First Traversal

Explanation:
The Breadth First Traversal (BFS) is a graph traversal algorithm that visits all the nodes
at the present depth prior to moving on to nodes at the next depth level. It uses a queue
data structure to keep track of the nodes to be visited.

Steps:
1. Create a queue and enqueue the root node.
2. While the queue is not empty, dequeue a node and visit it.
3. Enqueue all the unvisited neighbors of the dequeued node.
4. Repeat steps 2 and 3 until the queue is empty.

Here, we are going to have the list
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
        if vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)
        if vertex2 not in self.graph[vertex1] and not isBidirectional:
            self.graph[vertex1].append(vertex2)

    def removeVertex(self, vertex):

        if vertex in self.graph:
            del self.graph[vertex]

        for adjacentVertex in self.graph:
            if vertex in self.graph[adjacentVertex]:
                self.graph[adjacentVertex].remove(vertex)

    def removeEdge(self, vertex1, vertex2, isBidirectional=False):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        elif (
            not isBidirectional
            and vertex2 in self.graph
            and vertex1 in self.graph[vertex2]
        ):
            self.graph(vertex2).remove(vertex1)

    def display(self):

        for vertex, edges in self.graph.items():
            print(vertex, "->", edges)

    def breadthFirstTraversal(self, start):

        visited = {start}  # Set
        notVisited = [start]  # consider it as Queue

        while len(notVisited) > 0:
            currentValue = notVisited.pop()
            print(currentValue, end=" ")

            for children in self.graph[currentValue]:
                if children not in visited:
                    notVisited.append(children)
                    visited.add(children)
        print("", end="\n")


graph = Graph()
graph.addEdge("A", "B")
graph.addEdge("B", "C")
graph.addEdge("C", "D")
graph.addEdge("D", "E")
graph.addEdge("D", "F")
graph.addEdge("E", "F")
graph.display()
graph.breadthFirstTraversal("A")
graph.breadthFirstTraversal("E")
