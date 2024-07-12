'''
Two Pointer Algorithm: Unsorted and Sorted Array - Leetcode
Problem Name: Two Sum
Problem Link: https://leetcode.com/problems/two-sum/
'''



def twoSum(nums, target):
    hashMap = {}
    for i, nums in enumerate(nums):
        finalValue = target - nums
        if finalValue in hashMap:
            return [hashMap[finalValue], i]
        hashMap[nums] = i
    else:
        return [-1, -1]
       
        
arr = [3,2,5]
target = 7
        
print(twoSum(arr, target))