'''
Linked List - Using Class (Straight forward Approach) - Simple Way
'''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None # Pointer to the address



head = Node(1) 
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.next = node3

current = head # Temporary variable without affecting the head node

while(current != None):
    print(current.data)
    current = current.next # Next Node address is being pointed