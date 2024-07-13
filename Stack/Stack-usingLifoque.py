from queue import LifoQueue

stack = LifoQueue(maxsize=5)

# Initializing a stack
stack = LifoQueue(maxsize=3)
print(stack.qsize)

# Insertion 
stack.put(9)
stack.put(2)
stack.put('7')
print(stack)

# get - will remove the value one by one when get it called
print(stack.get()) 
print(stack.get()) 
print(stack.get())

# Check the stack is empty or not
print(stack.empty())
print(stack.get()) # will makes the program to freeze
print("Came") # Will not come to this line

# Note: we need to use this methods carefully