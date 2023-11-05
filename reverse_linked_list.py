'''
Leetcode: https://leetcode.com/problems/reverse-linked-list
Time complexity: O(n)
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while(curr != None):
            next_one = curr.next
            curr.next = prev
            prev = curr
            curr = next_one
        return prev    
