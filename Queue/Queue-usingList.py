'''
Simple Queue using List - FIFO
'''

queue = []

# Insertion
def enqueue(value):
    global queue
    return queue.append(value)

# Deletion
def dequeue():
    global queue
    return queue.pop(0)

# Access
def access():
    global queue
    return queue[0]

enqueue(5)
enqueue(6)
enqueue(7)
enqueue(8)
enqueue(9)
enqueue(10)
print(queue)

# Front
print(access())

dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
print(queue)

# IsEmpty
print(len(queue) == 0)