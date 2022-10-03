"""
# 234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 
Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Convert into a normal list to make life easier
        inp = list()
        while head is not None:
            inp.append(head.val)
            head=head.next
        # Get length, middle value, and first half
        inp_length = len(inp)
        inp_middle = int(len(inp)/2)
        first_half = inp[:inp_middle]
        # Get second half and reverse it
        if inp_length%2==0:
            second_half=inp[inp_middle:][::-1]
        else:
            second_half=inp[inp_middle+1:][::-1]
        # Check if pallindrome
        if first_half==second_half:
            return True
        return False