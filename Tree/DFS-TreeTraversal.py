"""
Tree (Binary Search Tree): Depth First Search:
1. PreOrder Traversal:
    - Root -> Left -> Right
2. InOrder Traversal:
    - Left -> Root -> Right
3. PostOrder Traversal:
    - Left -> Right -> Root
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def addNode(self, data):

        if self.root is None:
            self.root = TreeNode(data)

        self.addRecursively(data, self.root)

    def addRecursively(self, data, node):

        if not node:
            node = self.root

        if node.data < data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.addRecursively(data, node.left)

        if node.data > data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.addRecursively(data, node.right)
        return node

    def display(self, type="inOrder"):  # type -> inOrder, preOrder, postOrder

        result = []  # appending the sorted values in this list
        match type:
            case "inOrder":
                self.inOrderTraversal(self.root, result)
                print(result)
            case "preOrder":
                self.preOrderTraversal(self.root, result)
                print(result)
            case "postOrder":
                self.postOrderTraversal(self.root, result)
                print(result)
            case _:
                print("Enter the correct type")

    def inOrderTraversal(self, node, result):

        if node is None:
            return None
        else:
            self.inOrderTraversal(node.left, result)
            result.append(node.data)
            self.inOrderTraversal(node.right, result)

    def preOrderTraversal(self, node, result):

        if node is None:
            return None
        else:
            result.append(node.data)
            self.preOrderTraversal(node.left, result)
            self.preOrderTraversal(node.right, result)

    def postOrderTraversal(self, node, result):

        if node is None:
            return None
        else:
            self.postOrderTraversal(node.left, result)
            self.postOrderTraversal(node.right, result)
            result.append(node.data)


bst = BinarySearchTree()
bst.addNode(5)
bst.addNode(6)
bst.addNode(7)
bst.addNode(8)
bst.addNode(90)
bst.display()
bst.display("preOrder")
bst.display("postOrder")
