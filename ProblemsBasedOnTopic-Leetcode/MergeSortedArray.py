'''
88. Merge Sorted Array
Complexity: Easy
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

Topics
Array
Two Pointers
Sorting
'''
# Sorting the arrays - QuickSort
def mergeSortedArray(nums1, m, nums2, n):
    if(len(nums1) < 1 and len(nums2) > 1):
        return nums2
    elif(len(nums2) < 1 and len(nums1) > 1):
        return nums1
    count = 0
    
    # Merging both arrays
    for i in range(len(nums1)):
       if(nums1[i] == 0):
           nums1[i] = nums2[count]
           count += 1

    def quickSort(arrayValue):
        
        if(len(arrayValue) <= 1):
            return arrayValue

        pivot = arrayValue[len(arrayValue)//2] # Divide and Conquer
        left = [i for i in arrayValue if(i < pivot)] # Pivot with left comparison
        right = [i for i in arrayValue if(i > pivot)] # Pivot with left comparison
        middle = [i for i in arrayValue if(i == pivot)] # Pivot with middle comparison
        
        return (quickSort(left) + middle + quickSort(right))         
    return quickSort(nums1)


nums1 = [1,2,3,0,0,0]
m = 6
nums2 = [2,3,4]
n = 3

print(mergeSortedArray(nums1, m, nums2, n))