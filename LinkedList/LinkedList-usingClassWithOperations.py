
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

    #------------------
    # Deleting the data
    def delete(self, dataValue):
        current = self.head
        
        if(current == None):
            print("Linked list is empty. Add data or value in the list and try again")
            return
        
        if(current.data == dataValue): # initial check - O(1)
            current = current.next
            return
        else: # O(n)
            while(current.next != None and current.next.data != dataValue): 
                current = current.next

            if(current.next != None and current.next.data == dataValue):
                current.next = current.next.next         

    #--------------------
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
ll.delete(20)
ll.print()