'''
20. Valid Parentheses
Complexity : Easy
Topics: String , 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def validParanthesis(stringValue: list) -> bool:
    
    dictionary = {
        '(':')',
        '{':'}',
        '[':']' 
    }
    # We are going to apply stack concept
    stack = []
    for i in stringValue:
        if i in dictionary.keys():
            stack.append(i)
        else:
            if stack == [] :
                return 0
            else:
                if(dictionary[stack[-1]] == i):
                    stack.pop()
                else:
                    return 0
    return 1 if stack == [] else 0
        
stringValue = "{[()]}"

print(validParanthesis(stringValue))