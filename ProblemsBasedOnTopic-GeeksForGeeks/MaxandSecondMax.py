'''
Max and Second Max
Difficulty: EasyAccuracy: 41.08%Submissions: 92K+Points: 2
Given an array arr[] of size N of positive integers which may have duplicates. 
The task is to find the maximum and second maximum from the array, and both of them should be different from each other, 
so If no second max exists, then the second max will be -1.

Example 1:

Input:
N = 3
arr[] = {2,1,2}
Output: 2 1
Explanation: From the given array 
elements, 2 is the largest and 1 
is the second largest.
Example 2:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 5 4
Explanation: From the given array 
elements, 5 is the largest and 4 
is the second largest.
Your Task:
The task is to complete the function largestAndSecondLargest(), which should return maximum and second maximum element from the array with first element as maximum element and second element as second maximum(if there is no second maximum the  second element should be -1)

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
1 <= arr[i] <= 106
'''
def largestAndSecondLargest(sizeOfArray, arr):
    
    firstLargest  = 0
    secondLargest = 0
    for i in arr:
        if i > firstLargest:
           secondLargest = firstLargest
           firstLargest = i
        elif i > secondLargest and i != firstLargest:
            secondLargest = i
        else:
            secondLargest = -1
    return firstLargest, secondLargest
    
arr = [10, 10, 10, 10, 10, 10]
size = 16

print(largestAndSecondLargest(size, arr))