'''
Linear Search:
- Linear search is a search algorithm for finding an element in a list. It iterates the 
list sequentially until it finds the element or the end of the list is reached.
- The time complexity of linear search is O(n) where n is the number of elements in the
list.
- Linear Search will be useful, when an array value is not in order
'''
# Using Array, not the list
from array import array

def linearSearch(list, value):   
    if(len(list) != 0):
        for i in range(len(list)):
            if(list[i] == value):
                return "search Found in index : {}".format(i)
        else:
            return "search not found"

a = array("i", [1,3,4,6,8,9,2,1,7])
print(linearSearch(a, 3))