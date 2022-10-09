"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# https://leetcode.com/problems/climbing-stairs/solutions/251248/python-3-dp-solution/?languageTags=python3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        else:
            first_step = 1 
            second_step = 2
            total=0
            for i in range(3, n+1):
                total = first_step + second_step
                first_step = second_step
                second_step = total
            return total