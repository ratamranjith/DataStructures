'''
Two Pointer Algorithm (Sorted Array):
- Two pointers are used to iterate through a list or array(must be sorted).
- The two pointers are usually initialized to the first and last elements of the list/array.
- The pointers are then moved towards each other, comparing the elements they point to.
- The algorithm terminates when the pointers meet or cross each other.
'''
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    leftPointer = 0
    rightPointer = len(nums) - 1
    while(leftPointer < rightPointer):
        sumResult = (nums[leftPointer] + nums[rightPointer])
        if(sumResult == target):
            return ([leftPointer, rightPointer])
        elif(sumResult < target):
            leftPointer += 1
        else:
            rightPointer -= 1
    else:
        return ([-1, -1])
arr = [1,2,3,4,5,6]
# arr = [3,2,4]
target = 8
print(twoSum(arr, target))