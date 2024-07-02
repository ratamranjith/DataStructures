'''
Binary Search:
- Binary search is a search algorithm that finds the position of a target value within a sorted array
- Binary search compares the target value to the middle element of the array
- If they are not equal, the half in which the target cannot lie is eliminated and the search
continues on the remaining half, again taking the middle element to compare to the target value,
and repeating this until the target value is found.
- If the search ends with the remaining half being empty, the target is not in the array.
'''

# Using only Array, not list
from array import array

def binarySearch(list, searchValue, sortedValue=False):
    
    #----------------------------------
    # We need to sort it, it not sorted
    if(sortedValue == False):
        list = sorted(list)
    
    minValue = 0
    maxValue = len(list) - 1
    
    while(minValue <= maxValue):
        middle = (minValue + maxValue)//2
        if(list[middle] == searchValue):
            return "Value Found: {} in index {}: ".format(list[middle], middle)
        else:
            if(searchValue < list[middle]):
                maxValue = middle - 1
            else:
                minValue = middle + 1
    else:
        return "Value Not Found in any of the index"

ar = array('i', [6,7,8,3,2,5,6,1])    
value = 3
print(binarySearch(ar, value, False))