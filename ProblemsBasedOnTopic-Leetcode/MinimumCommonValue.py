"""
2540. Minimum Common Value
Easy
Topics
Companies
Hint
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 
Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
"""


def getCommon(nums1, nums2):
    i, j = 0, 0

    def find(i, j):
        if i >= len(nums1) or j >= len(nums2):
            return -1
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            return find(i + 1, j)
        else:
            return find(i, j + 1)

    return find(i, j)


print(getCommon([1, 2, 3], [2, 4]))
print(getCommon([1, 1, 2], [2, 4]))
print(getCommon([4, 12, 13], [2, 4]))
