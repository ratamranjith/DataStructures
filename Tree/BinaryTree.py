"""
Binary Tree: Unbalanced
- A tree is a data structure that consists of nodes connected through edges.
- A binary tree is a tree data structure in which each node has at most two children, which
are referred to as the left child and the right child.
"""


class TreeNode:
    # Constructor for Tree Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    # Constructor for Binary Tree
    def __init__(self):
        self.root = None

    def addNode(self, data):

        # Create a new node
        newNode = TreeNode(data)

        if self.root is None:
            self.root = newNode
            return

        # Use recursion method to add nodes
        addedNode = self.linkNode(data, self.root)

    def linkNode(self, data, node):
        if node.left is None:
            node.left = TreeNode(data)
        elif node.right is None:
            node.right = TreeNode(data)
        else:
            self.linkNode(data, node.left)

    def display(self, node=None, depth=0):
        if node is None:
            node = self.root

        if node:
            print("  " * depth, node.data)
            if node.left:
                self.display(node.left, depth + 1)
            if node.right:
                self.display(node.right, depth + 1)

    def removeNode(self, dataValue):

        if self.root == dataValue:
            self.root = None

        self.removeRecursively(dataValue, self.root)

    def removeRecursively(self, data, node):

        if node.left and node.left.data == data:
            node.left = None
            return
        if node.right and node.right.data == data:
            node.right = None
            return
        if node.left:
            self.removeRecursively(data, node.left)
        if node.right:
            self.removeRecursively(data, node.right)


bt = BinaryTree()
bt.addNode(1)
bt.addNode(7)
bt.addNode(6)
bt.addNode(8)
bt.addNode(2)
bt.addNode(5)
bt.addNode(8)
bt.addNode(9)
bt.addNode(10)
bt.addNode(11)
bt.addNode(12)
bt.display()
bt.removeNode(10)
bt.display()
