
#--------------
# Node Template
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#---------------------
# Linked list - single
class LinkedList:
    def __init__(self):
        self.head = None
    
    #------------
    # Adding Data
    def add(self, dataValue):
        newNode = Node(dataValue)
        if (self.head == None):
            self.head = newNode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newNode

    #-----------
    # Displaying the data
    def print(self):
        current = self.head 
        
        while(current is not None):
            print(current.data)
            current = current.next

ll = LinkedList()
dataList = [1,2,3,4,5,6,7,8,9,10]
for i in dataList:
    ll.add(i)

ll.print()