'''
Selection Sort:
- Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each
iteration and places that element at the beginning of the unsorted list.
- The algorithm maintains two sublists, a sorted sublist and a new sublist that is still to be
sorted. Initially, both sublists are empty.
- The elements are moved from the unsorted sublist to the sorted sublist, one at a time,
until no more elements remain in the unsorted sublist.
'''
from array import array

def selection_sort(arr):
    
    if(arr != None):
        for index in range(len(arr)-1):
            minimum = index
            for position in range(index +1 , len(arr)):
                if(arr[position] < arr[minimum]):
                    minimum = position
                    arr[index], arr[minimum] = arr[minimum], arr[index]
    else:
        print("Array is empty")
    return arr

#------------
# Using Array
ar = array('i', [1,6,8,3,2,0])
print(selection_sort(ar))

#------------
# Using List
list = [1,6,8,3,2,0]
print(selection_sort(list))