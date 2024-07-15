'''
String Rotated by 2 Places
Difficulty: EasyAccuracy: 32.7%Submissions: 218K+Points: 2
Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating (in any direction) string 'a' by exactly 2 places.

Example 1:

Input:
a = amazon
b = azonam
Output: 
1
Explanation: 
amazon can be rotated anti-clockwise by two places, which will make it as azonam.
Example 2:

Input:
a = geeksforgeeks
b = geeksgeeksfor
Output: 
0
Explanation: 
If we rotate geeksforgeeks by two place in any direction, we won't get geeksgeeksfor.
Your Task:
The task is to complete the function isRotated() which takes two strings as input parameters and checks if given strings can be formed by rotations. The function returns true if string 1 can be obtained by rotating string 2 by two places, else it returns false.

Expected Time Complexity: O(N).
Expected Auxilary Complexity: O(N).
Challenge: Try doing it in O(1) space complexity.

Constraints:
1 ≤ length of a, b ≤ 105
'''

def isRotated(str1, str2):
    count = 1
    while(count <= 2):
        if ((str1[2:] + str1[0:2]) == str2):
            return count
        elif ((str2[2:] + str2[0:2]) == str1):
            return count
        count += 1
    return 0
print(isRotated("amazon", "azonam"))
print(isRotated("geeksforgeeks", "geeksgeeksfor"))
print(isRotated("daxjheq", "eqdaxjh"))