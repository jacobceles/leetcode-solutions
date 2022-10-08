"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(set(s))
        if length in [1, 0]:
            return length
        else:
            output = 0
            flag = True
            for i in range(0, len(s)):
                processed = []
                for j in range(i, len(s)):
                    if s[j] in processed:
                        flag = True
                        break
                    else:
                        if flag:
                            substring = ""
                            flag = False
                        substring += s[j]
                        processed.append(s[j])
                    if j == len(s)-1:
                        flag = True
                if output < len(substring):
                    output = len(substring)
        return output
