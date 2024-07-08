'''
Merge Sort:
- Divide and Conquer Algorithm
- Divide the array into two halves, sort each half recursively, and then merge the two sorted halves
- Time Complexity: O(nlogn)
- Space Complexity: O(n)
'''
def mergeSort(arrayList):
    
    if(len(arrayList) > 1):
        # Splitting - Divide and Conquer
        middle = len(arrayList)//2
        left   = arrayList[:middle]
        right  = arrayList[middle:]
        
        mergeSort(left)
        mergeSort(right)
    
    
        # Sorting
        leftPoint  = 0
        rightPoint = 0
        fullPoint  = 0
        
        while(leftPoint < len(left) and rightPoint < len(right)):
            
            if(left[leftPoint] < right[rightPoint]):
                arrayList[fullPoint] = left[leftPoint]
                leftPoint += 1
            else:
                arrayList[fullPoint] = right[rightPoint]
                rightPoint += 1
            fullPoint += 1
            
        # Merging left
        while(leftPoint < len(left)):
            arrayList[fullPoint] = left[leftPoint]
            leftPoint += 1
            fullPoint += 1
        
        # Merging right
        while(rightPoint < len(left)):
            arrayList[fullPoint] = left[rightPoint]
            rightPoint += 1
            fullPoint += 1
    return arrayList

    
arr = [9,6,3,6,1,2,0,2,4,78,1,3,5,8,223,652,22]
print(mergeSort(arr))
