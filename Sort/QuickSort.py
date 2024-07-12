'''
Quick Sort:
- Divide and Conquer Algorithm
- It is a recursive algorithm that consists of two steps:
- Partitioning: It is used to partition the array around an element called pivot.
- Sorting: Recursively sort the subarrays.
'''

def quickSort(arrayValue):
    
    if(len(arrayValue) <= 1):
        return arrayValue

    pivot = arrayValue[len(arrayValue)//2] # Divide and Conquer
    left = [i for i in arrayValue if(i < pivot)] # Pivot with left comparison
    right = [i for i in arrayValue if(i > pivot)] # Pivot with right comparison
    middle = [i for i in arrayValue if(i == pivot)] # Pivot with middle comparison
    
    return (quickSort(left) + middle + quickSort(right))

# data = [1, 7, 4, 1, 10, 9, -2]
data = [1,2,3,2,5,6]
print(quickSort(data))