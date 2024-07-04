'''
Insertion Sort:
- Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our
hands.
- Insertion sort iterates, consuming one input element each repetition and growing a sorted
output list.
- At each iteration, insertion sort removes one element from the input data, finds the location
it belongs within the sorted list, and inserts it there.
- It repeats until no input elements remain.
Simple : Considering the array as two arrays(without extra array) and then inserting one by one
'''

a = [1,3,7,2,9,0,11]

for index in range(1, len(a)):
    current = a[index]
    start = index - 1
    while(start >= 0 and current < a[start]):
        a[start + 1] = a[start]
        start = start - 1
    a[start + 1] = current
    
print(a)