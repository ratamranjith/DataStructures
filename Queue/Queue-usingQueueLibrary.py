from queue import SimpleQueue, Queue

#--------------------
# 1. SimpleQueue
#--------------------
queue = SimpleQueue()
# Insert
queue.put(5)

# Size of queue after insertion
print(queue.qsize())  #1

# Delete
print(queue.get()) #5

# Size of queue after deletion
print(queue.qsize()) # 0

# IsEmpty
print(queue.empty()) # True

#---------------------
# 2. Queue
#---------------------
queue1 = Queue(maxsize=3) # If given, it is the length or else it is unlimited, whenever the insertion happens, size may vary

# Insert
queue1.put(5)
queue1.put(2)
queue1.put(1)

# Check queue is full
print(queue1.full()) # True

# Size of the queue after insertion
print(queue1.qsize()) #1

# Delete
print(queue1.get()) #5

# Size of queue after deletion
print(queue1.qsize()) # 0

# IsEmpty
print(queue1.empty()) # True