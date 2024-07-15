'''
Longest Common Prefix of Strings
Difficulty: Easy
Accuracy: 29.52%
Submissions: 254K+
Points: 2
Given an array of strings, Return the longest common prefix among all strings present in the array. If there's no prefix common in all the strings, return "-1".

Examples

Input: n = 4, arr[] = [geeksforgeeks, geeks, geek, geezer]
Output: gee
Explanation: "gee" is the longest common prefix in all the given strings.


Input: n = 2, arr[] = [hello, world]
Output: -1
Explanation: There's no common prefix in the given strings.
Expected Time Complexity: O(n*min(|arri|))
Expected Space Complexity: O(min(|arri|))

Constraints:
1 ≤ n ≤ 103
1 ≤ arr[i] ≤ 103
'''

def longestCommonPrefix(n, arr):
    
    arr = sorted(arr)
    minimum = len(arr[0])
    minValue = arr[0]
    count = 1
    while(n > count):
        if arr[count][:minimum] == minValue[:minimum]:
            minValue = arr[count][:minimum]
            count += 1
        else:
            minimum -= 1
    return minValue if len(minValue) > 0 else -1
    

print(longestCommonPrefix(2 , ['hello', 'world']))
print(longestCommonPrefix(4 , ['geeksforgeeks', 'geeks123', 'geek234', 'geezer']))