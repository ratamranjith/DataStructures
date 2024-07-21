"""
Tree DataStructure:
- A tree is a non-linear data structure consisting of nodes in which each node is connected to
other nodes by directed edges.
- A tree is a connected, undirected graph with no cycles.
"""


# -------------------------------
# Tree Node Template - Using this
# multiple nodes can be created
class TreeNode:

    # Constructor
    def __init__(self, data):
        self.data = data
        self.children = []


# -----------
# Tree Class
class Tree:

    # Constructor
    def __init__(self):
        self.root = None

    def addNode(self, data, parentNode=None):

        newNode = TreeNode(data)

        # Check root node is created.
        if self.root == None:
            self.root = newNode
            return

        currentParent = self.findParentNode(parentNode, self.root)
        if currentParent == None:
            print("Parent node not found")
            return

        currentParent.children.append(newNode)

    # Find the parent node - recursion is applied
    def findParentNode(self, parentNode, node):

        if node.data == parentNode:
            return node

        for child in node.children:
            nodeDetected = self.findParentNode(parentNode, child)
            if nodeDetected:
                return nodeDetected
        return None

    # Display the Tree Structure
    def display(self, depth=0, node=None):

        if node is None:
            node = self.root
        print("  " * depth, node.data)
        for child in node.children:
            self.display(depth + 1, child)


tree = Tree()
tree.addNode(5)
tree.addNode(6, 5)
tree.addNode(7, 6)
tree.addNode(21, 6)
tree.addNode(9, 7)
tree.addNode(10, 7)
tree.addNode(11, 7)

tree.display()
