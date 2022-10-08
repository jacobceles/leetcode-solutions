"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        shortest_string = min(strs, key=len)
        
        if shortest_string == output:
            return output
        
        flag = False
        for i in range(len(shortest_string)):        
            for item in strs:
                if item[i]==shortest_string[i]:
                    flag=True
                else:
                    flag=False
                    break
            if flag:
                output+=shortest_string[i]
            else:
                return output
        return output