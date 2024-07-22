"""
Binary Tree:
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

    def linkNode(self, data, node=None):

        if node.left is None:
            node.left = TreeNode(data)
        elif node.right is None:
            node.right = TreeNode(data)
        else:
            self.linkNode(data, node.left)

    def display(self, depth=0, node=None):
        if node is None:
            node = self.root

        print(" " * depth, node.data)

        if node.left:
            self.display(depth + 1, node.left)
        elif node.right:
            self.display(depth + 1, node.right)


bt = BinaryTree()
bt.addNode(1)
bt.addNode(7)
bt.addNode(6)
bt.addNode(8)
bt.addNode(2)
bt.display()
