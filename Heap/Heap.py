'''
Heap: Data Structure

Description:
    Heap is a specialized tree-based data structure that satisfies the heap property. It is a complete binary tree
where each parent node is either greater than (max heap) or less than (min heap) its
children. This property makes heap a useful data structure for sorting and priority queue operations.

Explanation:
- A max heap is a complete binary tree where each parent node is greater than its children.
- A min heap is a complete binary tree where each parent node is less than its children.
- The root node of the heap is the maximum or minimum value in the heap, depending on whether
it's a max heap or min heap.
We will cover both here
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class HeapDS: # Code is similar to binary tree

    def __init__(self):
        self.root = None

    def add_node(self, data):
        
        treeNode = TreeNode(data)
        if not self.root:
            self.root = treeNode
            return 

        return self.add_recursively(data, self.root)
    
    def add_recursively(self, data, node):
        
        tree_node = TreeNode(data)
        
        if not node.left:
            node.left = tree_node
        elif not node.right:
            node.right = tree_node
        else:
            if self.count_node(node.left) <=  self.count_node(node.right):
                self.add_recursively(data, node.left)
            else:
                self.add_recursively(data, node.right)    
    
    def count_node(self, node):
        
        if not node:
            return 0
        
        return 1 + self.count_node(node.left) + self.count_node(node.right)
        
        
        
heap = HeapDS()

heap.add_node(5)
heap.add_node(6)
heap.add_node(7)
heap.add_node(8)
heap.add_node(9)
heap.add_node(10)
heap.add_node(11)
heap.add_node(12)

print(heap)