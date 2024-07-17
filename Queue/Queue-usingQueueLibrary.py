from queue import SimpleQueue, Queue, PriorityQueue

from collections import deque

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


#------------------------------
# 3. Deque (Double ended queue)
#------------------------------
deque = deque()

# Insert
deque.append(5)     # deque([5])
deque.appendleft(2) # deque([2, 5])
deque.append(3)     # deque([2, 5, 3])
deque.appendleft(4) # deque([4, 2, 5, 3])
deque.append(3)     # deque([4, 2, 5, 3, 3]) 
deque.append(6)     # deque([4, 2, 5, 3, 3, 6]) 

print(deque)

# Deletion
print(deque.pop()) # Removes from backside
print(deque.popleft()) # Removes from frontside

#------------------
# 4. Priority Queue
#------------------
priQue = PriorityQueue()

# Insertion
priQue.put(5)
priQue.put(5)
priQue.put(5)
priQue.put_nowait(10) # Most Priority has been moved to index 0
priQue.put(0)
priQue.put(2)
priQue.put(1)
priQue.put(5)
print(priQue.queue) # [0, 5, 1, 5, 5, 5, 2, 10]

#deletion
print(priQue.get_nowait()) # 0 : Least one will be removed
print(priQue.queue) # [1, 5, 2, 5, 5, 5, 10]