from collections import deque

stack = deque([1,2,3,4,5,9,0])

# Insertion 
stack.append(9) # will insert at the end time & space : O(1)
print(stack)

# Access
print(stack[-1]) # will access the last element based on the negative index and time & space : O(1)
print(stack[2]) # will access the indexed value in between time & space : 0(n)

# Search
print(9 in stack) # will search the element in the stack and time & space : O(n)

# Delete
stack.pop() # will delete the last element in the stack and time & space : O(1)
print(stack)