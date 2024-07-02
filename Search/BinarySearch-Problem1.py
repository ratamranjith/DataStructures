'''
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

'''

def findMedianSortedArrays(nums1, nums2):
    
    list1Length = len(nums1)
    list2Length = len(nums2)
    evenOrOdd = "even" if((list1Length + list2Length)%2 == 0) else "odd"
    sortedValue = sorted(nums1 + nums2)
    value = len(sortedValue)//2
    print(value)
    if(evenOrOdd == "even"):
        return (sortedValue[int(value)] + sortedValue[int(value)-1])/2
    else:
        return float(sortedValue[int(value)])
    
print(findMedianSortedArrays([1,3], [2]))