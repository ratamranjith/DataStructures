'''
Python: SlidingWindow Algorithm

The sliding window algorithm is a technique used to efficiently process a section (or "window") of data from a larger dataset, 
like an array or a string, without repeatedly recalculating everything from scratch.

How It Works:

- Imagine a Window: Think of a window that you can move across an array or string. This window can have a fixed size or change size as needed.
- Sliding the Window: As you move this window from one end of the array to the other, you analyze the data inside the window. Instead of starting fresh each time you move the window, you update your calculations based on the changes as the window moves.
- Efficiency: This approach saves time because you don’t have to reprocess data that was already part of the previous window; you just adjust your results as the window moves.

This Algorithm can be explained with below problem,

209. Minimum Size Subarray Sum
Medium
Topics
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''

def minSubArray(target, nums):
    
    length = len(nums)
    left = 0
    right = 0
    subSum = 0
    minLen = 1000000000000 # am giving max number in order to find the minimum number
    
    while(right < length):
        subSum += nums[right] # adding the array values one by one
        
        while(subSum >= target): # Here comparing the sum with the target
           minLen = min(minLen, right-left+1)
           subSum -=  nums[left]
           left += 1
        
        right += 1 
    
    return 0 if minLen == 0 else minLen
    
target = 7
nums = [2,3,1,2,4,3]

print(minSubArray(target, nums)) # output : 2