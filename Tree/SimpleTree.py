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

        currentParent = self.findNode(parentNode, self.root)
        if currentParent == None:
            print("Parent node not found")
            return

        currentParent.children.append(newNode)

    # Find the parent node - recursion is applied
    def findNode(self, parentNode, node=None):

        if node.data == parentNode:
            return node

        for child in node.children:
            nodeDetected = self.findNode(parentNode, child)
            if nodeDetected:
                return nodeDetected
        return None

    # Display the Tree Structure
    def display(self, node=None, prefix=""):
        if node is None:
            node = self.root
        print(prefix + str(node.data))
        for i, child in enumerate(node.children):
            if i == len(node.children) - 1:  # Last child
                self.display(child, prefix + "└── ")
            else:
                self.display(child, prefix + "├── ")

    # Deleting the node
    def removeNode(self, data, parentNode=None):

        if self.root is None:
            print("Root is not present in the tree")
            return

        if self.root.data == data:
            self.root = None
            return

        removeNodedata = self.findParentNode(data, self.root)

        if removeNodedata:
            for child in removeNodedata.children:
                if child.data == data:
                    removeNodedata.children.remove(child)

        return None

    # Find the parent node - recursion is applied
    def findParentNode(self, parentNode, node):

        for child in node.children:

            # finding only the child node
            if child.data == parentNode:
                return node

            nodeDetected = self.findParentNode(parentNode, child)
            if nodeDetected:
                return nodeDetected
        return None


tree = Tree()
tree.addNode(5)
tree.addNode(6, 5)
tree.addNode(7, 6)
tree.addNode(21, 6)
tree.addNode(9, 7)
tree.addNode(10, 7)
tree.addNode(11, 7)
tree.display()
tree.removeNode(11)
tree.display()
tree.removeNode(7)
tree.display()
