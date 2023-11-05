'''
Leetcode: https://leetcode.com/problems/merge-two-sorted-lists
Time complexity: O(n)
'''

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2 == None:
            return l1
        elif l2 and l1 == None:
            return l2    

        elif l1 == None and l2 == None:
            return l1    

        dummy = ListNode
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next
