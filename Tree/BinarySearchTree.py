"""
Binary Search Tree:
- A binary tree where each node has at most two children
- A binary search tree is a binary tree where the values of each node are greater than or equal
to the values in the left subtree and less than or equal to the values in the right subtree
- Elements or values should be in sorted order.
- Duplicates will be neglected
"""


class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def addNode(self, data):

        if not self.root:
            self.root = BinaryTree(data)

        # ---------------------------------------------
        # Applying the recursive method to add the data
        else:
            self.addRecursively(data, self.root)

    def addRecursively(self, data, node):

        if node is None:
            node = self.root

        # ----------------------------------------------
        # If the data is less than the node's data, then
        # add the data to the left subtree
        if data < node.data:
            if node.left:
                self.addRecursively(data, node.left)
            else:
                node.left = BinaryTree(data)
        elif data > node.data:
            if node.right:
                self.addRecursively(data, node.right)
            else:
                node.right = BinaryTree(data)

    def display(self):

        result = []  # appending the sorted values in this list

        self.inOrderTraversal(self.root, result)
        print(result)

    def inOrderTraversal(self, node, result):

        if node is None:
            return None
        else:
            self.inOrderTraversal(node.left, result)
            result.append(node.data)
            self.inOrderTraversal(node.right, result)

    def search(self, data, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        if node.data == data:
            return node
        if data < node.data:
            return self.search(data, node.left)
        return self.search(data, node.right)


bst = BinarySearchTree()
elements = [45, 10, 50, 4, 1, 5, 5, 100, 60]
for element in elements:
    bst.addNode(element)

bst.display()
search = "Search Found" if (bst.search(1)) else "Search Not Found"
print(search)
