from queue import SimpleQueue

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