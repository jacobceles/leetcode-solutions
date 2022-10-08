"""
20. Valid Parentheses

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
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if s.startswith(("}", "]", ")")) or len(s)<2:
            return False
        
        opening_brackets = []
        brackets = { '(' : ')', '{' : '}', '[' : ']' }        
        for item in list(s):
            # append to a list if its an open bracket
            if item in ['(', '{', '[']:
                opening_brackets.append(item)
            else:
                # return false if we see closing brackets first
                if opening_brackets:
                    # check if last openng and closing brackets match
                    if item == brackets[opening_brackets[-1]]:
                        opening_brackets.pop()
                    else:
                        return False
                else:
                    return False

        # means the string had more opening brackets
        if len(opening_brackets)==0:
            return True

        return False
