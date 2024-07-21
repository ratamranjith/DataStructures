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

    # Find the parent node - recursion is applied
    def findParentNode(self, parentNode, node):

        if node.data == parentNode:
            return node.data

        for child in node.children:
            return self.findParentNode(parentNode, child)

        return None


tree = Tree()
tree.addNode(5)
tree.addNode(6, 5)
